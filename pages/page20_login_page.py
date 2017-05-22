from page_objects import PageObject, PageElement
class LoginPage(PageObject):
    def check_page(self):
        return "Sign" in self.w.title
