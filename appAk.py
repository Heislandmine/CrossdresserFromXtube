import client

client = client.Client("/mnt/g/data/R_Media/xtube/")
depth = 1
for i in range(depth):
    client.run(depth=i)
