from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


class RequestEngine:
    def __init__(self, driver_path: str = 'chromedriver.exe'):
        service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=service)

    def calculate(self, string: str) -> int:
        self.driver.get('http://google.com')

        self.driver.find_element(By.CLASS_NAME, 'gLFyf').send_keys('Калькулятор')

        time.sleep(1)

        self.driver.find_element(By.CLASS_NAME, 'gNO89b').click()

        time.sleep(1)

        self.driver.find_element(By.CLASS_NAME, 'jlkklc').send_keys(string)
        self.driver.find_element(By.CLASS_NAME, 'UUhRt ').click()

        result = int(self.driver.find_element(By.CLASS_NAME, 'qv3Wpe').text)

        return result

    def close(self):
        self.driver.close()


def calc(string: str) -> int:
    engine = RequestEngine()
    result = engine.calculate(string)

    time.sleep(0.5)
    engine.close()

    return result


if __name__ == '__main__':
    calc('1 * 2 - 3 + 1')
