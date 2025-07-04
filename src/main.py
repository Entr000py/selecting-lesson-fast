import time
import typer
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import ddddocr

class CourseSelector:
    def __init__(self, username, password, driver_path=None):
        self.username = username
        self.password = password
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        if driver_path:
            self.driver = webdriver.Chrome(executable_path=driver_path, options=options)
        else:
            self.driver = webdriver.Chrome(options=options)
        self.ocr = ddddocr.DdddOcr()

    def login(self):
        """Logs into the course selection system."""
        self.driver.get("http://210.28.81.11/")
        while True:
            try:
                # Get verification code
                icode_element = self.driver.find_element(By.ID, 'icode')
                verification_code = self.ocr.classification(icode_element.screenshot_as_png)

                # Fill in form
                self.driver.find_element(By.ID, 'txtUserName').send_keys(self.username)
                self.driver.find_element(By.ID, 'TextBox2').send_keys(self.password)
                self.driver.find_element(By.ID, 'txtSecretCode').send_keys(verification_code)
                self.driver.find_element(By.ID, 'Button1').click()

                # Check for login success
                self.driver.find_element(By.ID, 'navxl')
                print("Login successful.")
                break
            except (NoSuchElementException, Exception):
                print("Login failed, retrying...")
                self.driver.get("http://210.28.81.11/")
                time.sleep(1)

    def select_course(self, course_id, plate):
        """Navigates to the course selection page and selects a course."""
        main_page_url = f"http://210.28.81.11/xs_main.aspx?xh={self.username}"
        self.driver.get(main_page_url)

        # Navigate to course selection
        move = self.driver.find_element(By.XPATH, '//*[@id="navxl"]/li[2]/a/span')
        ActionChains(self.driver).move_to_element(move).perform()
        self.driver.find_element(By.XPATH, '//*[@id="navxl"]/li[2]/ul/li[1]/a').click()

        # Switch to iframe
        self.driver.switch_to.frame(self.driver.find_element(By.ID, 'iframeautoheight'))
        Select(self.driver.find_element(By.ID, 'kj')).select_by_value(plate)

        # Loop to select the course
        while True:
            try:
                course_element = self.driver.find_element(By.ID, course_id)
                self.driver.execute_script("arguments[0].click();", course_element)
                self.driver.find_element(By.ID, 'Button1').click()

                # Handle alert
                if self.alert_is_present():
                    alert_text = self.driver.switch_to.alert.text
                    print(f"Alert: {alert_text}")
                    self.driver.switch_to.alert.accept()
                
                print("Course selection submitted.")
                break 
            except NoSuchElementException:
                print("Course not found, refreshing...")
                self.driver.refresh()
                time.sleep(1)


    def alert_is_present(self):
        try:
            self.driver.switch_to.alert
            return True
        except Exception:
            return False

    def close(self):
        self.driver.quit()

def main(
    username: str = typer.Option(..., help="Your student ID"),
    password: str = typer.Option(..., help="Your password"),
    course_id: str = typer.Option(..., help="The ID of the course to select (e.g., 'kcmcGrid_xk_4')"),
    plate: str = typer.Option(..., help="The plate of the course to select(e.g., '板块（1）')"),
):
    """
    A tool to automate course selection.
    """
    selector = CourseSelector(username, password)
    selector.login()
    selector.select_course(course_id, plate)
    selector.close()

if __name__ == "__main__":
    typer.run(main)
