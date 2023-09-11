import os
from datetime import datetime, timezone
import pandas as pd


def query(dataframe):
    dt = datetime.now().replace(tzinfo=timezone.utc)
    year = dt.strftime('%Y')
    week = dt.strftime("%V")
    file_name = f"news/news_week_{week}_{year}.csv"
    if os.path.exists(file_name):
        #dataframe.to_csv(file_name, mode='a', header=None, index=False)
        pd.read_csv(file_name).append(dataframe).drop_duplicates(subset=["week", "headline", "news_channel"],
  keep = 'last').to_csv(file_name)
    else:
        dataframe.to_csv(file_name, index=False)
