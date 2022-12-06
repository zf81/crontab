import pandas as pd
import json
import requests
import os
import sys
import time
import crontab

# Found json file about Alzheimer's and healthy aging data
df = pd.read_json('https://chronicdata.cdc.gov/views/hfr9-rurv/rows.json')

# Save df as local csv file
df.to_csv('/Users/fizzahzaidi/Documents/development/python_projects/crontab/data/Alzheimers_Disease_and_Healthy_Aging_Data.csv')

# Show the current time 
now = time.time() 
begintime = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))

# Retrieve current working directory 
cwd = os.getcwd()
# print cwd
print(cwd)

# Create a new file in the current working directory 
with open(cwd + '/Users/fizzahzaidi/Documents/development/python_projects/crontab/healthAlz_' + begintime + '.txt', 'w') as f:
    f.write(str(df))
