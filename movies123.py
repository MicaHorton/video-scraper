# GET EPISODE LINKS
def getEpisodePage(name, season, driver):
    base = 'https://ww7.123moviesfree.sc/season/{name}-season-{season}/'
    introPage = base.format(name=name,season=season)
    driver.get(introPage)
    
    assert not '404' in driver.page_source

    playButton = driver.find_element_by_xpath('//*[@id="mv-info"]/a') 
    episodePage = (playButton.get_attribute('href'))
    driver.get(episodePage)

def getEpisodePage2(name, season, driver):
    pageFound = False
    page = 1

    while pageFound == False:
        if page == 1:
            driver.get('https://open123movies.com/tvshows')
        else:
            driver.get('https://open123movies.com/tvshows/page/' + str(page))

        showList = driver.find_elements_by_xpath('//*[@data-movie-id="363"]/a')

        for item in showList:
            if name in item.get_attribute('href'):
                item.click()
                pageFound = True
                break
        
        assert page != 40
        page += 1

    
    seasonList = driver.find_elements_by_xpath('//div[@class="les-title"]/strong')
    for item in seasonList:
        if str(season) in item.get_attribute('innerHTML'):
            # This is the right season, find the link attached to the div of an episode next to it
            number = len(seasonList) - seasonList.index(item)
            xpath = '//*[@id="seasons"]/div[{number}]/div[2]/a[1]'.format(number=str(number))

            element = driver.find_element_by_xpath(xpath)
            driver.execute_script("arguments[0].scrollIntoView();", element)
            #driver.fullscreen_window()
            
            element.click()


def getEpisodeLinks(driver):
    # Get all episodes by data-server attribute, then print (and store) episode name and video URL
    episodeLinks = []
    episodes = driver.find_elements_by_xpath('(//div[@class="les-content"])[1]/a')
    for item in episodes:
        name = item.get_attribute('innerHTML')
        url = item.get_attribute('data-drive')
        if url != None: 
            episodeLinks.append({'name':name,'url':url})
    
    # Print episode links
    for item in episodeLinks:
        print('{name:<80} {url:<80}'.format(name=item['name'], url=item['url']).rstrip())

    return episodeLinks

# DOWNLOAD EPISODES
def selectEpisodes(episodeLinks):
    import re

    print('Download Episodes?')
    userList = re.findall('[0-9]+', input()) # results in list (that is iterated through number in userList)
    downloadLinks = []

    for item in episodeLinks: 
        episodeNumber = re.findall('[0-9]+', item['name'])[0] # results in list, but isn't iterated through, hence the [0]
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

def convertToMP4(join_file, path):
    import os
    import shutil
    import subprocess

    output_file = join_file.replace('.txt','.mp4')
    createMP4 = 'ffmpeg -f concat -safe 0 -i {join_file} -c copy {output_file}'.format(join_file=join_file, output_file=output_file)
    subprocess.run(createMP4, shell=True)

    os.remove(join_file)
    shutil.rmtree(path)


# find parent_dir automatically
# fix mutiple webdriver things

