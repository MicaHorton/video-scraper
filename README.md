# What Does It Do
- Given a show name and season, find a list of links to each episode of the show.
- Download the show (which is served as a stream of .ts files not an .mp4 unfortunately) by extracting the 1080.m3u8 file (which has the paths to all the .ts files) and downloading all the .ts files into a folder which can be played by VLC media player.
- See videoNotes.md for more documentation

# Resources
Selenium Docs
https://selenium-python.readthedocs.io/locating-elements.html#locating-hyperlinks-by-link-text

Errors with Beautiful Soup That Lead Me To Selenium
https://stackoverflow.com/questions/51082130/getting-empty-src-while-scraping/51088253
https://stackoverflow.com/questions/52521456/empty-src-attribute-returned-with-selenium-on-python

RegEx Cheat Sheet
http://regexlib.com/cheatsheet.aspx

Using Requests Library to Download Video
https://www.codementor.io/@aviaryan/downloading-files-from-urls-in-python-77q3bs0un

About TS Files
https://stackoverflow.com/questions/22188332/download-ts-files-from-video-stream

Current Thoughts
#p = element.location
            #actions.move_by_offset(p['x'],p['y']).click(element).perform()

            #actions.move_to_element(element).move_by_offset(p['x'],p['y']).click(element).perform()

            #link = driver.find_element_by_xpath(xpath + '/a[1]')
            #print(link.get_attribute('outerHTML'))
            #actions.move_to_element(element).click(element).perform()
            #element.click()
            #link = 'https://open123movies.com' + element.get_attribute('href')
            #print(link)
            #driver.get(link)s