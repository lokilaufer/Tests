import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestYandexAuthorization(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://passport.yandex.ru/auth/")

    def test_yandex_authorization(self):
        login_input = self.driver.find_element_by_name("login")
        login_input.send_keys("your_yandex_login")

        password_input = self.driver.find_element_by_name("passwd")
        password_input.send_keys("your_yandex_password")
        password_input.send_keys(Keys.RETURN)

        assert "Аккаунты" in self.driver.title

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
