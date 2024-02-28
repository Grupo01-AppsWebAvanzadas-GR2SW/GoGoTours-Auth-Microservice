from flask import render_template, request, redirect, url_for, session, flash
from flask.views import MethodView
from injector import inject
from src.application.tourist_packages.services.tourist_packages_service_async import TouristPackagesServiceAsync
from src.application.tourist_packages.dtos.tourist_packages_request_dto import TouristPackagesRequestDto
from src.application.tourist_packages.dtos.tourist_packages_response_dto import TouristPackagesResponseDto
from src.extensions.decorations_extension import admin_required, admin_required_async


class PackageEditView(MethodView):

    @inject
    def __init__(self, tourist_packages_service: TouristPackagesServiceAsync):
        self._tourist_packages_service = tourist_packages_service

    @admin_required_async
    async def get(self, name):
        package = await self._tourist_packages_service.get_tourist_package_by_name(name)
        return render_template("packagesManager/edit_package.html", package=package)

    @admin_required_async
    async def post(self, name):
        previous_name = request.form.get("previous_name")
        update_name = request.form.get("updatePackageName")
        update_description = request.form.get("updatePackageDescription")
        update_destination = request.form.get("updatePackageDestinationPlace")
        update_duration = request.form.get("updatePackageDuration")
        update_capacity = request.form.get("updatePackageMaxCapacity")
        update_cost = request.form.get("updatePackageCost")
        update_start_Date = request.form.get("updatePackageStateDate")
        update_end_Date = request.form.get("updatePackageEndDate")
        update_image = request.form.get("updatePackageUrl")
        update_admin_id = session.get('id')

        update_package_dto = TouristPackagesRequestDto(
            name=update_name,
            description=update_description,
            destination_place=update_destination,
            duration=int(update_duration),
            max_capacity=int(update_capacity),
            cost=float(update_cost),
            start_date=update_start_Date,
            end_date=update_end_Date,
            image=update_image,
            admin_id=update_admin_id
        )
        await self._tourist_packages_service.edit_package(previous_name, update_package_dto)
        return redirect(url_for('package_detail', name=update_name))

