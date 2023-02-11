from pydantic import parse_obj_as
from yaml import safe_load
from pprint import pprint

from rf5_data.types.field_types import FieldData,TotalFieldData,FieldUsage
from typing import List

def main():
    data:List[FieldData]=[]
    with open("field-data.yml") as rfile:
        data=parse_obj_as(List[FieldData],safe_load(rfile))

    totaldata:TotalFieldData=calcTotalFieldData(data)

    pprint(totaldata.dict())

def calcTotalFieldData(fields:List[FieldData])->TotalFieldData:
    """compute total field data from fields"""

    # total amount of space available across all fields
    alltotalSpace:int=0

    # total amount of space used by all fields
    totalUse:float=0

    # dict that will contain combined usages of fields
    usages:FieldUsage={}

    # compute total usages
    for afield in fields:
        afield:FieldData

        alltotalSpace+=afield.totalSpace

        for itemName,itemUse in afield.usages.items():
            itemName:str
            itemUse:float

            usages[itemName]=usages.get(itemName,0)+itemUse

            totalUse+=itemUse

    # convert usages into percents
    for item,usage in usages.items():
        item:str
        usage:float

        usages[item]=usage/alltotalSpace

    totalSpacePercent:float=totalUse/alltotalSpace
    emptySpace:float=1-totalSpacePercent

    return TotalFieldData(
        fields=fields,
        totalSpaceUsage=totalSpacePercent,
        emptySpace=emptySpace,
        totalUsages=usages
    )

if __name__=="__main__":
    main()