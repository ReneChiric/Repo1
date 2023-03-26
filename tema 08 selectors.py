from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

LINK = ('https://formy-project.herokuapp.com/')

driver.get(LINK)
time.sleep(1)

id1 = driver.find_element(By.ID, 'logo') #id 1
time.sleep(5)
id1.click()
id2 = driver.find_element(By.ID, 'navbarNavDropdown') #id2
time.sleep(5)

LINK2 = ('https://phptravels.net/')
driver.get(LINK2)
time.sleep(5)

id3 = driver.find_element(By.ID, 'loading') #id3
time.sleep(5)

driver.get(LINK)
time.sleep(4)
LINK_TEXT1 = driver.find_element(By.LINK_TEXT, 'Autocomplete') #link text 1
LINK_TEXT1.click()
time.sleep(3)

driver.get(LINK)
time.sleep(2)
LINK_TEXT2 = driver.find_element(By.LINK_TEXT, 'Datepicker') #link text 2
LINK_TEXT2.click()
time.sleep(3)

driver.get(LINK)
time.sleep(2)
LINK_TEXT3 = driver.find_element(By.LINK_TEXT, 'Dropdown') #link text 3
LINK_TEXT3.click()
time.sleep(2)

driver.get(LINK)
time.sleep(2)
partial_link1 = driver.find_element(By.PARTIAL_LINK_TEXT, 'down') #partial link 1
partial_link1.click()
time.sleep(2)

driver.get(LINK)
time.sleep(2)
partial_link2 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Dro') #partial link 2
partial_link2.click()
time.sleep(2)

driver.get(LINK)
time.sleep(2)
partial_link3 = driver.find_element(By.PARTIAL_LINK_TEXT, 'dal') #partial link 3
partial_link3.click()
time.sleep(2)



LINK3 = 'https://www.techlistic.com/p/selenium-practice-form.html'
driver.get(LINK3)
time.sleep(2)
name_link = driver.find_element(By.NAME, 'theme-color') #name 1
time.sleep(1)


driver.get(LINK3)
time.sleep(2)
name_link2 = driver.find_element(By.NAME, 'msapplication-navbutton-color') #name 2
time.sleep(1)

driver.get(LINK3)
time.sleep(2)
name_link3 = driver.find_element(By.NAME,'generator') #name 3
time.sleep(1)

LINK4 = 'https://the-internet.herokuapp.com/'
driver.get(LINK4)
time.sleep(2)
driver.maximize_window()
tagname1 = driver.find_elements(By.TAG_NAME, 'class')




LINK4 = 'https://formy-project.herokuapp.com/'
driver.get(LINK4)
time.sleep(2)
driver.maximize_window()
tagnames = driver.find_elements(By.TAG_NAME, 'li')
print(f'{tagnames}')


driver.get(LINK4)
time.sleep(2)
class_search = driver.find_elements(By.CLASS_NAME, 'navbar') #search by Class name
print(f'{class_search}')

LINK5 = 'https://the-internet.herokuapp.com/'
driver.get(LINK5)
time.sleep(2)
class_search2 = driver.find_elements(By.CLASS_NAME, 'row') #multiple search by Class name
print(f'{class_search2}')

driver.get(LINK5)
time.sleep(2)
tag_name_search = driver.find_elements(By.TAG_NAME, 'li') #multiple search by Tag Name
print(f'{tag_name_search}')


driver.get(LINK4)
time.sleep(1)
css_search_id = driver.find_element(By.CSS_SELECTOR, 'a#logo') #CSS selector by ID
print(f'{css_search_id}')

driver.get(LINK4)
time.sleep(1)
css_search_by_class = driver.find_element(By.CSS_SELECTOR, 'a.navbar-brand') #css selector by class name
print(f'{css_search_by_class}')


LINK6 = "https://phptravels.net/"
driver.get(LINK6)
time.sleep(1)
css_search_by_value = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter your email"]') #css selector by atribute/value
print(f'{css_search_by_value}')

driver.get(LINK6)
time.sleep(1)
css_search_by_partial_value = driver.find_element(By.CSS_SELECTOR, 'input[placeholder*="Enter yo"]') #css selector search by partial value
print(f'{css_search_by_partial_value}')


driver.get(LINK6)
time.sleep(1)
xpath_value1 = driver.find_element(By.XPATH, '//*[@id="select2-hotels_city-container"]') #1 xpath by attribute/value
print(f'{xpath_value1}')


driver.get(LINK4)
time.sleep(1)
xpath_value2 = driver.find_element(By.XPATH, '//li[@class="nav-item"]') #2xpath by attribute/value
print(f'{xpath_value2}')


driver.get(LINK4)
time.sleep(1)
xpath_value3 = driver.find_element(By.XPATH, '//li/a[@class="nav-link"]') #3 xpath by attribute/value
print(f'{xpath_value3}')


driver.get(LINK6)
time.sleep(1)
xpath_text = driver.find_element(By.XPATH, '//*[text()="Travel to anytime, anywhere"]') #xpath by text
print(f'{xpath_text}')

driver.get(LINK4)
time.sleep(1)
xpath_text2 = driver.find_element(By.XPATH, '//*[text()="Here are the list of all the components"]') #2 xpath by text
print(f'{xpath_text2}')

driver.get(LINK5)
time.sleep(1)
xpath_text3 = driver.find_element(By.XPATH, "//h2[contains(text(),'Available Examples')]") #3 xpath by text
print(f'{xpath_text3}')

driver.get(LINK5)
time.sleep(1)
partial_xpath = driver.find_element(By.XPATH, "//h1[contains(text(),'Welcome')]") #xpath by partial text
print(f'{partial_xpath}')

LINK7 = "https://www.automatetheplanet.com/applications/most-exhaustive-xpath-locators-cheat-sheet/"
driver.get(LINK7)
time.sleep(1)
pipe = driver.find_element(By.XPATH, '//*[@id="menu-item-9565"] | //*[@class="c_def menu-item menu-item-type-custom menu-item-object-custom toplvl"]') #using pipe/or
print(f'{pipe}')

driver.get(LINK6)
time.sleep(1)
xpath_steluta = driver.find_element(By.XPATH, '//*[text()="Travel to anytime, anywhere"]') #using *
print(f'{xpath_steluta}')

driver.get(LINK7)
time.sleep(1)
xpath_lista = driver.find_element(By.XPATH, '//div[7]') #using xpath[x]
print(f'{xpath_lista}')

driver.get(LINK7)
time.sleep(1)
xpath_parent = driver.find_element(By.XPATH, '//div[@class="th"]/parent::div') #using parent::
print(f'{xpath_parent}')

driver.get(LINK7)
time.sleep(1)
xpath_sibling = driver.find_element(By.XPATH, '//div[@class="th"]/following-sibling::div') #following sibling
print(f'{xpath_sibling}')

#user choice
driver.get(LINK5)
time.sleep(1)
optiunea1 = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[3]/a')
optiunea2 = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[2]/a')

# def userchoice():
#     userchoice = int(input(f'Va rugam alegeti una dintre cele 2 optiuni'))
#     if userchoice == 1:
#         driver.get(LINK5)
#         time.sleep(1)
#         optiunea1.click()
#     if userchoice == 2:
#         driver.get(LINK5)
#         time.sleep(1)
#         optiunea2.click()
#
# userchoice() #INCA IN LUCRU