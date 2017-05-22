from page_objects import PageObject, PageElement
class WelcomePage(PageObject):
    login_link = PageElement(link_text="Login")
    def check_page(self):
        return "Welcome" in self.w.title
    def click_login(self, loginpage):
        self.login_link.click()
        return loginpage.check_page()
