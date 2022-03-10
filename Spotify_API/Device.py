import json
from typing import List

import requests

from .Spotify_auth import Spotify_Auth

spotify_token, spotify = Spotify_Auth()


class Device:
    @staticmethod
    def get_devices() -> json:
        """Will return a list of devices connected to the LAN

        Returns:
            json: JSON containing information about the devices
        """
        devices = requests.get(
            "https://api.spotify.com/v1/me/player/devices",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {spotify_token}",
            },
        )

        return devices.json()

    @staticmethod
    def get_id(device_name: str) -> int:
        """Will return an id of specific device

        Args:
            device_name (str): Name of the device you want to get the id.

        Returns:
            int: ID of the device
        """

        for device in Device.get_devices()["devices"]:
            if device["name"] == str(device_name):
                return device["id"]

        return

    @staticmethod
    def get_all_names() -> List[str]:
        """Will return a list of all connected devices

        Returns:
            list: List containing names of the devices
        """
        return [device["name"] for device in Device.get_devices()["devices"]]
