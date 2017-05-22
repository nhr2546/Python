from page_objects import PageObject, PageElement
class LoginPage(PageObject):
    def check_page(self):
        return "Sign" in self.w.title
    username_field = PageElement(id_ = "myid")
    password_field = PageElement(id_ = "mypass")
    def login(self, mainpage, username, password):
        self.username_field.send_keys(username)
        self.password_field.send_keys(password)
        self.password_field.submit()
        return mainpage.check_page()

