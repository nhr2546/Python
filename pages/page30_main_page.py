from page_objects import PageObject, PageElement
class MainPage(PageObject):
    logout_link = PageElement(link_text="Logout")
    def check_page(self):
        return "Logged" in self.w.title
    def click_logout(self, mainpage):
        self.logout_link.click()
        return "Welcome" in self.w.title
