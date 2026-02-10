#  Import LIBRARIES
from fastapi import APIRouter, HTTPException, status

#  Import FILES
from ..data.tracks_db import tracks
from ..models.schema import TrackModel, TrackUpdateModel

#  ______________________
#


tracks_router = APIRouter()


@tracks_router.get(path="/tracks")
async def get_tracks() -> dict[str, list[TrackModel]]:
    return {"tracks": tracks}


# {  "id": 0,  "title": "Title0"}
# {  "id": 1,  "title": "Title1"}
@tracks_router.post(path="/tracks", response_model=list[TrackModel])
def create_track(track: TrackModel) -> dict[str, list[TrackModel]]:
    tracks.append(track)
    return {"tracks": tracks}


@tracks_router.get(path="/tracks/{track_id}", response_model=list[TrackModel])
async def get_tracks_by_id(track_id: int) -> TrackModel | dict[str, str]:
    for track in tracks:
        if track.id == track_id:
            return track

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This track does not exist.")
    # return {"message": "Could not find track based on your id"}


@tracks_router.delete(path="/tracks/{track_id}", response_model=str)
def delete_track_by_id(track_id: int) -> str:
    for index in range(len(tracks)):
        track: TrackModel = tracks[index]
        if track.id == track_id:
            tracks.pop(index)
            return "Track deleted"

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This track does not exist.")
    # return "Could not find track based on your id"


@tracks_router.put(path="/tracks/{track_id}", response_model=str)
def update_track_by_id(track_id: int, track_dto: TrackUpdateModel) -> str:  # Data Transfer Object
    for index in range(len(tracks)):
        track: TrackModel = tracks[index]
        if track.id == track_id:
            track.title = track_dto.title
            return "Track Updated"

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This track does not exist.")
    # return "Could not find track based on your id"


# @tracks_router.get(path="/tracks")
# async def getTracks():
#     return tracks
