import pathlib
import url_extractor
import client
# 設定
target_dir = "/mnt/g/data/R_Media/xtube/"
base_url = "https://www.xtube.com/profile/"
root_dir = "test/"
# クライアントの作成
profile_video = client.ClientProfileVideo(root_dir)
# コレクションから女装子IDを取得
p = pathlib.Path(target_dir)
ids = [x.name for x in p.glob("*")]
# メイン処理
for id_ in ids:
    page_url = base_url + id_ + "#videos"
    urls = profile_video.extractor.extract_urls(profile_video.driver, page_url)
    if urls is False:
        continue
    for url in urls:
        if not profile_video.isVisited(url):
            profile_video.downlader.download_video(url,  profile_video.driver)
            