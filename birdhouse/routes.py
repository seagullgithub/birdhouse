from flask import render_template
from birdhouse import app
from birdhouse.take_snapshot import take_snapshot

@app.route('/')
@app.route('/index')
def index():
    return render_template('default.html', message='beep beep')

@app.route('/take')
def take():
    snapshot = take_snapshot()
    if snapshot:
        return 'alles roger'
    else:
        return 'nope'
