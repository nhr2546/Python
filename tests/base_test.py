import unittest
from utils import Parameters
from page10_welcome_page import WelcomePage
from page20_login_page import LoginPage
from page30_main_page import MainPage
from page40_frames_page import FramePage
class BaseTest(unittest.TestCase):
    param = Parameters()
    welcomepage = WelcomePage(param.w, param.rootUrl)
    loginpage = LoginPage(param.w, param.rootUrl)
    mainpage = MainPage(param.w, param.rootUrl)
    framepage = FramePage(param.w, param.rootUrl)
    def test_setUp(self):
        self.param.w.get(self.param.rootUrl)
        self.param.w.maximize_window()


