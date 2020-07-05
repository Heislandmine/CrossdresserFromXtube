from bs4 import BeautifulSoup
from requests import get

class Akicompany:
    def __init__(self):
        self.url = "http://xtube.akicompany.com/"

    def extract_urls(self, depth=1):
        urls = []
        pagenation = "/p=" + str(depth + 1) + "&o=n"
        # Xtube日本人女装子動画からurlを抽出
        html = get(self.url + pagenation).text
        html = BeautifulSoup(html, 'html.parser')

        target = html.find_all("div", class_="card-body")

        [urls.append(x.a.get("href")) for x in target if "PR" not in x.a.text] # 広告を除外
        print(len(urls)) # デバック用

        return urls

class ProfileVideo:
    def __init__(self):
        self.url = "https://www.xtube.com"

    def extract_urls(self, driver, url, depth=1):
        urls = []

        driver.get(url)
        html = BeautifulSoup(driver.page_source, 'html.parser')
        try:
            target_ul = html.find("ul", class_="row rowSpace")
            targets = target_ul.find_all("a", class_="titleRemover")
        except AttributeError: # なぜかhtmlがNoneになる場合があるのでその場合はurlを記録してメソッドを抜ける
            with open("skip_urls.txt", "w") as f:
                print(url, file=f)
            return False
        for target in targets:
            urls.append(self.url + target.get("href"))
        return urls