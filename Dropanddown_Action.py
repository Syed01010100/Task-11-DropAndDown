# Program - Drop and Down include iframe with ActionChains ( https://jqueryui.com/droppable/ )
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import StaleElementReferenceException


from selenium.webdriver.common.action_chains import ActionChains



class DragAndDrop:

    source_locator = "//*[@id='draggable']"
    target_locator = "//*[@id='droppable']"

    def __init__(self,url):
        self.url=url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def open_url(self):
        try:
         self.driver.maximize_window()
         self.driver.get(self.url)
         sleep(3)
         return True

        except WebDriverException as e:
            print("Error : URL NOT WORKING", e)
            return False


    def switch_to_iframe(self):
        try:
         iframe_element=self.driver.find_element(by=By.TAG_NAME, value="iframe")
         self.driver.switch_to.frame(iframe_element)
         sleep(2)
         return True

        except StaleElementReferenceException as e:
            print("Error : element not found")
            return False

    def perform_drag_and_drop(self):
        try:
         action = ActionChains(self.driver)
         # Locate the source and target elements
         source_element = self.driver.find_element(by=By.XPATH,value=self.source_locator)
         target_element = self.driver.find_element(by=By.XPATH, value=self.target_locator)
         if source_element.is_displayed() and target_element.is_displayed(): # to check displayed source and target
            if source_element.is_enabled() and target_element.is_enabled():

                action.drag_and_drop(source_element,target_element).perform()# Perform drag and drop
                sleep(2)
                return True

        except (NoSuchElementException,ElementNotVisibleException) as e:
            print("Error :cant locate the element",e)
            return True

        finally:
            self.driver.quit()
            return None

if __name__=="__main__":
    url = "https://jqueryui.com/droppable/"
    Syed = DragAndDrop(url)
    Syed.open_url()
    Syed.switch_to_iframe()
    Syed.perform_drag_and_drop()
