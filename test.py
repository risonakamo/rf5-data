from yaml import safe_load
from pprint import pprint
from pydantic import BaseModel,parse_obj_as
from pandas import DataFrame

from typing import List,Dict

class FarmItem(BaseModel):
    # item name
    name:str

    # current attained level of the item
    lv:int

    # price to produce item
    buy:float

    # time to grow item
    growTime:float

    # sell price for 1 item
    sell:float

    # amount of items produced
    growQuant:float

    # seasons item is good in
    goodSeasons:List[str]

    # does this item regrow or not
    regrow:bool

class FarmItem2(FarmItem):
    # total amount of sale (sell price * grow quantity)
    totalSale:float

    # actual profit (total sale - buy price)
    profit:float
    # profit per day (profit / grow time)
    profitPerDay:float

    # time to grow when in season (grow time * 1.5)
    fastGrowTime:float
    # profit per day when in season (profit / fast grow time)
    fastProfitPerDay:float

class FarmItem3(FarmItem2):
    # the current active profit per day of this item, based on the current season
    currentProfitPerDay:float

def main():
    data:List[FarmItem]=[]

    with open("rf5-farm-data.yml","r",encoding="utf-8") as rfile:
        data=parse_obj_as(List[FarmItem],safe_load(rfile))

    data2:List[FarmItem2]=[
        upgradeFarmItem(x)
        for x in data
    ]

    dataframeDisplay(data2)

def upgradeFarmItem(farmitem:FarmItem)->FarmItem2:
    """calculate farm item 2 values"""

    totalSale:float=farmitem.sell*farmitem.growQuant
    profit:float=totalSale-farmitem.buy
    fastGrowTime:float=farmitem.growTime/1.5

    return FarmItem2(
        name=farmitem.name,
        lv=farmitem.lv,
        buy=farmitem.buy,
        growTime=farmitem.growTime,
        sell=farmitem.sell,
        growQuant=farmitem.growQuant,
        goodSeasons=farmitem.goodSeasons,
        regrow=farmitem.regrow,

        totalSale=totalSale,

        profit=profit,
        profitPerDay=profit/farmitem.growTime,

        fastGrowTime=fastGrowTime,
        fastProfitPerDay=profit/fastGrowTime
    )

def dataframeDisplay(data:List[FarmItem2])->None:
    """do dataframe display"""

    print(DataFrame.from_records([
        x.dict()
        for x in data
    ]))

if __name__=="__main__":
    main()