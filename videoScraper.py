# GET USER INPUT
print('Show Name:', end=' ')
raw_name = input()
name = raw_name.lower().replace(' ','-')
print('Season #:', end=' ')
season = input()

# TRY 123MOVIES
from movies123 import *

from selenium import webdriver
driver = webdriver.Chrome()

getEpisodePage2(name, season, driver)

driver.close()




'''
try:
    getEpisodePage(name, season, driver)
except AssertionError:
    try:
        getEpisodePage2(name, season, driver)
    except AssertionError:
        print('Show not found.')

episodePage = getEpisodePage()

episodeLinks = getEpisodeLinks(episodePage, driver)

driver.close()


downloadLinks = selectEpisodes(episodeLinks)
for episode in downloadLinks:
    tslinks = getFileLinks(episode['url'])
    path = makeDirectory(raw_name, season, episode['number'])

    print(len(tslinks),' files to install.')
    counter = 0
    for link in tslinks:
        try:
            counter += 1
            downloadTsFile(link, path, counter)
        except OSError: 
            print('Remote disconnected, waiting 5 seconds and trying again.')
            time.sleep(5)
            downloadTsFile(link, path)

    join_file = createJoinFile(path)
    convertToMP4(join_file, path)

'''