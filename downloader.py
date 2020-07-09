import os
import os.path
import tempfile
from requests import get
from bs4 import BeautifulSoup


class FailedGetVideoPageError(Exception):
    pass


class XtubeDownloader:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def download_video(self, url, driver):
        html = self._get_html(driver, url)
        # 投稿者の名前を取得
        user_name = self._get_user_name(html)
        # 動画のダウンロード
        video_url = self._get_video_url(html)
        self._print_start_download(url)
        res = get(video_url)
        save_path = self.get_save_path(user_name)
        self._save_video(save_path, res.content)
        self._print_end_download(url)

    def _get_user_name(self, html):
        user_info = html.find("a", class_="profileUsername nickname js-pop")
        user_name = user_info.text.strip()

        return user_name

    def _get_html(driver, url):
        driver.get(url)
        html = BeautifulSoup(driver.page_source, 'html.parser')

        if not html:
            raise FailedGetVideoPageError("failed to get video page")

        return html

    def _get_video_url(html):
        source = html.find("source", type="video/mp4")
        video_url = source.get("src")
        return video_url

    def _get_file_name(self):
        _, tmp = tempfile.mkstemp(suffix=".mp4")
        file_name = os.path.basename(tmp)
        return file_name

    def _get_save_dir(self, user_name):
        file_name = self._get_file_name()
        save_dir = self.root_dir + user_name

        return save_dir

    def _get_save_path(self, save_dir, file_name):
        save_path = save_dir + "/" + file_name

        return save_path

    def get_save_path(self, user_name):
        file_name = self._get_file_name()
        save_dir = self._get_save_dir(user_name)
        save_path = self._get_save_path(save_dir, file_name)
        
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)

        return save_path

    def _save_video(self, save_path, video):
        with open(save_path, "wb") as fo:
            fo.write(video)

    def _save_visited_list(self):
        with open("url_list.txt", "a") as f: # このクラスで処理するのが適正か？？？
            print(url, file=f)

    def _print_start_download(self, url):
            print("ダウンロード開始:{}".format(url))

    def _print_end_download(self, url):
            print("ダウンロード完了:{}".format(url))