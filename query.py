import os
from datetime import datetime, timezone
import pandas as pd
from config import output_columns


def query(dataframe):
    """
    Create the csv if it does not exist in the target folder.
    :param dataframe:
    :return:
    """
    dt = datetime.now().replace(tzinfo=timezone.utc)
    year = dt.strftime('%Y')
    week = dt.strftime("%V")
    file_name = f"news/news_week_{week}_{year}.csv"
    if os.path.exists(file_name):
        # dataframe.to_csv(file_name, mode='a', header=None, index=False)
        new_dataframe = pd.concat([pd.read_csv(file_name, usecols=output_columns), dataframe], ignore_index=True)
        unique_dataframe = new_dataframe.drop_duplicates(subset=["week", "headline", "news_channel"], keep="first")
        unique_dataframe.to_csv(file_name, index=False)
        # Read file and drop duplicates one more time to enhance duplicate drop
        pd.read_csv(file_name, usecold=output_columns).drop_duplicates(subset=["week", "headline", "news_channel"],
                                                                       keep="first").to_csv(file_name)
    else:
        dataframe.to_csv(file_name, index=False)
