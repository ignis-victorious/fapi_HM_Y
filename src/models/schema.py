#
#  Import LIBRARIES

from pydantic import BaseModel

#  Import FILES
#  ______________________
#


class TrackModel(BaseModel):
    id: int
    title: str


class TrackUpdateModel(BaseModel):
    title: str
