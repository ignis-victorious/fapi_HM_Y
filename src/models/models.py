#
#  Import LIBRARIES
from enum import Enum

#  Import FILES
#  ______________________
#


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
