import os
import json
import datetime
from collections import defaultdict
from loggerConfig import log_app


LG_MAIN = log_app('data_processor')
DEP_DEPENDENCY = os.path.join(os.path.dirname(__file__), 'data\\')
day = datetime.date.today()


def data_format():
    with open(DEP_DEPENDENCY + f'final_adsb{day}.json', 'r') as file:
        try:
            data = json.load(file)
            LG_MAIN.info(f"Data loaded from 'final_adsb{day}.json'")
        except json.decoder.JSONDecodeError:
            LG_MAIN.critical(f"Error loading data from 'final_adsb{day}.json'")
        

    unique_flights = defaultdict(dict)


    for flight in data['mil_data']:
        unique_flights[flight.get("hex")] = flight


    with open(DEP_DEPENDENCY + 'output.json', 'w') as data2:
        json.dump(unique_flights, data2, indent=2)


def remove_test1234():
    with open(DEP_DEPENDENCY + 'output.json', 'r') as file:
        data = json.load(file)


    for k, v in list(data.items()):
        try:
            if v['flight'] == 'TEST1234' or v['flight'] == 'GNDTEST ':
                del data[k]
        except KeyError:
            pass


    with open(DEP_DEPENDENCY + 'output.json', 'w') as data2:
        json.dump(data, data2, indent=2)
