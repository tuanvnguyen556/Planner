from flask import Flask, request, jsonify
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
        return jsonify({'courses':courses})
@app.route("/professor/",methods=['GET'])
def prof():

    save1 = request.args['class']
    save = save1[3:]
    def run():
        response = requests.get("https://api.peterportal.org/rest/v0/grades/raw")
        ist = response.json()
        end = []
        final = []
        for i in ist:
            if i["department"] == "I&C SCI":
                if type(i["averageGPA"]) not in [int,float]:
                    if i["number"] == save:
                        end.append((i["instructor"],i["averageGPA"]))
                elif type(i["averageGPA"]) in [int,float]:
                    if i["number"] == save:
                        final.append((i["instructor"],i["averageGPA"]))
        fin = sorted(final, key=lambda x:x[1])
        for i in end:
            fin.append(i)
        copies = []
        final = []
        for i in range(len(fin)):
            for y in range(len(fin[i])):
                if fin[i][0] not in copies:
                    copies.append(fin[i][0])
                    final.append(fin[i])
        # results = dict((x, y) for x, y in fin)
        return sorted(final,reverse=True)
    return run()
# print(run())

if __name__ == "__main__":
   app.run(host="localhost", port=4000)