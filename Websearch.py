import selenium.webdriver as webdriver

class Web:
    def __init__(self):
        url = "https://www.google.com"
        self.browser = webdriver.Chrome("/Users/Swgityswag/Desktop/chromedriver")
        self.browser.get(url)
        self.position = 0

    def web_search(self,search_term):
        if self.browser == None:
            url = "https://www.google.com"
            self.browser = webdriver.Chrome("/Users/Swgityswag/Desktop/chromedriver")
            self.browser.get(url)
        else:
            search_box = self.browser.find_element_by_name('q')
            search_box.clear()
            search_box.send_keys(search_term)
            search_box.submit()
    
    def scroll_down(self):
        self.position += 700
        self.browser.execute_script("window.scrollTo(0, %d)" % (self.position))

    def scroll_to_bottom(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_up(self):
        self.position -= 700
        self.browser.execute_script("window.scrollTo(0, %d)" % (self.position))
    
    def scroll_to_top(self):
        self.browser.execute_script("window.scrollTo(0, 0);")
    
    def click(self,text):
        self.browser.find_element_by_partial_link_text(text).click()
    
    def return_url(self):
        return self.browser.current_url
    
    def go_back(self):
         self.browser.execute_script("window.history.go(-1)")