import client

client = client.Client("/mnt/g/data/R_Media/xtube/")
depth = 10
for i in range(depth):
    urls = client.extractor.extract_urls()
    for url in urls:
        if not client.isVisited(url):
            client.downlader.download_video(url, client.driver)