#
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
from .models.models import ApplicationType, SongModel

#  ______________________
#


app = FastAPI()


@app.get(path="/")
def root() -> dict[str, str]:
    return {"message": "Hello World"}


@app.get(path="/items/{item_id}")
def get_item_by_id(item_id: int) -> dict[str, int]:
    return {"item_id": item_id}


@app.get(path="/albums/{album_id}")
def get_album(album_id: int) -> dict[str, int]:
    return {"album_id": album_id}


@app.get(path="/users/me")
def get_user() -> dict[str, str]:
    return {"user": "Manny is the the current user"}


@app.get(path="/user/{user_id}")
def get_user_by_id(user_id: str) -> dict[str, str]:
    # def get_user_by_id(user_id: str) -> dict[str, int]:
    # def get_user_by_id(user_id: int) -> dict[str, int]:
    return {"user_id": "The current user id is: {user_id}"}


# ORDER matters
@app.get(path="/users")
def get_users() -> list[str]:
    return ["john", "sandy"]


@app.get(path="/users")
def get_users1() -> list[str]:
    return ["Al", "Sam"]


@app.get(path="/application/{app_type}")
def get_application(app_type: ApplicationType) -> dict[str, ApplicationType]:
    match app_type:
        case ApplicationType.LOAN:
            # Specific logic for loans
            return {"app_type": app_type}
        case ApplicationType.BUSINESS_FINANCING:
            # Specific logic for business
            return {"app_type": app_type}
        case ApplicationType.CAR_FINANCING:
            # Specific logic for car
            return {"app_type": app_type}
        case ApplicationType.HOME_FINANCING:
            # Specific logic for home
            return {"app_type": app_type}
        case _:
            # Wildcard/Default case
            return {"app_type": app_type}


# @app.get(path="/application/{app_type}")
# def get_application(app_type: ApplicationType) -> dict[str, ApplicationType]:
#     print(app_type)
#     if app_type is ApplicationType.LOAN:
#         return {"app_type": app_type}
#     if app_type.value == "business_financing":
#         return {"app_type": app_type}
#     if app_type.value == "car_financing":
#         return {"app_type": app_type}
#     if app_type.value == "home_financing":
#         return {"app_type": app_type}
#     return {"app_type": app_type}


#  QUERY parameters
@app.get(path="/songs")
def get_songs(skip: int = 1, limit: int = 0, page: int = 1, per_page: int = 10) -> dict[str, int]:
    # def get_songs(skip: int, limit: int, page: int, per_page: int) -> dict[str, int]:
    return {"skip": skip, "limit": limit, "page": page, "per_page": per_page}


#  Multiple Query Parameters
# @app.get(path="/playlist/{playlist_id}/songs/{song_id}")
# def get_songs_by_playlist(playlist_id: int, song_id: int) -> dict[str, int]:
#     return {"song_id": song_id, "playlist_id": playlist_id}
@app.get(path="/playlist/{playlist_id}/songs/{song_id}")
def get_songs_by_playlist(playlist_id: int, song_id: int, q: str | None = None) -> dict[str, int | str | None]:
    # def get_songs_by_playlist(playlist_id: int, song_id: int, q: str = "") -> dict[str, int]:
    return {"song_id": song_id, "playlist_id": playlist_id, "q": q}


#  {"title": "I Love You","desc": "Lovers","releasedDate": "2026-02-09","album": "Love Me All the Way"}
@app.post(path="/songs")
def create_song(song: SongModel) -> SongModel:
    return song


# {"title": "I Don't Love You Any More", "desc": "Lovers", "releasedDate": "2026-02-09", "album": "Love Me All the Way"}
@app.put(path="/songs/{song_id}")
def change_song(song: SongModel, song_id: int) -> dict[str, int]:
    return {"song_id": song_id, **song.model_dump()}


#
#  Import LIBRARIES
#  Import FILES
#  ______________________
#
