#  Import LIBRARIES
from fastapi import APIRouter

#  Import FILES
from ..data.tracks_db import tracks
from ..models.models import TrackModel, TrackUpdateModel

#  ______________________
#


tracks_router = APIRouter()


@tracks_router.get(path="/tracks")
async def get_tracks() -> dict[str, list[TrackModel]]:
    return {"tracks": tracks}


# {  "id": 0,  "title": "Title0"}
# {  "id": 1,  "title": "Title1"}
@tracks_router.post(path="/tracks")
def create_track(track: TrackModel) -> dict[str, list[TrackModel]]:
    tracks.append(track)
    return {"tracks": tracks}


@tracks_router.get(path="/tracks/{track_id}")
async def get_tracks_by_id(track_id: int) -> TrackModel | dict[str, str]:
    for track in tracks:
        if track.id == track_id:
            return track

    return {"message": "Could not find track based on your id"}


@tracks_router.delete(path="/tracks/{track_id}")
def delete_track_by_id(track_id: int) -> str:
    for index in range(len(tracks)):
        track: TrackModel = tracks[index]
        if track.id == track_id:
            tracks.pop(index)
            return "Track deleted"
    return "Could not find track based on your id"


@tracks_router.put(path="/tracks/{track_id}")
def update_track_by_id(track_id: int, track_dto: TrackUpdateModel) -> str:  # Data Transfer Object
    for index in range(len(tracks)):
        track: TrackModel = tracks[index]
        if track.id == track_id:
            track.title = track_dto.title
            return "Track Updated"
    return "Could not find track based on your id"


# @tracks_router.get(path="/tracks")
# async def getTracks():
#     return tracks
