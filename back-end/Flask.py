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
nul = []
DEPARTMENT = "I&C SCI"
for i in first_response.json():
    if i["department"] == DEPARTMENT:
        courses.append("ICS"+i["number"])


@app.route("/",methods = ['GET'])
def course():
    if request.method == 'GET':
        return json.dumps(courses)

@app.route("/professor/",methods=['GET'])
def prof():
    if request.method == 'GET':
        found_course = request.args['class']
        num = found_course.rfind('S')
        course_number = found_course[num + 1:]
        print(first_response)
        return course_number
        for s in second_response.json():
            if (s["number"] == course_number) and (s["department"] == DEPARTMENT):
                if type(s["averageGPA"]) in [int, float]:
                    profs.append((s["instructor"], s["averageGPA"]))
                else:
                    nul.append((s["instructor"], s["averageGPA"]))
        prof_sort = sorted(prof, key=(lambda x: x[1]))
        return prof_sort

if __name__ == "__main__":
    app.run(host='localhost', port=4000)
