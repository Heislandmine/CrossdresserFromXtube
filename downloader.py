import os
import os.path
import tempfile
from requests import get
from bs4 import BeautifulSoup
class XtubeDownloader:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def download_video(self, url, driver):
        driver.get(url)
        html = BeautifulSoup(driver.page_source, 'html.parser')
        try:
            # 投稿者の名前を取得
            user_name = self._get_user_name(html)
        except AttributeError: # 広告が入り込んだ場合の対応
            with open("skip_urls.txt", "a") as f:
                print("AttributeError:{}".format(url), file=f)

            print("AttributeError:{}".format(url))
            return 
        # 動画のダウンロード
        source = html.find("source", type="video/mp4")
        if source: # 上にtry文を追加したのでいらないかも
            print("ダウンロード開始:{}".format(url))
            video_url = source.get("src")
            res = get(video_url)
            _, tmp = tempfile.mkstemp(suffix=".mp4")
            save_dir = self.root_dir + user_name
            if not os.path.exists(save_dir):
                os.mkdir(save_dir)
            file_name = save_dir + "/" + os.path.basename(tmp)
            with open(file_name, "wb") as fo:
                fo.write(res.content)
            with open("url_list.txt", "a") as f: # このクラスで処理するのが適正か？？？
                print(url, file=f)
            print("ダウンロード完了:{}".format(url))
        else:
            with open("skip_urls.txt", "a") as f:
                print("source取得失敗:{}".format(url), file=f)

            print("source取得失敗:{}".format(url))

    def _get_user_name(self, html):
        user_info = html.find("a", class_="profileUsername nickname js-pop")
        user_name = user_info.text.strip()

        return user_name