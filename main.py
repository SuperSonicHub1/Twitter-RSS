from twitscrape import twitterToRSS # Returns RSS feed
from flask import Flask, send_from_directory, render_template, redirect, url_for, request # Web app framework
import schedule  # Schedule clearing of cache
import os # for retrieving favicon

app = Flask('') # Init app

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<username>/')
def returnRSS(username):
    return twitterToRSS(username)

@app.route('/lookup')
def lookup():
    return redirect(url_for('returnRSS', username=request.args.get("q")))

twitterToRSS.cache_clear() # Clears cache every server reboot.

while True:
    app.run(host='0.0.0.0',port=8080)
    
    # Clear RSS cache every 10 minutes
    schedule.every(5).to(10).minutes.do(twitterToRSS().cache_clear())
    schedule.run_pending()