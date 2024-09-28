from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://jqueryui.com/droppable/")

act = ActionChains(driver)

scr = driver.find_element(by=By.XPATH,"//*[@id="draggable"]")
des = driver.find_element(by=By.XPATH,"//*[@id="droppable"]")

sleep(3)

#scr = driver.find_element(by=By.XPATH,"/html/body/div[1] )
#des = driver.find_element(by=By.XPATH,"/html/body/div[1]")
#scr = driver.find_element(By.XPATH, "])

act.drag_and_drop(scr,des).perform()