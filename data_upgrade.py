from data_types import FarmItem,FarmItem2,FarmItem3

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

def upgradeFarmItem3(item:FarmItem2,currentSeason:str)->FarmItem3:
    """calculate farm item 3 values"""

    currentProfit:float
    if currentSeason in item.goodSeasons:
        currentProfit=item.fastProfitPerDay
    else:
        currentProfit=item.profitPerDay

    return FarmItem3(
        name=item.name,
        lv=item.lv,
        buy=item.buy,
        growTime=item.growTime,
        sell=item.sell,
        growQuant=item.growQuant,
        goodSeasons=item.goodSeasons,
        regrow=item.regrow,
        totalSale=item.totalSale,
        profit=item.profit,
        profitPerDay=item.profitPerDay,
        fastGrowTime=item.fastGrowTime,
        fastProfitPerDay=item.fastProfitPerDay,

        currentProfitPerDay=currentProfit
    )