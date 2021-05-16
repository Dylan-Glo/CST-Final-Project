'''
Johnny Huynh
Dylan Ignacio
CST205 
Final Project: Blog/Learning App
'''

#Imports
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from posts_info import posts_info
from PIL import Image

#Creating flask instance
app = Flask(__name__)

#Creating bootstrap instance
boostrap = Bootstrap(app)

#Homepage Route
@app.route('/', methods=['GET','POST'])
def home():
    #Return
    return render_template("template.html", imgList=posts_info)

#Details Route
@app.route('/details/<pid>')
def details(pid):
    #Open Image
    im = Image.open(f"static/images/{pid}.jpg")
    #All variables that will be sent
    wk=""
    sub=""
    desc=""
    dets=""
    #Loop and find matching
    for x in posts_info:
        if (x['id'] == pid):
            wk = x['week']
            sub = x['subject']
            desc = x['description']
            dets = x['details']
    #Return
    return render_template("details.html", imgList=posts_info, pid=pid, im=im, wk=wk, sub=sub, desc=desc, dets=dets)


#Run App
if __name__ == "__main__":
    app.run()

