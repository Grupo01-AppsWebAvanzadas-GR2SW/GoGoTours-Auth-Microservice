from flask import render_template, request, redirect, url_for, flash
from datetime import datetime
from flask.views import MethodView
from injector import inject
from src.application.tourist_packages.services.tourist_packages_service_async import TouristPackagesServiceAsync
from src.application.tourist_packages.dtos.tourist_packages_response_dto import TouristPackagesResponseDto


class HomeView(MethodView):

    @inject
    def __init__(self, tourist_packages_service: TouristPackagesServiceAsync):
        self._tourist_packages_service = tourist_packages_service

    async def get(self):
        packages = await self._tourist_packages_service.get_tourist_packages()

        return render_template("home/home.html", packages=packages)
