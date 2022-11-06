from flask import Flask, request
import requests
import json
app = Flask(__name__)

url_course = "https://api.peterportal.org/rest/v0/courses/all"
url_prof = "https://api.peterportal.org/rest/v0/grades/raw"
first_response = requests.get(url_course)
second_response = requests.get(url_prof)
courses = []
profs = []
DEPARTMENT = "I&C SCI"
for i in first_response.json():
    if i["department"] == DEPARTMENT:
        courses.append("ICS"+i["number"])


@app.route("/",methods = ['GET'])
def course():
    if request.method == 'GET':
        return {'courses':courses}

@app.route("/professor/",methods=['GET'])
def prof():

    save = request.data
    return save
    def run():
        response = requests.get("https://api.peterportal.org/rest/v0/grades/raw")
        ist = response.json()
        end = []
        final = []
        for i in ist:
            if i["department"] == "I&C SCI":
                if type(i["averageGPA"]) not in [int,float]:
                    if i["number"] == save:
                        end.append((i["instructor"],i["averageGPA"], i["number"]))
                elif type(i["averageGPA"]) in [int,float]:
                    if i["number"] == save:
                        final.append((i["instructor"],i["averageGPA"], i["number"]))
        fin = sorted(final, key=lambda x:x[1])
        for i in end:
            fin.append(i)
        # results = dict((x, y) for x, y in fin)
        return fin
    return run()
# print(run())

if __name__ == "__main__":
   app.run(host="localhost", port=4000)