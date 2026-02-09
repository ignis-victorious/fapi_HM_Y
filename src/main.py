#
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
from .models.models import ApplicationType

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


@app.get(path="/songs")
def get_songs(skip: int, limit: int, page: int, per_page: int) -> dict[str, int]:
    return {"skip": skip, "limit": limit, "page": page, "per_page": per_page}


#
#  Import LIBRARIES
#  Import FILES
#  ______________________
#
