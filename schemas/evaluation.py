from pydantic import BaseModel

class Evaluation(BaseModel):
    score : int
    feedback : str
    improvement_area : str