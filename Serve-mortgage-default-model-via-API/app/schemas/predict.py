from typing import Any, List, Optional

from model.processing.validation import MortgageDataInputSchema
from pydantic import BaseModel


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[int]]


class MultipleMortgageDataInputs(BaseModel):
    inputs: List[MortgageDataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "AP001": 30,
                        "AP002": 1,
                        "AP003": 3,
                        "AP004": 12,
                        "AP005": "2017/6/20 16:31",
                        "AP006": "h5",
                        "AP007": 4,
                        "AP008": 4,
                        "AP009": 1,
                        "TD001": 4,
                        "TD002": 0,
                        "TD005": 4,
                        "TD006": 0,
                        "TD009": 9,
                        "TD010": 1,
                        "TD013": 9,
                        "TD014": 1,
                        "TD015": 1,
                        "TD022": 20.0,
                        "TD023": 0.0,
                        "TD024": 16.0,
                        "TD025": 0.0,
                        "TD026": 0.0,
                        "TD027": 0.0,
                        "TD028": 0.0,
                        "TD029": 6.0,
                        "TD055": None,
                        "CR004": 1,
                        "CR005": 1,
                        "CR009": 15000,
                        "CR012": 0,
                        "CR015": 6,
                        "CR017": 8,
                        "CR018": 7,
                        "CR019": 11,
                        "PA022": -1.0,
                        "PA023": -1.0,
                        "PA028": -98.0,
                        "PA029": -98.0,
                        "PA030": -98.0,
                        "PA031": -98.0,
                        "CD008": 7845.0,
                        "CD018": 256.0,
                        "CD071": 71.0,
                        "CD072": 21.0,
                        "CD088": 11.0,
                        "CD100": 0.0,
                        "CD101": 0.0,
                        "CD106": 0.0,
                        "CD107": 0.0,
                        "CD108": 0.0,
                        "CD113": 0.0,
                        "CD114": 0.0,
                        "CD115": 61.0,
                        "CD117": 41.0,
                        "CD118": 100.0,
                        "CD120": 68.0,
                        "CD121": 130.0,
                        "CD123": 88.0,
                        "CD130": 100.0,
                        "CD131": 41.0,
                        "CD132": 47.0,
                        "CD133": 109.0,
                        "CD135": 115.0,
                        "CD136": 47.0,
                        "CD137": 64.0,
                        "CD152": 4016.0,
                        "CD153": 8282.0,
                        "CD160": 7.0,
                        "CD162": 24.0,
                        "CD164": 22.0,
                        "CD166": 477.0,
                        "CD167": 413.0,
                        "CD169": 731.0,
                        "CD170": 640.0,
                        "CD172": 2307.0,
                        "CD173": 2216.0,
                        "MB005": 5.0,
                        "MB007": "WEB",
                    }
                ]
            }
        }
