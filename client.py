from selenium import webdriver
import os.path

class Client:
    def __init__(self):
       self.visited_urls = self._set_visited_urls()
       self.driver = self._set_driver()
       self.extractor = self._set_extractor()
       self.downlader = self._set_downlader()

    def _set_visited_urls(self):
        if os.path.exists("url_list.txt"):
            with open("url_list.txt", "r") as f:
                url_list = f.readlines()
            url_list = [x.strip() for x in url_list]
        else:
            url_list = []

        return url_list

    def _set_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        # Selenium Server に接続する
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=options.to_capabilities(),
            options=options,
        )
        return driver

    def _set_extractor(self):
        pass

    def _set_downlader(self):
        pass
