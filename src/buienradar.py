import logging
import requests
import json
import pandas as pd
import timeago
from datetime import datetime


def get_data():
    """

    :return: tuple of 2 dataframes
    :info:
    actuals: Dataset containing the most recent measurements from the weather stations.
    forecast: Dataset contaning the 5-day forecast
    """
    data = request_data()
    actuals = get_actuals(data)
    logging.info(f"dataset updated {timeago.format(actuals.timestamp[0], datetime.now() )}")
    logging.info(f"pulled measurements from {len(actuals)} weather stations")
    forecast = get_forecast(data)
    logging.info(f"pulled {len(forecast)} records for 5-day forecast")

    return actuals, forecast


def request_data():
    """
    :return: json object.
    dataset containing information of weatherstation measurements of Buienradar.
    """
    r = requests.get("https://data.buienradar.nl/2.0/feed/json")
    data = json.loads(r.text)

    return data


def get_actuals(data):
    """
    :param data: json object retrieved from the buienradar API.
    :return: dataframe object containing the current station measurements.
    """

    data = data["actual"]
    stations = data["stationmeasurements"]
    df = pd.DataFrame(stations)

    df["sunrise"] = pd.to_datetime(data["sunrise"])
    df["sunset"] = pd.to_datetime(data["sunset"])
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["id"] = df["stationid"].astype(str) + " - " + df["timestamp"].astype(str)

    df.drop(columns=["$id", "iconurl", "graphUrl"], inplace=True)

    return df


def get_forecast(data):
    """
    :param data: json object retrieved from the buienradar API.
    :return: dataframe object containing the five day forecast data.
    """

    data = data["forecast"]
    df = pd.DataFrame(data["fivedayforecast"])
    df["day"] = pd.to_datetime(df["day"])
    df.drop(columns=["$id", "mintemperature", "maxtemperature", "iconurl"], inplace=True)

    return df
