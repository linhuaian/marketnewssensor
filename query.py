import os
from datetime import datetime, timezone
import pandas as pd


def query(dataframe):
    """
    Create a the csv if it does not exist in the target folder.
    :param dataframe:
    :return:
    """
    dt = datetime.now().replace(tzinfo=timezone.utc)
    year = dt.strftime('%Y')
    week = dt.strftime("%V")
    file_name = f"news/news_week_{week}_{year}.csv"
    if os.path.exists(file_name):
        #dataframe.to_csv(file_name, mode='a', header=None, index=False)
        pd.concat(pd.read_csv(file_name), dataframe).drop_duplicates(subset=["week", "headline", "news_channel"]).to_csv(file_name)
    else:
        dataframe.to_csv(file_name, index=False)
