''' Displays the weather forecast for three days using the service open-meteo.com
The location is determined by IP through the service ip2location.io
'''

import requests


def direction(degrees: float) -> str:
    '''converts the azimuth to the wind rose'''
    if degrees < 23:
        return "northern"
    elif degrees < 68:
        return "northeast"
    elif degrees < 113:
        return "eastern"
    elif degrees < 158:
        return "south-east"
    elif degrees < 203:
        return "south"
    elif degrees < 248:
        return "southwest"
    elif degrees < 293:
        return "western"
    elif degrees < 338:
        return "northwest"
    else:
        return "northern"


def print_daily_forecast(forecast: dict, i: int):
    print()
    print(('Tomorrow:', 'The day after tomorrow:', 'On the 3rd day:')[i])
    print(f'In the daytime {forecast["temperature_2m_max"][i]}°C,',
          f'at night {forecast["temperature_2m_min"][i]}°C,')
    print(f'Precipitation {forecast["precipitation_sum"][i]} мм,',
          f'with probability {forecast["precipitation_probability_mean"][i]}%')
    print('Wind',
          f'{direction(float(forecast["wind_direction_10m_dominant"][i]))},',
          f'{forecast["wind_speed_10m_max"][i]} м/с')


GEO = 'https://api.ip2location.io/'
ERR_LOC = 'Your location could not be determined'
ERR_MSG = 'There is a cloudless sky over the whole of Spain, and it is raining in Santiago'

print('Weather forecast')

geo_resp = requests.get(GEO)
if not geo_resp.ok:
    print(ERR_LOC)
    exit(1)
geo_json = geo_resp.json()
country = geo_json['country_name']
city    = geo_json['city_name']
lat     = geo_json['latitude']
long    = geo_json['longitude']
tz = 'auto'

METEO = 'https://api.open-meteo.com/v1/forecast'

daily = ('weather_code,'
         'temperature_2m_max,'
         'temperature_2m_min,'
         'precipitation_sum,'
         'precipitation_probability_mean,'
         'wind_speed_10m_max,'
         'wind_direction_10m_dominant')

params = {'latitude': lat,
          'longitude': long,
          'wind_speed_unit': 'ms',
          'timezone': tz,
          'forecast_days': '3',
          'daily': daily}

meteo_resp = requests.get(METEO, params=params)
if not meteo_resp.ok:
    print(ERR_MSG)
    exit(2)
forecast = meteo_resp.json()['daily']
print(f'{country}, {city}')
for i in range(3):
    print_daily_forecast(forecast, i)