import User
from Websearch import Web
import re

def open_browser(user):
    user.browser = Web()

def open_blackboard(user):
    if not user.browser:
        user.browser = Web()
    url = 'https://ole.sandiego.edu/?new_loc=%2Fultra%2Fcourses%2F_57779_1%2Fcl%2Foutline%3FlegacyUrl%3D%25252Fwebapps%25252Fassignment%25252FuploadAssignment%253Fcontent_id%253D_1399747_1%2526course_id%253D_57779_1%2526group_id%253D%2526mode%253Dview'
    user.browser.get(url)

def search_web(user,command):
    reg_ex = command.split('for')
    if reg_ex:
        search_item = reg_ex[1]
        if not user.browser:
            user.browser = Web()
        user.browser.web_search(search_item)
    else:
        pass

def search_again(user,command):
    reg_ex = re.search('search again for (.+)',command)
    if reg_ex:
        search_item = reg_ex.group(1)
        user.browser.web_search(search_item)
    else:
        pass

def scroll_down_webpage(user):
    user.browser.scroll_down()

def scroll_to_bottom_webpage(user):
    user.browser.scroll_to_bottom()

def scroll_to_top_webpage(user):
    user.browser.scroll_to_top()

def select_link(user,text):
    user.browser.click(text)

def return_current_url(user):
    return user.browser.return_url()

def go_back(user):
    user.browser.go_back()

# elif 'current weather in' in command:
#     talkToMe("command accepted")
#     reg_ex = re.search('current weather in (.*)', command)
#     if reg_ex:
#         city = reg_ex.group(1)
#         weather = Weather()
#         location = weather.lookup_by_location(city)
#         condition = location.condition
#         talkToMe('The Current weather in %s is %s The tempeture is %.1f degree' % (city, condition.text, (int(condition.temp-32)/1.8)))

# elif 'weather forecast in' in command:
#     talkToMe("command accepted")
#     reg_ex = re.search('weather forecast in (.*)', command)
#     if reg_ex:
#         city = reg_ex.group(1)
#         weather = Weather()
#         location = weather.lookup_by_location(city)
#         forecasts = location.forecast
#         for i in range(0,3):
#             talkToMe('On %s will it %s. The maximum temperture will be %.1f degree.'
#                      'The lowest temperature will be %.1f degrees.' % (forecasts[i].date(), forecasts[i].text(), (int(forecasts[i].high())-32)/1.8, (int(forecasts[i].low())-32)/1.8))