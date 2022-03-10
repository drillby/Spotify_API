# Spotify_API:

Author: Pavel Podrazký

Small pakage that can be used to operate Spotify.
Some function may require premium account.

## Setup

To be able to comunicate with Spotify API you need to create developer account and create credentials.

### Creating credentials

First you need to visit <a href="https://developer.spotify.com/dashboard/login">this</a> website and setup developer account.

Than you need to provide your credentials to create config file.

```python
from Spotify_API.Spotify_auth import create_credentials

create_credentials()
# Follow intructions in console
```

## Album

Class type object for searching and playing albums

### search

Will search for an album

    Args:
        album_name (str): name of album to search

    Returns:
        SimpleAlbumPaging: information about the search result

```python
from Spotify_API.Album import Album

Album.search(album_name)
```

### play

Will play an album

    Args:
        album_name (str): Name of the album to play
        device (str): Name of the device you want to play on.

    Raises:
        ValueError: if the album name is less than 1 character long

    Returns:
        None: None

```python
from Spotify_API.Album import Album

Album.search(album_name, device)
# You can find the device name in the Spotify app
# Also you need to be on the same LAN
```

## Track

Class type object for searching and playing tracks

### search

Will search for track

    Args:
        album_name (str): name of track to search

    Returns:
        FullTrack: information about the search result

```python
from Spotify_API.Track import Track

Track.search(track_name)
```

### play

Will play an track

    Args:
        album_name (str): Name of the track to play
        device (str): Name of the device you want to play on.

    Raises:
        ValueError: if the album name is less than 1 character long

    Returns:
        None: None

```python
from Spotify_API.Track import Track

Track.search(track_name, device)
# You can find the device name in the Spotify app
# Also you need to be on the same LAN
```

### shuffle

Will shuffle upcomming tracks

    Args:
        shuffle (bool, optional):
        True = shuffle, False = don't shuffle. Defaults to True.

```python
from Spotify_API.Track import Track

Track.shuffle()
```

### add_to_queue

Will add a song to the queue

    Args:
        track_name (str): Name of the track to add to the queue.

## Artist

Class type object for searching and playing artist

### search

Will search for artist

    Args:
        artist_name (str): name of artist to search

    Returns:
        FullArtist: artist information

```python
from Spotify_API.Artist import Artist

Artist.search(artist_name)
```

### play

Will play an artist

    Args:
        artist_name (str): Name of the track to play
        device (str): Name of the device you want to play on.

    Raises:
        ValueError: if the album name is less than 1 character long

    Returns:
        None: None

```python
from Spotify_API.Artist import Artist

Artist.play(artist_name, device)
# You can find the device name in the Spotify app
# Also you need to be on the same LAN
```

## Playlist

Class type object for searching and playing playlist

### search

Will search the playlist

    Args:
        playlist_name (str): Name of the playlist you want to search

    Returns:
        SimplePlaylist: info about the playlist

```python
from Spotify_API.Playlist import Playlist

Artist.search(playlist_name)
# you need to have this playlist saved in your library
```

### play

Will play a playlist

    Args:
        playlist_name (str): name of the playlist you want to play
        device (str, optional): name of the device you wan tot play on.

    Raises:
        ValueError: if the playlist name is less than 1 character long

    Returns:
            None

```python
from Spotify_API.Playlist import Playlist

Artist.play(playlist_name, device)
# You can find the device name in the Spotify app
# Also you need to be on the same LAN
```

## CurrentTrack

Class type object for getting info about current track

### get_track_info

Will return the currently playing track json

    Returns:
        json: JSON containing the currently playing track information

```python
from Spotify_API.CurrentTrack import CurrentTrack

CurrentTrack.get_track_info()
```

### get_name_and_cover

Will return the name and cover of the currently playing track

    Returns:
        tuple: (name of the currently playing track, cover of the currently playing track)

```python
from Spotify_API.CurrentTrack import CurrentTrack

CurrentTrack.get_name_and_cover()
```

### add_recomended_to_queue

Will add recommended song to the queue

    Args:
        device (str): Name of the device you want to add songs to queue to. Defaults to "MYPC".
        num_of_songs (int, optional): Number of devices you want to add to queue. Defaults to 20. min=0, max=100

```python
from Spotify_API.CurrentTrack import CurrentTrack

CurrentTrack.add_recomended_to_queue(device, num_of_songs)
```

## Device

Class type object for getting info about devices that can be used for playback on LAN

### get_devices

Will return a list of devices connected to the LAN

    Returns:
        json: JSON containing information about the devices

```python
from Spotify_API.Device import Device

Device.get_devices()
```

### get_id

Will return an id of specific device

    Args:
        device_name (str): Name of the device you want to get the id.

    Returns:
        int: ID of the device

```python
from Spotify_API.Device import Device

Device.get_id(device_name)
# You can find the device name in the Spotify app
# Also you need to be on the same LAN
```

### get_all_names

Will return a list of all connected devices

    Returns:
        list: List containing names of the devices

```python
from Spotify_API.Device import Device

Device.get_all_names()
```

## ActiveDevice

Class type object for getting info about currently active device.
Only class in this module that needs to be initialized.

### init

When ActiveDevice is initialized it will try to get information about active device from Spotify API, if unsuccessful it will set ActiveDevice.name = "None".
If you will provide name that is not recognised by Spotify, it won't provide any further results

### update_active_device

Will update active device

    Returns:
        None

```python
from Spotify_API.ActiveDevice import ActiveDevice

ad = ActiveDevice()
ad.update_active_device(new_name)
```

You could make API call to get active device, but it is unnecessary call, when you can store localy, where you are playing.

### get_active_device

Will return active device

    Returns:
        str: Active device name

```python
from Spotify_API.ActiveDevice import ActiveDevice

ad = ActiveDevice()
ad.get_active_device()
```

This function will return name of active device stored in object ActiveDevice.

### get_volume

Will return volume of an active device.

    Args:
        device_name (str, optional): Name of the device you want to get volume from. Defaults to "MYPC".

    Returns:
        int: Persentage volume

```python
from Spotify_API.ActiveDevice import ActiveDevice

ad = ActiveDevice(name_recognized_by_Spotify)
ad.get_volume()
```

### change_volume

Will change the volume on active device

    Args:
        volume (int): Defired volume of the device

    if volume not in range(0, 101):
        raise ValueError("Volume must be between 0 and 100")

```python
from Spotify_API.ActiveDevice import ActiveDevice

ad = ActiveDevice(name_recognized_by_Spotify)
ad.change_volume(volume_percentage)
```
