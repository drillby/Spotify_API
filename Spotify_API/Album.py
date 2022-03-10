import tekore as tk  # https://tekore.readthedocs.io/en/stable/reference/client.html#
from tekore._model.album import SimpleAlbumPaging

from .Device import Device
from .Spotify_auth import Spotify_Auth

spotify_token, spotify = Spotify_Auth()


class Album:
    @staticmethod
    def search(album_name: str) -> SimpleAlbumPaging:
        """Will search for an album

        Args:
            album_name (str): name of album to search

        Returns:
            json: JSON containing information about the search result
        """
        if len(album_name) < 1:
            raise ValueError("Name must be at least one character long")

        (albums,) = spotify.search(
            str(album_name),
            types=("album",),
            limit=1,
        )

        return albums

    @staticmethod
    def play(album_name: str, device: str) -> None:
        """Will play an album

        Args:
            album_name (str): Name of the album to play
            device (str): Name of the device you want to play on.

        Raises:
            ValueError: if the album name is less than 1 character long

        Returns:
            None: None
        """

        album = Album.search(album_name)
        album_uri = tk.to_uri("album", album.items[0].id)
        device_id = Device.get_id(str(device))
        spotify.playback_start_context(
            context_uri=album_uri, device_id=device_id, position_ms=0
        )
        return
