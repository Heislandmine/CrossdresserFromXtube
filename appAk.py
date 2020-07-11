import client
from downloader import XtubeDownloader
from url_extractor import Akicompany
from driver import Driver
from logger import Logger

downloader = XtubeDownloader("")
extractor = Akicompany()
driver = Driver()
logger = Logger()
client = client.Client(driver.driver, extractor, downloader, logger)
depth = 1
for i in range(depth):
    client.run(depth=i)
