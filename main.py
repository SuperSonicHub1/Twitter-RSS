from twitscrape import twitterToRSS # Returns RSS feed
from flask import Flask, send_from_directory # Web app framework
import schedule  # Schedule clearing of cache
import os # for retrieving favicon

app = Flask('') # Init app

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return "Greetings user! Welcome to my basic Twitter RSS feed! In order to use it, just enter the name of the account that you want to follow, without the '@'."

@app.route('/<username>/')
def returnRSS(username):
    return twitterToRSS(username)

twitterToRSS.cache_clear() # Clears cache every server reboot.

while True:
    app.run(host='0.0.0.0',port=8080)
    
    # Clear RSS cache every 10 minutes
    schedule.every(5).to(10).minutes.do(twitterToRSS().cache_clear())
    schedule.run_pending()