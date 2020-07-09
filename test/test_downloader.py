import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from downloader import XtubeDownloader
from client import Client

test_url = "https://www.xtube.com/video-watch/-13-44399651"
client = Client("")
downloader = XtubeDownloader("")
class TestXtubeDownloader:
    def __init__(self, test_url, downloader):
        self.url = test_url
        self.downloader = downloader

    def test_get_html(self, driver):
        html = self.downloader._get_html(driver, self.url)
        return html

    def test_get_user_name(self, html):
        user_name = self.downloader._get_user_name(html)
        return user_name

    def test_get_video_url(self, html):
        video_url = self.downloader._get_video_url(html)
        return video_url

    def test_download_video(self, test_url, driver):
        self.downloader.download_video(test_url, driver)

if __name__ == "__main__":
    tester = TestXtubeDownloader(test_url,downloader)
    html = tester.test_get_html(client.driver)
    print(html)
    user_name = tester.test_get_user_name(html)
    print(user_name)
    video_url = tester.test_get_video_url(html)
    print(video_url)
    tester.test_download_video(test_url, client.driver)
