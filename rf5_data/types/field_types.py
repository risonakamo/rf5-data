from pydantic import BaseModel
from typing import List,Dict

FieldUsage=Dict[str,float]
"""usage information of a field
key: type of item
value: amount of space being used by that item"""

class FieldData(BaseModel):
    """raw field data"""

    name:str
    totalSpace:int
    usages:FieldUsage

class TotalFieldData(BaseModel):
    fields:List[FieldData]

    totalSpaceUsage:float
    """space usage as percent"""

    emptySpace:float
    """empty percent"""

    totalUsages:FieldUsage
    """combined field usages from all fields"""