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

    def test_download_video(self, test_url, driver):
        self.downloader.download_video(test_url, driver)


if __name__ == "__main__":
    tester = TestXtubeDownloader(test_url, downloader)
    tester.test_download_video(test_url, client.driver)
