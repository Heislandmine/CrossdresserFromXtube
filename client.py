from url_extractor import ProfileVideo
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

    def _isVisited(self, url):
        visited_urls = self._get_visited_urls()
        return url in visited_urls

    def run(self, **kwargs):
        urls = self.extractor.extract_urls(
            kwargs["depth"]
        )  # モジュールの違いを吸収するために別メソッドでラッピングすること

        for url in urls:
            self.logger.logging("ダウンロード開始:{}".format(url))
            self.downlader.download_video(url, self.driver)
            self._write_visited_url(url)
            self.logger.logging("ダウンロード完了:{}".format(url))


class ClientProfileVideo(Client):
    def __init__(self, root_dir):
        super().__init__(root_dir)

    def _set_extractor(self):
        return ProfileVideo()
