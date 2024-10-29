from time import sleep
import time
import unittest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.action_chains import ActionChains
from fake_useragent import UserAgent

def delay():
    time.sleep(random.randint(1,5))

class ChromePositiveTestCases(unittest.TestCase):
    def setUp(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()


    def test_case_001(self):
        driver = self.driver
        print("                                                                                                    ")
        print("                                          Apple - Store                                  ")
        print("                                                                                                    ")
        print("-----------------------------------------POSITIVE TEST CASES ---------------------------------------")
        print("                                                                                                    ")

        # test_case_001
        print("                                                                                                    ")
        print("             Apple-Store test_case_001                                                                  ")
        print("             ------------------------                                                               ")




        driver.get("https://www.apple.com")
        time.sleep(3)


        #Click on the header menu "Store"
        store_menu = driver.find_element(By.XPATH, "(//span[contains(.,'Store')])[1]" )
        store_menu.click()
        time.sleep(6)

        # Verify that the current URL contains 'Store'
        current_url = driver.current_url
        self.assertIn("https://www.apple.com/store", current_url, "Failed to navigate to Store page.")

        # Verify the content on the Store page
        store_page_content = driver.find_element(By.XPATH, "//div[@class='rs-cardsshelf rs-productnav-cardsshelf']")
        self.assertTrue(store_page_content.is_displayed(), "The Apple Store content is not displayed on the Store page")

        mac_link = driver.find_element(By.XPATH, "//a[@href='/shop/buy-mac']")
        self.assertTrue(mac_link.is_displayed(), "Mac link is not visible on the Store page.")

        iPhone_link = driver.find_element(By.XPATH, "(//a[contains(.,'iPhone')])[17]")
        self.assertTrue(iPhone_link.is_displayed(), "iPhone link is not visible on the Store page.")

        iPad_link = driver.find_element(By.XPATH, "(//a[contains(.,'iPad')])[17]")
        self.assertTrue(iPad_link.is_displayed(), "iPad link is not visible on the Store page.")

        apple_watch_link = driver.find_element(By.XPATH, "(//a[contains(.,'Apple Watch')])[16]")
        self.assertTrue(apple_watch_link.is_displayed(), "Apple watch link is not visible on the Store page.")

        apple_vision_pro_link = driver.find_element(By.XPATH, "//a[@href='/shop/buy-vision']")
        self.assertTrue(apple_vision_pro_link.is_displayed(), "Apple vision pro link is not visible on the Store page.")

        airPods_link = driver.find_element(By.XPATH, "(//a[contains(.,'AirPods')])[13]")
        self.assertTrue(airPods_link.is_displayed(), "AirPods link is not visible on the Store page.")

        airTag_link = driver.find_element(By.XPATH, "(//a[contains(.,'AirTag')])[3]")
        self.assertTrue(airTag_link.is_displayed(), "AirTag link is not visible on the Store page.")

        appleTV_link = driver.find_element(By.XPATH, "(//a[contains(.,'Apple TV 4K')])[3]")
        self.assertTrue(appleTV_link.is_displayed(), "Apple TV 4K link is not visible on the Store page.")


        # Test results for test_case_001
        print("                                                                                                    ")
        print("        !!!  test_case_001  PASS   !!!                                                              ")
        print("        --------------------                                                                        ")


    def test_case_002(self):
        driver = self.driver
        print("                                                                                                    ")
        print("                                          Apple - Store                                  ")
        print("                                                                                                    ")
        print("-----------------------------------------POSITIVE TEST CASES ---------------------------------------")
        print("                                                                                                    ")

        # test_case_002
        print("                                                                                                    ")
        print("             Apple-Store test_case_002                                                                  ")
        print("             ------------------------                                                               ")

        driver.get("https://www.apple.com")
        time.sleep(3)

        #Click on the header menu "Store"
        store_menu = driver.find_element(By.XPATH, "(//span[contains(.,'Store')])[1]" )
        store_menu.click()
        time.sleep(6)

        store_menu = driver.find_element(By.LINK_TEXT, "Store")
        self.assertTrue(store_menu.is_displayed(), "Store link is not visible on the homepage.")
        store_menu.click()

        # Wait for the page to load and ensure the Store page is displayed
        driver.implicitly_wait(5)
        current_url = driver.current_url
        self.assertIn("https://www.apple.com/store", current_url, "Failed to navigate to the Store page.")

        #Locate the "Mac" link and click it
        mac_link = driver.find_element(By.XPATH, "(//a[contains(.,'Mac')])[19]")
        self.assertTrue(mac_link.is_displayed(), "Mac link is not visible on the Store page.")
        mac_link.click()

        #Verify redirection to the correct "Mac" page
        driver.implicitly_wait(10)
        mac_url = driver.current_url
        self.assertIn("https://www.apple.com/shop/buy-mac", mac_url, "Failed to navigate to the Mac page.")

        #Check page contents (ensure the page has Mac-related content)
        mac_header = driver.find_element(By.XPATH, "(//a[contains(.,'Mac')])[19]")
        self.assertTrue(mac_header.is_displayed(), "Mac-related content is not displayed on the page.")

        # Verify that the page contains Mac-related product links (MacBook Pro, MacBook Air)
        macbook_pro_link = driver.find_element(By.XPATH, "//h3[contains(text(),'MacBook Pro')]")
        self.assertTrue(macbook_pro_link.is_displayed(), "MacBook Pro link is not visible on the Mac page.")

        macbook_air_link = driver.find_element(By.XPATH, "//h3[contains(.,'MacBook Air with M2 or M3 chip')]")
        self.assertTrue(macbook_air_link.is_displayed(), "MacBook Air link is not visible on the Mac page.")

        imac_link = driver.find_element(By.XPATH, "//h3[contains(.,'iMac')]")
        self.assertTrue(imac_link.is_displayed(), "iMac link is not visible on the Mac page.")
        # Test results for test_case_001
        print("                                                                                                    ")
        print("        !!!  test_case_002  PASS   !!!                                                              ")
        print("        --------------------                                                                        ")

    def test_case_003(self):
        driver = self.driver
        print("                                                                                                    ")
        print("                                          Apple - Store                                             ")
        print("                                                                                                    ")
        print("-----------------------------------------POSITIVE TEST CASES ---------------------------------------")
        print("                                                                                                    ")

        # test_case_003
        print("                                                                                                    ")
        print("             Apple-Store test_case_003                                                                  ")
        print("             ------------------------                                                               ")

        driver.get("https://www.apple.com")
        time.sleep(3)

        #Click on the header menu "Store"
        store_menu = driver.find_element(By.XPATH, "(//span[contains(.,'Store')])[1]" )
        store_menu.click()
        time.sleep(6)

        store_menu = driver.find_element(By.LINK_TEXT, "Store")
        self.assertTrue(store_menu.is_displayed(), "Store link is not visible on the homepage.")
        store_menu.click()

        # Wait for the page to load and ensure the Store page is displayed
        driver.implicitly_wait(5)
        current_url = driver.current_url
        self.assertIn("https://www.apple.com/store", current_url, "Failed to navigate to the Store page.")

        #Locate the "Mac" link and click it
        mac_link = driver.find_element(By.XPATH, "(//a[contains(.,'Mac')])[19]")
        self.assertTrue(mac_link.is_displayed(), "Mac link is not visible on the Store page.")
        mac_link.click()

        #Verify redirection to the correct "Mac" page
        driver.implicitly_wait(5)
        mac_url = driver.current_url
        self.assertIn("https://www.apple.com/shop/buy-mac", mac_url, "Failed to navigate to the Mac page.")

        #Check page contents (ensure the page has Mac-related content)
        mac_header = driver.find_element(By.XPATH, "(//a[contains(.,'Mac')])[19]")
        self.assertTrue(mac_header.is_displayed(), "Mac-related content is not displayed on the page.")
        time.sleep(4)

        # Scroll to the "Shopping Guides" section (this step might vary based on the page layout)
        driver.execute_script("window.scrollBy(0, 800)")

        # Test the right arrow functionality
        right_arrow = driver.find_element(By.XPATH, "//button[contains(.,'Next - Shopping guides')]")
        right_arrow.click()
        time.sleep(3)

        driver.execute_script("window.scrollBy(0, 800)")
        right_arrow = driver.find_element(By.XPATH, "//button[contains(.,'Next - Shopping guides')]")
        right_arrow.click()
        time.sleep(3)


        # Test the left arrow functionality to go back to the original slide
        left_arrow = driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Previous - Shopping guides')]")
        left_arrow.click()
        time.sleep(3)
        # Wait for the carousel to slide back

        left_arrow = driver.find_element(By.XPATH, "//button[contains(.,'Previous - Shopping guides')]")
        left_arrow.click()
        time.sleep(3)


        # Test results for test_case_003
        print("                                                                                                    ")
        print("        !!!  test_case_003  PASS   !!!                                                              ")
        print("        --------------------                                                                        ")

    def test_case_004(self):
        driver = self.driver
        print("                                                                                                    ")
        print("                                          Apple - Store                                             ")
        print("                                                                                                    ")
        print("-----------------------------------------POSITIVE TEST CASES ---------------------------------------")
        print("                                                                                                    ")

        # test_case_004
        print("                                                                                                    ")
        print(
            "             Apple-Store test_case_004                                                                  ")
        print("             ------------------------                                                               ")

        driver.get("https://www.apple.com")
        time.sleep(3)

        # Click on the header menu "Store"
        store_menu = driver.find_element(By.XPATH, "(//span[contains(.,'Store')])[1]")
        store_menu.click()
        time.sleep(6)

        store_menu = driver.find_element(By.LINK_TEXT, "Store")
        self.assertTrue(store_menu.is_displayed(), "Store link is not visible on the homepage.")
        store_menu.click()

        # Wait for the page to load and ensure the Store page is displayed
        driver.implicitly_wait(5)
        current_url = driver.current_url
        self.assertIn("https://www.apple.com/store", current_url, "Failed to navigate to the Store page.")

        # Locate the "Mac" link and click it
        mac_link = driver.find_element(By.XPATH, "(//a[contains(.,'Mac')])[19]")
        self.assertTrue(mac_link.is_displayed(), "Mac link is not visible on the Store page.")
        mac_link.click()

        # Verify redirection to the correct "Mac" page
        driver.implicitly_wait(10)
        mac_url = driver.current_url
        self.assertIn("https://www.apple.com/shop/buy-mac", mac_url, "Failed to navigate to the Mac page.")

        # Check page contents (ensure the page has Mac-related content)
        mac_header = driver.find_element(By.XPATH, "(//a[contains(.,'Mac')])[19]")
        self.assertTrue(mac_header.is_displayed(), "Mac-related content is not displayed on the page.")
        time.sleep(4)

        # Scroll to the "Shopping Guides" section (this step might vary based on the page layout)
        driver.execute_script("window.scrollBy(0, 800)")

        # Test the right arrow functionality
        right_arrow = driver.find_element(By.XPATH, "//button[contains(.,'Next - Shopping guides')]")
        ActionChains(driver).move_to_element(right_arrow).click().perform()

        # Wait for a brief moment to allow the carousel to slide (explicit waits can also be used)
        time.sleep(2)

        # Scroll to the "Shopping Guides" section (this step might vary based on the page layout)
        driver.execute_script("window.scrollBy(0, 800)")

        right_arrow = driver.find_element(By.XPATH, "//button[contains(.,'Next - Shopping guides')]")
        ActionChains(driver).move_to_element(right_arrow).click().perform()
        time.sleep(2)

        #Locate the video
        video = driver.find_element(By.XPATH, "//button[contains(.,'Play')]")
        video.click()
        driver.implicitly_wait(5)
        time.sleep(5)
        driver.execute_script('document.getElementsByTagName("video")[0].play()')
        time.sleep(5)
        driver.execute_script('document.getElementsByTagName("video")[0].pause()')
        time.sleep(2)
        driver.execute_script('document.getElementsByTagName("video")[0].play()')
        time.sleep(5)
        driver.execute_script("return arguments[0].duration", video)
        driver.execute_script("return arguments[0].currentTime", video)

        self.assertTrue(video.is_displayed(), "Video did not play")
        if video.is_displayed():
            print("Video is play - Test Case 004 passed")
        else:
            raise Exception("Video is not play - Test Case 004 failed")


        try:
            assert video.get_attribute("paused") == "true"
            print("Video is not paused: ", video)
        except AssertionError:
            print("Video is  paused: ", video)

        try:
            assert video.get_attribute("resumed") == "false"
            print("Video is not resumed: ", video)
        except AssertionError:
            print("Video is resumed")



        try:
            assert video.get_attribute("duration") == "true"
            print("Video duration is not valid or video not loaded properly: ", video)
        except AssertionError:
            print("Video duration is valid or video loaded properly : ", video)



        # Test results for test_case_004
        print("                                                                                                    ")
        print("        !!!  test_case_004  PASS   !!!                                                              ")
        print("        --------------------                                                                        ")
    def test_case_005(self):
        driver = self.driver
        print("                                                                                                    ")
        print("                                          Apple - Store                                             ")
        print("                                                                                                    ")
        print("-----------------------------------------POSITIVE TEST CASES ---------------------------------------")
        print("                                                                                                    ")

        # test_case_005
        print("                                                                                                    ")
        print("             Apple-Store test_case_005                                                              ")
        print("             ------------------------                                                               ")

        driver.get("https://www.apple.com")
        time.sleep(3)

        # Click on the header menu "Store"
        store_menu = driver.find_element(By.XPATH, "(//span[contains(.,'Store')])[1]")
        store_menu.click()
        time.sleep(6)

        store_menu = driver.find_element(By.LINK_TEXT, "Store")
        self.assertTrue(store_menu.is_displayed(), "Store link is not visible on the homepage.")
        store_menu.click()

        # Wait for the page to load and ensure the Store page is displayed
        driver.implicitly_wait(5)
        current_url = driver.current_url
        self.assertIn("https://www.apple.com/store", current_url, "Failed to navigate to the Store page.")

        # Locate the "Mac" link and click it
        mac_link = driver.find_element(By.XPATH, "(//a[contains(.,'Mac')])[19]")
        self.assertTrue(mac_link.is_displayed(), "Mac link is not visible on the Store page.")
        mac_link.click()

        # Verify redirection to the correct "Mac" page
        driver.implicitly_wait(10)
        mac_url = driver.current_url
        self.assertIn("https://www.apple.com/shop/buy-mac", mac_url, "Failed to navigate to the Mac page.")
        time.sleep(3)

        next_button = driver.find_element(By.XPATH, "//button[contains(.,'Next - All Models')]")
        next_button.click()
        time.sleep(2)
        next_button = driver.find_element(By.XPATH, "//button[contains(.,'Next - All Models')]")
        next_button.click()
        time.sleep(2)
        next_button= driver.find_element(By.XPATH, "//button[contains(.,'Next - All Models')]")
        next_button.click()
        time.sleep(2)
        next_button = driver.find_element(By.XPATH, "//button[contains(.,'Next - All Models')]")
        next_button.click()
        time.sleep(2)
        next_button = driver.find_element(By.XPATH, "//button[contains(.,'Next - All Models')]")
        next_button.click()
        time.sleep(2)
        next_button = driver.find_element(By.XPATH, "//button[contains(.,'Next - All Models')]")
        next_button.click()
        time.sleep(2)
        print("----Next scroll 6 times completed")

        previous_button = driver.find_element(By.XPATH, "// button[contains(., 'Previous - All Models')]")
        previous_button.click()
        time.sleep(2)
        previous_button = driver.find_element(By.XPATH, "// button[contains(., 'Previous - All Models')]")
        previous_button.click()
        time.sleep(2)
        previous_button = driver.find_element(By.XPATH, "// button[contains(., 'Previous - All Models')]")
        previous_button.click()
        time.sleep(2)
        previous_button = driver.find_element(By.XPATH, "// button[contains(., 'Previous - All Models')]")
        previous_button.click()
        time.sleep(2)
        previous_button = driver.find_element(By.XPATH, "// button[contains(., 'Previous - All Models')]")
        previous_button.click()
        time.sleep(2)
        previous_button = driver.find_element(By.XPATH, "// button[contains(., 'Previous - All Models')]")
        previous_button.click()
        time.sleep(2)

        print("----Previous scroll 6 times completed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()