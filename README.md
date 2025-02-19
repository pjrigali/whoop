# whoop
Interacting with Whoop's API

Uses -> [whoop package](https://github.com/hedgertronic/whoop/)

```python
import configparser
from whoop_class import Whoop

config = configparser.ConfigParser()
WHOOP_USERNAME = config["WHOOP"]["WHOOP_USERNAME"]
WHOOP_PASSWORD = config["WHOOP"]["WHOOP_PASSWORD"]
WHOOP_START_DATE = config["WHOOP"]["WHOOP_START_DATE"] # YYYY-MM-DD
WHOOP_END_DATE = None if config["WHOOP"]["WHOOP_END_DATE"] == 'None' else config["WHOOP"]["WHOOP_END_DATE"] # YYYY-MM-DD

wp = Whoop(username=WHOOP_USERNAME, password=WHOOP_PASSWORD, start_date=WHOOP_START_DATE, end_date=WHOOP_END_DATE)
wp.profile
```