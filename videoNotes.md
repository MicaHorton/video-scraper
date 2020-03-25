# Resources
Selenium Docs
https://selenium-python.readthedocs.io/locating-elements.html#locating-hyperlinks-by-link-text
//*[@attribute = "attribute_value"]

Errors with Beautiful Soup That Lead Me To Selenium
https://stackoverflow.com/questions/51082130/getting-empty-src-while-scraping/51088253
https://stackoverflow.com/questions/52521456/empty-src-attribute-returned-with-selenium-on-python

RegEx Cheat Sheet
http://regexlib.com/cheatsheet.aspx

Using Requests Library to Download Video
https://www.codementor.io/@aviaryan/downloading-files-from-urls-in-python-77q3bs0un

About TS Files
https://stackoverflow.com/questions/22188332/download-ts-files-from-video-stream

# To-Do's
## Current
- [ ] run script with createJoinFile function to see if it works (in progress)
- [ ] join files using bash, if it doesn't
- [ ] run ffmpeg from bash to see if it works
- [ ] automate ffmpeg commands with ffmpy or auto-trigger bash script?
 
## Feature Ideas 
- [ ] add progress bar
- [ ] add email/text link option
- [ ] add virus checker
- [ ] add bash line shortcut for easy access

## Floating Bugs
- [ ] definition issues
- [ ] sometimes not all files download?
- [ ] why is different on Chrome?


## Logbook
- [x] add download option
- [x] split download code into more pieces 
- [x] test sending next link at break time

# Current Thoughts
- not an in issue of sudden authentication failure b/c https requests works find after failutre
- not an issue of opening the file interrupting data flow (series of writes)

- has stopped on different files for different episodes. why does it choose to stop when?
- ugh, I hate how it takes so long to test shit, I need to find someway to make the download process faster

# How do I want to structure this?
- such that I can test individual components of the program (flexiblity)
- for flexibility, such that I can re-use some components for scraping other sources (flexibility)
- such that I don't have a bunch of icky variables that kind of sound the same (clean)
- for speed, such that I'm not double importing things (speedy)


Most of this code is 123movies.com specific
but it could be not
