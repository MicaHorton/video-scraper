import requests
headers = {
    'Accept':'*/*',
    'Connection':'keep-alive',
    'Host':'shockwave.streamvid.co',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15',
    'Accept-Language':'en-us',
    'Referer':'https://streamvid.co/player/VaEGru3xugMvZHa/',
    'Accept-Encoding':'idenity'
}

response = requests.get('https://haystack.streamvid.co/tsfiles/BBBIHABE/1080K/2018/HEICAIAC/05/CFHBFGBA/08/FBBEAIAI/37991-002.ts',headers=headers)

with open('newfile.ts','wb') as f:
    f.write(response.content)

'''
curl 'https://haystack.streamvid.co/tsfiles/BBBIHABE/1080K/2018/HEICAIAC/05/CFHBFGBA/08/FBBEAIAI/37991-002.ts' \
-XGET \
-H 'Cookie: _gid=GA1.2.1256074209.1584503718; __cfduid=de84d80f57ba3e75972d368a744f438b71584503714; _ga=GA1.2.1659290744.1584503718' \
-H 'Accept: */*' \
-H 'Connection: keep-alive' \
-H 'Host: haystack.streamvid.co' \
-H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15' \
-H 'Accept-Language: en-us' \
-H 'Referer: https://streamvid.co/player/VaEGru3xugMvZHa/' \
-H 'Accept-Encoding: identity' \
-H 'X-Playback-Session-Id: BCE1DA80-CDC4-49E0-B9BD-5064136B55A3'
'''