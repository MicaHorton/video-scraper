# Get .m3u8 file (works for all of them, thank god)
import requests
headers = {
    'Accept':'*/*',
    'Connection':'keep-alive',
    'Host':'shockwave.streamvid.co',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15',
    'Accept-Language':'en-us',
    'Referer':'https://streamvid.co/player/VaEGru3xugMvZHa/',
    'Accept-Encoding':'gzip'
}

response = requests.get('https://haystack.streamvid.co/WN3EPeMkRSV8y5vMKy0sgP2tbBevnT_Y-E7eoAe90m4HhKfVVuzLO2EbjScs798FDUw3Hyi-M3GVVUbbpL_vvg/C9NCVxOjlv4vjLqEYdzUpzB2QHvY0jXkbJ4A1dMj7J0/video.m3u8', headers=headers)

print(response.content)







'''

curl 'https://haystack.streamvid.co/tsfiles/BBBIHABE/1080K/2018/HEICAIAC/05/CFHBFGBA/08/FBBEAIAI/37991-001.ts' \
-H 'Accept: */*' \
-H 'Connection: keep-alive' \
-H 'Host: haystack.streamvid.co' \
-H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15' \
-H 'Accept-Language: en-us' \
-H 'Referer: https://streamvid.co/player/VaEGru3xugMvZHa/' \
-H 'Accept-Encoding: identity' \

'''