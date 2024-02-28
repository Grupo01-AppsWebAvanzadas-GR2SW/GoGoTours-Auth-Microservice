from flask import render_template, request, redirect, url_for
from flask.views import MethodView
from injector import inject
from src.application.tourist_packages.services.tourist_packages_service_async import TouristPackagesServiceAsync


class PackageDeleteView(MethodView):
    @inject
    def __init__(self, tourist_packages_service: TouristPackagesServiceAsync):
        self._tourist_packages_service = tourist_packages_service

    async def get(self, name: str):
        await self._tourist_packages_service.delete_package(name)
        return redirect(url_for("home"))


