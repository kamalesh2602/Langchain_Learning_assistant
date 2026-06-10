from pydantic import BaseModel

class Route(BaseModel):
    action :str
    topic : str | None= None