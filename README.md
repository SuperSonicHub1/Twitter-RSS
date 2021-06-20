# Twitter-RSS
Lightweight Twitter timeline to RSS converter via Flask, rfeed, and twitter-scraper; Feedly compatible.

![Feedly Screenshot](https://github.com/SuperSonicHub1/Twitter-RSS/blob/master/feedly.png?raw=true)

[Try it right now!](https://Twitter-RSS.supersonichub1.repl.co)

Every Twitter-to-RSS feed converter I've used or have heard of is either dead, doesn't support Feedly all that well, or costs money, so I made my own over a few days.

Rfeed really came in clutch with it's extensibility, which allowed me to easily add Webfeeds support. twitter-scraper also allowed me to have image thumbnails by containing all media associated with a Tweet in a dictionary.

## Setup

Clone this repository, install dependencies with Python Poetry, and run the `main.py` within the cloned folder.
```bash
git clone https://github.com/SuperSonicHub1/Twitter-RSS.git
poetry install
python3 main.py
```
Yes, I know, I know, I should name it `app.py` so that's it's compatible with `flask run`, but this was a project originally hosted on Repl.it, and having custom run commands on there can be irritating sometimes, so deal with it or just change the name of one file yourself. Also, if you are actually considering deploying this app, please remove `app.run()` from `main.py` and use a real WSGI server.
