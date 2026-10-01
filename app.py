from flask import Flask,render_template,request
import os
from parser import *
from model import *

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/",methods=["GET","POST"])
def index():

    result=None

    if request.method=="POST":

        file = request.files["resume"]

        path=os.path.join(app.config["UPLOAD_FOLDER"],file.filename)
        file.save(path)

        text = extract_text_from_pdf(path)

        name = extract_name(text)
        email = extract_email(text)
        phone = extract_phone(text)
        skills = extract_skills(text)
        education = extract_education(text)

        job_description = """
        looking for web developer with python html css javascript
        machine learning knowledge
        """

        score = resume_score(text,job_description)

        result={
        "name":name,
        "email":email,
        "phone":phone,
        "skills":skills,
        "education":education,
        "score":score
        }

    return render_template("index.html",result=result)

if __name__=="__main__":
    app.run(debug=True)