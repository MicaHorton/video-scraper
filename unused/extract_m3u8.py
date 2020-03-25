f = open('1080.m3u8','r')
playlist = f.readlines()

tslinks = []

for line in playlist:
    if not line.lstrip().startswith('#'):
        tslinks.append('https://shockwave.streamvid.co'+line)

print(len(tslinks))
