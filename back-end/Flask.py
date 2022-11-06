from flask import Flask, request  
import requests  
app = Flask(__name__)

url_course = "https://api.peterportal.org/rest/v0/courses/all"
url_prof = "https://api.peterportal.org/rest/v0/grades/raw"
first_response = requests.get(url_course)
second_response = requests.get(url_prof)
courses = []
profs = []

for i in first_response.json():
    if i["department"] in ["I&C SCI"]:
        courses.append("ICS"+i["number"])


@app.route("/",methods = ['GET'])
def home():
    if request.method == 'GET':
        return courses

if __name__ == "__main__":
    app.run(host='localhost', port=4000)
