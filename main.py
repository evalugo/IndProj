from flask import Flask, render_template

app = Flask(__name__)

# Eva, you may want to cinsider making this a PWA once it works like you want(when finished)
# Here is a great tutorial: https://youtu.be/sFsRylCQblw
# Also, here is a tutorial on "modals" https://www.youtube.com/watch?v=TAB_v6yBXIE
#read repl.it database https://docs.replit.com/hosting/database-faq
from replit import db
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notes')
def notes_page():
    #logic to cover the notes
    return render_template('notes.html')
  
@app.route('/calendar')
def calendar_page():
    #logic to cover the calendar
    return render_template('calendar.html')

@app.route('/calendar')
def calendar():
    return render_template("calendar.html")

@app.route('/reminders')
def reminders_page():
    #logic to cover the reminders
    return render_template('reminders.html')

app.run(host='0.0.0.0', port=81)