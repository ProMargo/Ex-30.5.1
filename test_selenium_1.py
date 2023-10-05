import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://petfriends.skillfactory.ru/login")
driver.implicitly_wait(10)

class element_has_css_class(object):
  def __init__(self, locator, css_class):
    self.locator = locator
    self.css_class = css_class

  def __call__(self, driver):
    element = driver.find_element(*self.locator)
    if self.css_class in element.get_attribute("class"):
        return element
    else:
        return False

@pytest.fixture(autouse=True)
def driver():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    pytest.driver = webdriver.Chrome(service=service)
    pytest.driver.maximize_window()
    pytest.driver.get('https://petfriends.skillfactory.ru/login')
    yield
    pytest.driver.quit()

def testing():
    driver = webdriver.Chrome('/Users/apple/Downloads/chromedriver.exe')
    # Переходим на страницу авторизации
    driver.get('http://petfriends.skillfactory.ru/login')
    yield
    driver.quit()

def test_show_my_pets():
    # Вводим email
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located(By.ID, "email"))
    pytest.driver.find_element(By.ID, 'email').send_keys('mspromargo@gmail.com')

    # Вводим пароль
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located(By.ID, "pass"))
    pytest.driver.find_element(By.ID, 'pass').send_keys('12qw!@QW')
    # Нажимаем на кнопку входа в аккаунт
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTORD, 'button[type="submit"]'))
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    #driver.find_element(By.XPATH, )
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck.card-img-top')
    names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck.card-title')
    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck.card-text')
    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0


def test_check_my_pets():
    # Вводим email
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    myDynamicElement = pytest.driver.find_element(By.ID, "email")
    pytest.driver.find_element(By.ID, 'email').send_keys('mspromargo@gmail.com')
    # Вводим пароль
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
    myDynamicElement = pytest.driver.find_element(By.ID, "pass")
    pytest.driver.find_element(By.ID, 'pass').send_keys('12qw!@QW')
    # Нажимаем на кнопку входа в аккаунт
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'PetFriends')))
    myDynamicElement = pytest.driver.find_element(By.LINK_TEXT, "PetFriends")
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Мои питомцы')))
    myDynamicElement = pytest.driver.find_element(By.LINK_TEXT, "Мои питомцы")
    pytest.driver.find_element(By.CLASS_NAME, 'nav-link').click()

    assert pytest.driver.find_element(By.TAG_NAME, 'h2').text == "ProMargo"

    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck.card-img-top')
    names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck.card-title')
    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck.card-text')
    num = int(pytest.driver.find_element(By.CLASS_NAME, 'task3').text.split('\n')[1].split(' ')[-1])
    count = 0
    for i in range(len(names)):
        if images[i].get_attribute('src') != '':
            count += 1
        assert count >= num/2
        assert count == num
    for i in range(len(names)):
        if images[i].get_attribute('src') != '' and names[i].text != '' and descriptions[i].text != '':
            assert ', ' in descriptions[i]
            parts = descriptions[i].text.split(", ")
            assert len(parts[0]) == num
            assert len(parts[1]) == num



