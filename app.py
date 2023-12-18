from flask import Flask, flash, redirect, url_for, render_template, request

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#FIXME: add images and hyperlinks landing page
#TODO: Check grammar of projects.
#TODO: Add images to projects
#TODO: Upload project repositories 
#TODO: About html 

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/about")
def about():
    ...