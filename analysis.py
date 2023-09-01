import json
import coloredlogs, logging

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)

data = []
res_plan="plan_respons.json"
res_opis="opis_respons.json"

logger.info("Opening respons header files...")
try:
   with open(res_plan) as f:
      plan_j = json.load(f)
except FileNotFoundError:
   logger.critical("Cannot find file named "+ res_plan)
   exit()
try:
   with open(res_opis) as f:
      opisy_j = json.load(f)
except FileNotFoundError:
   logger.critical("Cannot find file named "+ res_opis)
   exit()
   

plan_j_data=plan_j["r"]["ttitems"]
for i in range(len(plan_j_data)):
    plan_j_data=plan_j["r"]["ttitems"][i]
    data.append([plan_j_data['date'], plan_j_data["starttime"], plan_j_data["endtime"], plan_j_data["subjectid"], plan_j_data["classids"][0], plan_j_data["groupnames"][0], plan_j_data["teacherids"][0], plan_j_data["classroomids"][0]])

#   data         start   koniec     nazwa   klasa? ?   nazwisko sala
#['2023-09-04', '07:45', '08:30', '-423', '-233', '', '-262', '-274']
teachers={}
subjects={}
classrooms={}
classes={}
opisy_j_data = opisy_j["r"]["tables"][0]["data_rows"]
for i in range(len(opisy_j_data)):
    teachers[opisy_j_data[i]["id"]]=opisy_j_data[i]["short"]
opisy_j_data = opisy_j["r"]["tables"][1]["data_rows"]
for i in range(len(opisy_j_data)):
    subjects[opisy_j_data[i]["id"]]=opisy_j_data[i]["name"]
opisy_j_data = opisy_j["r"]["tables"][2]["data_rows"]
for i in range(len(opisy_j_data)):
    classrooms[opisy_j_data[i]["id"]] = opisy_j_data[i]["short"]
opisy_j_data = opisy_j["r"]["tables"][3]["data_rows"]
for i in range(len(opisy_j_data)):
    classes[opisy_j_data[i]["id"]] = opisy_j_data[i]["short"]

plan=[]
for i in range (len(data)):
    a = [data[i][0], data[i][1], data[i][2], subjects[data[i][3]], classes[data[i][4]], data[i][5], teachers[data[i][6]], classrooms[data[i][7]]]
    plan.append(a)
print(plan[0])

#print("classrooms: " + str(classrooms))
#print("subjects: " + str(subjects))
#print("teachers: " + str(teachers))