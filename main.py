from src.log import set_logging
from src import buienradar
import logging
from datetime import datetime

def run():

    actuals, forecast = buienradar.get_data()


if __name__ == "__main__":
    set_logging()
    logging.info(f"started script at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    run()
