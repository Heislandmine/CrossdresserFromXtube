from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
import tempfile
import os.path

# 設定
root_dir = "/mnt/g/data/R_Media/xtube/"  # todo: config fileから読むようにする
depth = 5 # 起動オプションで指定できるようにする

# seleniumの設定 # todo: 外だし

# Chrome のオプションを設定する
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# Selenium Server に接続する
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=options.to_capabilities(),
    options=options,
)


for i in range(depth):
    urls = []
    pagenation = "/p=" + str(i + 1) + "&o=n"
    # Xtube日本人女装子動画からurlを抽出
    html = get("http://xtube.akicompany.com/" + pagenation).text
    html = BeautifulSoup(html)

    target = html.find_all("div", class_="card-body")

    [urls.append(x.a.get("href")) for x in target if "PR" not in x.a.text] # 広告を除外
    print(len(urls))

    # 抽出したurlから動画を保存

    for url in urls:
        print(url)
        with open("url_list.txt", "r") as f:
            url_list = f.readlines()
            url_list = [x.strip() for x in url_list]
        if url in url_list:
            continue
        driver.get(url)
        html = BeautifulSoup(driver.page_source, 'html.parser')
        # 投稿者の名前を取得
        user_info = html.find("a", class_="profileUsername nickname js-pop")
        user_name = user_info.text.strip()
        # 動画のダウンロード
        source = html.find("source", type="video/mp4")
        if not source:
            continue
        video_url = source.get("src")
        res = get(video_url)
        _, tmp = tempfile.mkstemp(suffix=".mp4")
        save_dir = root_dir + user_name
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        file_name = save_dir + "/" + os.path.basename(tmp)
        with open(file_name, "wb") as fo:
            fo.write(res.content)
        with open("url_list.txt", "a") as f:
            print(url, file=f)
driver.quit()
