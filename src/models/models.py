#
#  Import LIBRARIES
from datetime import date
from enum import Enum

from pydantic import BaseModel

#  Import FILES
#  ______________________
#


class SongModel(BaseModel):
    title: str
    desc: str
    releasedDate: date
    album: str | None = None  # Optional property


class ApplicationType(str, Enum):
    LOAN = "loan"
    BUSINESS_FINANCING = "business_financing"
    CAR_FINANCING = "car_financing"
    HOME_FINANCING = "home_financing"


# class AppLicationType(str, Enum):
#     LOAN = "LOAN"
#     BUSINESS_FINANCING = "BUSINESS_FINANCING"
#     CAR_FINANCING = "CAR_FINANCING"
#     HOME_FINANCING = "HOME_FINANCING"
