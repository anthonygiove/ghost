import re
import pandas as pd
import numpy as np

# df = pd.read_html('https://www.capfriendly.com/teams/redwings/cap-tracker/2019')
# print(df)

import requests
url = 'https://www.capfriendly.com/teams/redwings/cap-tracker/2019'

r = requests.get(url)

print (r.content)