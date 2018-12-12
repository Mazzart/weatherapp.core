"""Constants for the weather application project."""

DEFAULT_NAME = 'Kyiv'
DEFAULT_URL = {'accu': 'https://www.accuweather.com/en/ua/kyiv/324505/weather-forecast/324505',
               'rp5': 'http://rp5.ua/Weather_in_Kiev,_Kyiv'}
BROWSE_LOCATIONS = {'accu': 'https://www.accuweather.com/en/browse-locations',
                    'rp5': 'http://rp5.ua/Weather_in_the_world'}
CONFIG_FILE = 'weatherapp.ini'
CACHE_DIR = '.weatherappcache'
CACHE_TIME = 900
DAY_IN_SECONDS = 86400