import json
from json.decoder import JSONDecodeError

import requests

from .Device import Device
from .Spotify_auth import Spotify_Auth

spotify_token, spotify = Spotify_Auth()


class CurrentTrack:
    @staticmethod
    def get_track_info() -> json:
        """Will return the currently playing track json

        Returns:
            json: JSON containing the currently playing track information
        """
        # this try/except is necessary when we boot up the server
        # and we don't have a session on Spotify, Flask returns an error
        try:
            track_info = requests.get(
                "https://api.spotify.com/v1/me/player/currently-playing",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {spotify_token}",
                },
            )

        except JSONDecodeError:
            return

        if track_info:
            return track_info.json()
        else:
            return

    @staticmethod
    def get_name_and_cover() -> tuple:
        """Will return the name and cover of the currently playing track

        Returns:
            tuple: (name of the currently playing track, cover of the currently playing track)
        """

        json = CurrentTrack.get_track_info()
        return (json["item"]["name"], json["item"]["album"]["images"][0]["url"])

    @staticmethod
    def get_ids_for_recomendation() -> tuple:
        """Will return the tuple containing the ids recommended songs based on the currently playing

        Returns:
            tuple: IDs of the recommended songs
        """
        artists_id = []
        json = CurrentTrack.get_track_info()
        for i in range(len(json["item"]["artists"])):
            artists_id.append(json["item"]["artists"][i]["id"])

        if len(artists_id) > 5:
            artists_id = [artists_id[i] for i in range(4)]
        # id of artists on track, id of the track
        return (artists_id, [json["item"]["id"]])

    @staticmethod
    def get_uris_recomended_songs(num_of_songs: int = 20) -> list:
        """Will convert the tuple of recommended ids to uris

        Args:
            num_of_songs (int, optional): Number of songs you want to convert. Defaults to 20.

        Raises:
            ValueError: If the number of songs you want to convert is greater than 100

        Returns:
            list: Contains the recommended uris
        """
        # the 100 here is API limit
        if int(num_of_songs) > 100:
            raise ValueError("Number of recommended songs cant be more than 100")

        elif int(num_of_songs) <= 0:
            raise ValueError("Number of recommended songs cant be less than 0")

        artists_ids, song_id = CurrentTrack.get_ids_for_recomendation()
        recom = spotify.recommendations(
            artist_ids=artists_ids, track_ids=song_id, limit=num_of_songs
        ).tracks

        return [recom_song.uri for recom_song in recom]

    @staticmethod
    def add_recomended_to_queue(device: str, num_of_songs: int = 20) -> None:
        """Will add recommended song to the queue

        Args:
            device (str): Name of the device you want to add songs to queue to. Defaults to "MYPC".
            num_of_songs (int, optional): Number of devices you want to add to queue. Defaults to 20. min=0, max=100
        """

        uris = CurrentTrack.get_uris_recomended_songs(num_of_songs)
        device_id = Device.get_id(device)
        for uri in uris:
            spotify.playback_queue_add(uri=uri, device_id=device_id)

        return
