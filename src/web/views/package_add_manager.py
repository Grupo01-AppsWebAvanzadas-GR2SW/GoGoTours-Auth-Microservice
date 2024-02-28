from asgiref.sync import async_to_sync
from flask import render_template, request, redirect, url_for, session
from flask.views import MethodView
from injector import inject

from extensions.decorations_extension import admin_required, admin_required_async
from src.application.tourist_packages.services.tourist_packages_service_async import TouristPackagesServiceAsync
from src.application.tourist_packages.dtos.tourist_packages_request_dto import TouristPackagesRequestDto


class PackageAddView(MethodView):

    @inject
    def __init__(self, tourist_packages_service: TouristPackagesServiceAsync):
        self._tourist_packages_service = tourist_packages_service

    @admin_required
    def get(self):
        # packages = await self._tourist_packages_service.get_tourist_packages()
        return render_template("packagesManager/add_Package.html")

    @admin_required_async
    async def post(self):
        package_name = request.form.get("packageName")
        package_description = request.form.get("packageDescription")
        package_destination = request.form.get("packageDestinationPlace")
        package_duration = request.form.get("packageDuration")
        package_capacity = request.form.get("packageMaxCapacity")
        package_cost = request.form.get("packageCost")
        package_start_Date = request.form.get("packageStateDate")
        package_end_Date = request.form.get("packageEndDate")
        package_image = request.form.get("packageUrl")
        package_admin_id = session.get('id')

        package_dto = TouristPackagesRequestDto(
            name=package_name,
            description=package_description,
            destination_place=package_destination,
            duration=int(package_duration),
            max_capacity=int(package_capacity),
            cost=float(package_cost),
            start_date=package_start_Date,
            end_date=package_end_Date,
            image=package_image,
            admin_id=package_admin_id
        )
        await self._tourist_packages_service.add_package(package_dto)
        return redirect(url_for("home"))
