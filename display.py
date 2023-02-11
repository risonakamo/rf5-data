from pandas import DataFrame

from typing import List
from data_types import FarmItem3

def dataframeDisplay(data:List[FarmItem3])->None:
    """do dataframe display"""

    df:DataFrame=DataFrame.from_records([
        x.dict()
        for x in data
    ])

    df=df[["name","lv","currentProfitPerDay"]]
    df=df.sort_values("currentProfitPerDay",ascending=False)

    print(df)