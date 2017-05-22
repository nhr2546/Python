from selenium import webdriver
class Parameters():
    def __init__(self):
        self.w = webdriver.Chrome()
        self.rootUrl = "http://automate.safebear.co.uk"
        self.w.implicitly_wait(5)

