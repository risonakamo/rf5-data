from rf5_data.types.data_types import FarmItem,FarmItem2,FarmItem3

def upgradeFarmItem(farmitem:FarmItem)->FarmItem2:
    """calculate farm item 2 values"""

    totalSale:float=farmitem.sell*farmitem.growQuant

    profit:float
    if not farmitem.regrow:
        profit=totalSale-farmitem.buy
    else:
        profit=totalSale

    fastGrowTime:float=farmitem.growTime/1.5

    return FarmItem2(
        **farmitem.dict(),

        totalSale=totalSale,

        profit=profit,
        profitPerDay=profit/farmitem.growTime,

        fastGrowTime=fastGrowTime,
        fastProfitPerDay=profit/fastGrowTime
    )

def upgradeFarmItem3(item:FarmItem2,currentSeason:str)->FarmItem3:
    """calculate farm item 3 values"""

    currentProfit:float
    if currentSeason in item.goodSeasons:
        currentProfit=item.fastProfitPerDay
    else:
        currentProfit=item.profitPerDay

    return FarmItem3(
        **item.dict(),

        currentProfitPerDay=currentProfit
    )