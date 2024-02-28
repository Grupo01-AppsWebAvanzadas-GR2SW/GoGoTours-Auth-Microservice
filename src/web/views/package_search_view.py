from flask import render_template, request, redirect, url_for
from flask.views import MethodView
from injector import inject
from src.application.tourist_packages.services.tourist_packages_service_async import TouristPackagesServiceAsync
from src.application.tourist_packages.dtos.tourist_packages_response_dto import TouristPackagesResponseDto
from src.application.reserves.services.reserve_service_async import ReservesServiceAsync
from src.application.reserves.dtos.reserves_request_dto import ReservesRequestDto


class PackageSearchView(MethodView):

    @inject
    def __init__(self, tourist_packages_service: TouristPackagesServiceAsync):
        self._tourist_packages_service = tourist_packages_service

    async def get(self):
        search_term = request.args.get("destination_place", default="", type=str)
        packages = await self._tourist_packages_service.get_tourist_packages()

        filtered_packages = list(filter(
            lambda package: search_term.lower().replace(" ", "") in package.destination_place.lower().replace(" ", ""),
            packages))
        print(filtered_packages)

        return render_template("home/package_search.html", packages=filtered_packages)
