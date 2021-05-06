'''
Johnny Huynh
Dylan P
CST205 
Final Project: Blog/Learning App
'''

#Imports
from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from posts_info import posts_info

#Creating flask instance
app = Flask(__name__)

#Creating bootstrap instance
boostrap = Bootstrap(app)

#Homepage Route
@app.route('/', methods=['GET','POST'])
def home():
    #Return
    return render_template("template.html", imgList=updateList)

#Details Route
@app.route('/details/<pid>')
def details(pid):
    #Open Image
    image = Image.open(f"static/images/{pid}.jpg")
    #All variables that will be sent
   	week=""
    subject=""
    description=""
    details=""
    #Loop and find matching
    for x in posts_info:
        if (x['id'] == pid):
            week = x['week']
            subject = x['subject']
            description = x['description']
            details = x['details']
    #Return
    return render_template("details.html", imgList=posts_info, pid=pid, im=image, wk=week, sub=subject, desc=description, dets=details)


#Run App
if __name__ == "__main__":
    app.run()

