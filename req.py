import requests
import json
import coloredlogs, logging
import os

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')
coloredlogs.install(level='DEBUG', logger=logger)

url1 = 'https://lo3gdynia.edupage.org/timetable/server/currenttt.js?__func=curentttGetData'
url2 = 'https://lo3gdynia.edupage.org/rpr/server/maindbi.js?__func=mainDBIAccessor'

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
   exit()
try:
   with open(req_opis) as f:
      opisy_j = json.load(f)
except FileNotFoundError:
   logger.critical("Cannot find file named "+ req_opis)
   exit()
logger.info("Requesting for data...")

plan = requests.post(url1, json=plan_j)
opis = requests.post(url2, json=opisy_j)
if(os.path.isfile(req_plan)):
   logger.warning("File named " + req_plan + " exists, overwriting")
with open(res_plan, 'w') as outfile:
    json.dump(plan.json(), outfile)
if(os.path.isfile(req_opis)):
   logger.warning("File named "+ req_opis +" exists, overwriting")
with open(res_opis, 'w') as outfile:
    json.dump(opis.json(), outfile)
logger.info("Sucesfully writed data to json files")