import pandas_gbq as gbq
from datetime import datetime
import logging


def export_datasets(actuals, forecast):

    export_forecast(forecast)
    export_actuals(actuals)


def export_forecast(df):

    filename = f"forecast_{datetime.now().strftime('%Y%m%d')}"
    gbq.to_gbq(df, f"forecast.{filename}", project_id="buienradar", if_exists="replace")


def get_current_ids(filename):

    try:
        id_list = gbq.read_gbq(f"SELECT id FROM actuals.{filename}", project_id="buienradar")[
            "id"
        ].to_list()
    except:
        id_list = []

    return id_list


def export_actuals(df):

    filename = "measurements"
    current_ids = get_current_ids(filename)
    df = df[~df.id.isin(current_ids)]

    if len(df):
        logging.info(f"{len(df)} new records.")
        gbq.to_gbq(df, f"actuals.{filename}", project_id="buienradar", if_exists="append")
    else:
        logging.info("records already exist in Google BigQuery")
