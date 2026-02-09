#
#  Import LIBRARIES

from fastapi import FastAPI

#  Import FILES
from .routers.tracks import tracks_router

#  ______________________
#


app = FastAPI()
app.include_router(router=tracks_router)


@app.get(path="/")
def root() -> dict[str, str]:
    return {"message": "Hello World"}


#  Import LIBRARIES
#  Import FILES
#  ______________________
#
