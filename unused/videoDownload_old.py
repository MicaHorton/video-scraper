


toDownload = 'https://streamvid.co/player/3KEfyw2brPuwLrH/'

# Get m3u8 link
from selenium import webdriver
driver = webdriver.Safari()
driver.get(toDownload)

video_m3u8 = driver.find_element_by_tag_name('video').get_attribute('src')
final_m3u8 = video_m3u8.replace('video.m3u8','1080.m3u8')

driver.close()

# Get m3u8 file
import requests
headers = {
    'Accept':'*/*',
    'Connection':'keep-alive',
    'Host':'shockwave.streamvid.co',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15',
    'Accept-Language':'en-us',
    'Referer': toDownload,
    'Accept-Encoding':'gzip'
}

playlist = requests.get(final_m3u8, headers=headers).content.decode('utf-8').split()

# Extract .ts links
tslinks = []
for line in playlist:
    if not line.lstrip().startswith('#'):
        tslinks.append('https://shockwave.streamvid.co'+line)

print(tslinks)

# Download .ts files
headers['Accept-Encoding'] = 'idenity'
import time

import os
show_name = 'Riverdale'
parent_dir = '/Users/mica/Movies/'
path = os.path.join(parent_dir, show_name)
os.mkdir(path)

counter = 0
for link in tslinks:
    time.sleep(5)
    tsfile = requests.get(link, headers=headers)

    counter +=1
    file_name = str(counter)
    filePath = path + '/' + file_name

    with open(filePath,'wb') as f:
        f.write(tsfile.content)

    


'''