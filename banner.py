from bs4 import BeautifulSoup
import requests

def get_banner(user):
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Referer": f"https://twitter.com/{user}",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",
        "X-Twitter-Active-User": "yes",
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Language": "en-US",
    }

    try:
        soup = BeautifulSoup(
            requests.get("https://twitter.com/{user}").text,
            'html.parser'
        )
        return soup.find(class_='ProfileCanopy-headerBg').find('img').get('src')
    except:
        return ''