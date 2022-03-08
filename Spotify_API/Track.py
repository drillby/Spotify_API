import tekore as tk  # https://tekore.readthedocs.io/en/stable/reference/client.html#
from tekore._model.track import FullTrack
from .Device import Device
from .Spotify_auth import Spotify_Auth

spotify_token, spotify = Spotify_Auth()


class Track:
    @staticmethod
    def search(param: str) -> FullTrack:
        """Will search for track

        Args:
            param (str): Name of the track you want to search

        Returns:
            json: JSON containing information about the track
        """
        if len(param) < 1:
            raise ValueError("Name must be at least one character long")

        (tracks,) = spotify.search(
            param,
            types=("track",),
            limit=1,
        )
        track = tracks.items[0]
        return track

    @staticmethod
    def play(track_name: str, device: str) -> None:
        """Will play the specific track

        Args:
            track_name (str): Name of the track you want to play
            device (str, optional): Name of the device to play on. Defaults to "MYPC".

        Raises:
            ValueError: if the track name is less than 1 character long

        Returns:
            None: None
        """

        track = Track.search(track_name)
        device_id = Device.get_id(device)
        spotify.playback_start_tracks([track.id], device_id=device_id, position_ms=0)
        return

    @staticmethod
    def shuffle(boolean: bool = True) -> None:
        """Will shuffle the tracks

        Args:
            boolean (bool, optional): True = shuffle, False = don't shuffle. Defaults to True.
        """

        spotify.playback_shuffle(boolean)

        return

    @staticmethod
    def add_to_queue(track_name: str) -> None:
        """Will add a song to the queue

        Args:
            track_name (str): Name of the track to add to the queue.
        """

        track = Track.search(track_name)
        track_uri = tk.to_uri("track", track.id)
        spotify.playback_queue_add(uri=track_uri)

        return
