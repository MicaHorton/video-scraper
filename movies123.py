# GET EPISODE LINKS
def getEpisodePage(name, season):
    from selenium import webdriver
    driver = webdriver.Chrome()

    # Get intro page 
    base = 'https://ww7.123moviesfree.sc/season/{name}-season-{season}/'
    introPage = base.format(name=name,season=season)
    driver.get(introPage)

    # Get episode page
    playButton = driver.find_element_by_xpath('//*[@id="mv-info"]/a') 
    episodePage = (playButton.get_attribute('href'))

    driver.close()
    return episodePage

def getEpisodeLinks(episodePage):
    from selenium import webdriver
    driver = webdriver.Chrome()

    # Get all episodes by data-server attribute, then print (and store) episode name and video URL
    driver.get(episodePage)
    episodeLinks = []

    # Try data-server 1
    episodes = driver.find_elements_by_xpath('//a[@data-server="1"]')
    for item in episodes:
        name = item.get_attribute('innerHTML')
        url = item.get_attribute('data-strvid')
        if url != None: 
            episodeLinks.append({'name':name,'url':url})

    # If not, try data-server 2
    if episodes == []:
        episodes = driver.find_elements_by_xpath('//a[@data-server="10"]')
        for item in episodes:
            name = item.get_attribute('innerHTML')
            url = item.get_attribute('data-drive')
            if url != None: 
                episodeLinks.append({'name':name,'url':url})
    
    # Print episode links
    for item in episodeLinks:
        print('{name:<80} {url:<80}'.format(name=item['name'], url=item['url']).rstrip())

    driver.close()
    return episodeLinks

# DOWNLOAD EPISODES
def selectEpisodes(episodeLinks):
    import re

    print('Download Episodes?')
    userList = re.findall('\d', input()) 
    downloadLinks = []

    for item in episodeLinks: 
        episodeNumber = re.findall('\d', item['name'])
        episodeNumber = ''.join(episodeNumber)

        for number in userList: 
            if episodeNumber == number:
                downloadLinks.append({'number':number,'url':item['url']})

    return downloadLinks

def getFileLinks(episode):
    from selenium import webdriver
    driver = webdriver.Safari()
    import requests

    # Get 1080.m3u8 
    driver.get(episode)
    video_m3u8 = driver.find_element_by_tag_name('video').get_attribute('src')
    final_m3u8 = video_m3u8.replace('video.m3u8','1080.m3u8')

    driver.close()

    # Get m3u8 file
    global headers
    headers = {
        'Accept':'*/*',
        'Connection':'keep-alive',
        'Host':'shockwave.streamvid.co',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15',
        'Accept-Language':'en-us',
        'Referer': episode,
        'Accept-Encoding':'gzip'
    }
    playlist = requests.get(final_m3u8, headers=headers).content.decode('utf-8').split()

    # Extract .ts links
    tslinks = []
    for line in playlist:
        if not line.lstrip().startswith('#'):
            tslinks.append('https://shockwave.streamvid.co'+line)
    
    return tslinks

def makeDirectory(raw_name, season, episodeNumber):
    import os
    name_dir = raw_name + '_s' + season + 'e' + episodeNumber
    parent_dir = '/Users/mica/Movies/'

    path = os.path.join(parent_dir, name_dir)
    os.mkdir(path)

    return path

def downloadTsFile(link, path, counter):  
    import requests
    import time

    time.sleep(1)
    headers['Accept-Encoding'] = 'idenity'
    tsfile = requests.get(link, headers=headers)

    file_name = str(counter)
    filePath = path + '/' + file_name

    with open(filePath,'wb') as f:
        f.write(tsfile.content)


def createJoinFile(path):
    import os
    from natsort import natsorted

    files = natsorted(os.listdir(path))
    join_file = path + '.txt'

    with open(join_file,'w') as f:
        for file in files:
            f.write('file \''+ path + '/' + file + '\' \n') 

    return join_file

def convertToMP4(join_file):
    import os
    import shutil
    import subprocess

    output_file = join_file.replace('.txt','.mp4')
    createMP4 = 'ffmpeg -f concat -safe 0 -i {join_file} -c copy {output_file}'.format(join_file=join_file, output_file=output_file)
    subprocess.run(createMP4, shell=True)

    os.remove(join_file)
    shutil.rmtree(path)


'''
from selenium import webdriver

driver = webdriver.Chrome()
episodePage = getEpisodePage(name, season)
episodeLinks = getEpisodeLinks(episodePage)
driver.close()


downloadLinks = selectEpisodes(episodeLinks)
for episode in downloadLinks:
    tslinks = getFileLinks(episode)
    path = makeDirectory(raw_name, season, downloadLinks['episode']])

    print(len(tslinks),' files to install.')
    for link in tslinks:
        try:
            downloadTsFile(link, path)
        except OSError: 
            print('Remote disconnected, waiting 5 seconds and trying again.')
            time.sleep(5)
            downloadTsFile(link, path)

    join_file = createJoinFile(path)
    convertToMP4(join_file)
'''


# turn download and num list into dictionary
# find parent_dir automatically
# fix counter thing
# fix mutiple webdriver things