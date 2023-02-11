from pydantic import BaseModel
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

    # actual profit (total sale - buy price). if the item is regrowing, then the profit
    # is based on 0 buy price (because it has no cost to regrow)
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
    fields:Dict[str,FieldData]
    """all field datas.
    key: field name
    val: the field data"""

    totalSpaceUsage:float
    """space usage as percent"""

    totalUsages:FieldUsage
    """combined field usages from all fields"""