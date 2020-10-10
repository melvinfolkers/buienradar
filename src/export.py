import pandas_gbq as gbq
from datetime import datetime


def export_datasets(actuals, forecast):

    export_forecast(forecast)
    export_actuals(actuals)


def export_forecast(df):

    filename = f"forecast_{datetime.now().strftime('%Y%m%d')}"
    gbq.to_gbq(df, f"forecast.{filename}", project_id="buienradar", if_exists="replace")


def export_actuals(df):

    filename = f"actuals_{datetime.now().strftime('%Y%m%d')}"
    gbq.to_gbq(df, f"actuals.{filename}", project_id="buienradar", if_exists="replace")
