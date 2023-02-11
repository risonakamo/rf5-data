from yaml import safe_load
from pydantic import parse_obj_as

from rf5_data.data_upgrade import upgradeFarmItem,upgradeFarmItem3
from rf5_data.display import dataframeDisplay

from typing import List
from rf5_data.types.farm_types import FarmItem,FarmItem2,FarmItem3

def main():
    data:List[FarmItem]=[]
    currentSeason:str="summer"

    with open("rf5-farm-data.yml","r",encoding="utf-8") as rfile:
        data=parse_obj_as(List[FarmItem],safe_load(rfile))

    # calculate main values
    data2:List[FarmItem2]=[
        upgradeFarmItem(x)
        for x in data
    ]

    # calculate values with inputs
    data3:List[FarmItem3]=[
        upgradeFarmItem3(x,currentSeason)
        for x in data2
    ]

    dataframeDisplay(data3)

if __name__=="__main__":
    main()