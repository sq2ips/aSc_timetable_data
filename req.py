import requests
import json
import coloredlogs, logging
import os
from datetime import datetime
from datetime import timedelta

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')
coloredlogs.install(level='DEBUG', logger=logger)

url_plan = 'https://lo3gdynia.edupage.org/timetable/server/currenttt.js?__func=curentttGetData'
url_opis = 'https://lo3gdynia.edupage.org/rpr/server/maindbi.js?__func=mainDBIAccessor'

req_plan='plan_request.json'
req_opis='opis_request.json'
res_plan='plan_respons.json'
res_opis='opis_respons.json'

logger.info("Opening request header files...")
try:
   with open(req_plan) as f:
      plan_j = json.load(f)
except FileNotFoundError:
   logger.critical("Cannot find file named "+ req_plan)
   exit(13)
try:
   with open(req_opis) as f:
      opisy_j = json.load(f)
except FileNotFoundError:
   logger.critical("Cannot find file named "+ req_opis)
   exit(13)
logger.info("Requesting for data...")
x=datetime.now()
#x=datetime(2023, 9, 2)


if(x.strftime('%w') == '0'):
    x=x+timedelta(days=1)
    print("ni")
elif(x.strftime('%w') == '6'):
    print("so")
    x=x+timedelta(days=2)
    
w = x-timedelta(days=x.weekday())

plan_j["__args"][1]['datefrom'] = w.strftime("%Y-%m-%d")
plan_j["__args"][1]['dateto'] = (w+timedelta(days=6)).strftime("%Y-%m-%d")

opisy_j["__args"][2]["vt_filter"]['datefrom'] = w.strftime("%Y-%m-%d")
opisy_j["__args"][2]['dateto'] = (w+timedelta(days=6)).strftime("%Y-%m-%d")

plan = requests.post(url_plan, json=plan_j)
opis = requests.post(url_opis, json=opisy_j)
if(os.path.isfile(req_plan)):
   logger.warning("File named " + req_plan + " exists, overwriting")
with open(res_plan, 'w') as outfile:
    json.dump(plan.json(), outfile)
if(os.path.isfile(req_opis)):
   logger.warning("File named "+ req_opis +" exists, overwriting")
with open(res_opis, 'w') as outfile:
    json.dump(opis.json(), outfile)
logger.info("Sucesfully writed data to json files")