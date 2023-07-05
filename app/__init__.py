import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Prairie Dogs - Nimra & Joni's portfolio", url=os.getenv("URL"))


@app.route('/hobby')
def hobby():
    return render_template('hobby.html', hobbies=[
        {
            "name": "Board Games",
            "img": "./static/img/hobby-1.jpg"
        },
        {
            "name": "Hiking",
            "img": "./static/img/hobby-2.jpg"
        }
    ])


@app.route('/experience')
def experience():
    return render_template('experience.html', work_experiences=[
        {
            "company": "Meta",
            "title": "Software Engineer Intern",
            "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl vitae aliquam ultricies, nunc nisl ultricies nunc, vitae aliquam elit nisl vitae elit. Donec euismod, nisl vitae aliquam ultricies, nunc nisl ultricies nunc, vitae aliquam elit nisl vitae elit.",
            "date": "2023.06 - Present",
            "url": "https://www.google.com/",
        },
        {
            "company": "Apple",
            "title": "Software Engineer Intern",
            "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl vitae aliquam ultricies, nunc nisl ultricies nunc, vitae aliquam elit nisl vitae elit. Donec euismod, nisl vitae aliquam ultricies, nunc nisl ultricies nunc, vitae aliquam elit nisl vitae elit.",
            "date": "2021.06 - 2023.05",
            "url": "https://www.google.com/",
        }
    ], education=[
        {
            "school": "ABC College",
            "url": "https://www.google.com/",
            "date": "2019 - 2023",
            "major": "Computer Science",
            "gpa": "4.0/4.0",
            "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl vitae aliquam ultricies, nunc nisl ultricies nunc, vitae aliquam elit nisl vitae elit. Donec euismod, nisl vitae aliquam ultricies, nunc nisl ultricies nunc, vitae aliquam elit nisl vitae elit.",
        },
        {
            "school": "AIT-Budapest",
            "url": "https://www.google.com/",
            "date": "2022",
            "major": "Computer Science",
            "gpa": "4.0/4.0",
            "desc": "Study Abroad Program",
        },
    ])


@app.route('/map')
def map():
    return render_template('map.html')
