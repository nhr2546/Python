import base_test
class TestCases(base_test.BaseTest):
    def test_01_test_login_page_login(self):
        # Step 1:Click on Login and the Login Page Loads
        assert self.welcomepage.click_login(self.loginpage)
        # Step 2: Login to the webpage and confirm the main page appears
        assert self.loginpage.login(self.mainpage, "testuser", "testing")
        # Step 3: Logout of the webpage and confirm it returs to the welcome page
        assert self.mainpage.click_logout(self.welcomepage)
        # Last line
