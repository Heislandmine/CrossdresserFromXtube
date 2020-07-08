import url_extractor
import client
import time

root_dir = "/mnt/g/data/R_Media/xtube/"
# クライアントの作成
profile_video = client.ClientProfileVideo(root_dir)
for i in range(10):
    urls = profile_video.extractor.extract_urls(profile_video.driver, "https://www.xtube.com/profile/427_yuuri#videos")
    time.sleep()
    print(urls)