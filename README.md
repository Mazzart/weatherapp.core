# WEATHER INFORMATION FROM VARIOUS WEBSITES
### MAIN PURPOSE
> The main purpose of this project is to get real and practical 
knowledge in the parsing of weather websites, finding solutions 
during development.
### IDEA
> Combine and present information from different weather websites in 
one place and be able to view and compare them.
### GOALS:
1. Collect information from different weather websites.
2. A simple interface to use the program. 
3. Adding a new resource, feature will not change the implementation of
the main functionality.
4. Possibility of further development of the program.

*RESOURCES:* [AccuWeather](https://www.accuweather.com/),
[Rp5](http://rp5.ua/), [Sinoptik](https://ua.sinoptik.ua)\
*TOOL:* Python3
***
### Installation of weather application:
TODO
### Commands available in the weather application:
* Run the weather application for all providers\
`wfapp`
* Get a list of all providers\
`wfapp providers`
* Get weather information from a specific provider\
`wfapp [provider id]`
* Update cache\
`wfapp --refresh`\
or\
`wfapp [provider id] --refresh`
* Clear cache\
`wfapp clear-cache`
* Save the weather information to the file\
`wfapp save-to-csv [provider id]`
* Customize your location to get weather information\
`wfapp config [provider id]`
* To see the full traceback in the case of error, use --debug command\
`wfapp --debug, wfapp config accu --debug, etc.`
* For setting log level of the program use the following:\
`-v - log messages starting from level INFO`\
`-vv - log messages starting from level DEBUG`