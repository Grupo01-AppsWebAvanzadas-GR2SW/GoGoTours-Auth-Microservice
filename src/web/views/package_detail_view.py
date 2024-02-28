from flask import render_template, request, redirect, url_for, session, flash
from flask.views import MethodView
from injector import inject
from src.application.tourist_packages.services.tourist_packages_service_async import TouristPackagesServiceAsync
from src.application.reserves.services.reserve_service_async import ReservesServiceAsync
from src.application.reserves.dtos.reserves_request_dto import ReservesRequestDto
from src.extensions.decorations_extension import login_required_async


class PackageDetailView(MethodView):

    @inject
    def __init__(self, tourist_packages_service: TouristPackagesServiceAsync, reserves_service: ReservesServiceAsync):
        self._tourist_packages_service = tourist_packages_service
        self._reserves_service = reserves_service

    package = ""

    async def get(self, name):
        package = await self._tourist_packages_service.get_tourist_package_by_name(name)
        return render_template("home/package_detail.html", package=package)

    @login_required_async
    async def post(self, name):
        package = await self._tourist_packages_service.get_tourist_package_by_name(name)
        id_tourist_package = package.id
        id_customer = session.get("id")
        message_dto = ReservesRequestDto(id_tourist_package=id_tourist_package, id_customer=id_customer)
        await self._reserves_service.create_reserve(message_dto)
        return redirect(url_for("home"))
