import json
import coloredlogs, logging

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')
coloredlogs.install(level='DEBUG', logger=logger)

data = []
res_plan="plan_respons.json"
res_opis="opis_respons.json"

logger.info("Opening respons header files...")
try:
   with open(res_plan) as f:
      plan_j = json.load(f)
except FileNotFoundError:
   logger.critical("Cannot find file named "+ req_plan)
   exit()
try:
   with open(res_opis) as f:
      opisy_j = json.load(f)
except FileNotFoundError:
   logger.critical("Cannot find file named "+ req_opis)
   exit()
plan_j_data=plan_j["r"]["ttitems"]
for i in range(len(plan_j_data)):
    plan_j_data=plan_j["r"]["ttitems"][i]
    data.append([plan_j_data['date'], plan_j_data["starttime"], plan_j_data["endtime"], plan_j_data["subjectid"], plan_j_data["classids"][0], plan_j_data["groupnames"][0], plan_j_data["teacherids"][0], plan_j_data["classroomids"][0]])

teachers=[]
teachers_n=[]
subjects=[]
subjects_n=[]
classrooms=[]
classrooms_n=[]
opisy_j_data = opisy_j["r"]["tables"][0]["data_rows"]
for i in range(len(opisy_j_data)):
    teachers.append(opisy_j_data[i]["id"])
    teachers_n.append(opisy_j_data[i]["short"])
opisy_j_data = opisy_j["r"]["tables"][1]["data_rows"]
for i in range(len(opisy_j_data)):
    subjects.append(opisy_j_data[i]["id"])
    subjects_n.append(opisy_j_data[i]["name"])
opisy_j_data = opisy_j["r"]["tables"][2]["data_rows"]
for i in range(len(opisy_j_data)):
    classrooms.append(opisy_j_data[i]["id"])
    classrooms_n.append(opisy_j_data[i]["short"])


print(classrooms)