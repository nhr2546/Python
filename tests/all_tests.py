import base_test
class TestCases(base_test.BaseTest):
    def test_01_test_login_page_login(self):
        # Step 1:Click on Login and the Login Page Loads
        assert self.welcomepage.click_login(self.loginpage)
