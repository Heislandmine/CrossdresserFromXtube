from selenium import webdriver
from url_extractor import Akicompany, ProfileVideo
from downloader import XtubeDownloader
import os.path


class Client:
    def __init__(self, driver, extractor, downlader, logger):
        self.driver = driver
        self.extractor = extractor
        self.downlader = downlader
        self.logger = logger

    def _get_visited_urls(self):
        if os.path.exists("visited_list.txt"):
            with open("visited_list.txt", "r") as f:
                url_list = f.readlines()
            url_list = [x.strip() for x in url_list]
        else:
            url_list = []

        return url_list

    def _write_visited_url(self, url):
        with open("url_list.txt", "a") as f:
            print(url, file=f)

    def _set_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        # Selenium Server に接続する
        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities=options.to_capabilities(),
            options=options,
        )
        return driver

    def _isVisited(self, url):
        visited_urls = self._get_visited_urls()
        return url in visited_urls


class ClientProfileVideo(Client):
    def __init__(self, root_dir):
        super().__init__(root_dir)

    def _set_extractor(self):
        return ProfileVideo()
