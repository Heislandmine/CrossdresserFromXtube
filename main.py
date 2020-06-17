from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
import tempfile
import os.path
# todo:pagenation 巡回済みurlの管理　投稿者情報の取得と動画の紐づけ
# seleniumの設定

# Chrome のオプションを設定する
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# Selenium Server に接続する
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=options.to_capabilities(),
    options=options,
)

# Xtube日本人女装子動画からurlを抽出
html = get("http://xtube.akicompany.com/").text
html = BeautifulSoup(html)

target = html.find_all("div", class_="card-body")

urls = [x.a.get("href") for x in target if "PR" not in x.a.text] # 広告を除外

# 抽出したurlから動画を保存

for url in urls:
    driver.get(url)
    html = BeautifulSoup(driver.page_source, 'html.parser')
    video_url = html.find("source", type="video/mp4").get("src")
    res = get(video_url)
    _, tmp = tempfile.mkstemp(suffix=".mp4")
    file_name = os.path.basename(tmp)
    with open(file_name, "wb") as fo:
        fo.write(res.content)
driver.quit()
