
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 

class Test_Demo:
    def test_invalid_login(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/v1/")
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        usernameInput = driver.find_element(By.ID, "user-name")
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.ID, "password")))
        loginInput = driver.find_element(By.ID, "password")
        usernameInput.send_keys("1")
        loginInput.send_keys("1")
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/form/h3")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU: {testResult}")
        sleep(2) 
    def test_invalid2_login(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/v1/")  
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        usernameInput = driver.find_element(By.ID, "user-name")
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.ID, "password")))
        loginInput = driver.find_element(By.ID, "password")
        usernameInput.send_keys()
        loginInput.send_keys("1")
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/form/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"TEST SONUCU: {testResult}")
        sleep(2)
        
        
    def test_invalid3_login(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/v1/")  
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        usernameInput = driver.find_element(By.ID, "user-name")
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.ID, "password")))
        loginInput = driver.find_element(By.ID, "password")
        usernameInput.send_keys("dkfskf")
        loginInput.send_keys()
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/form/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"TEST SONUCU: {testResult}")
        sleep(2) 

    def test_valid_login(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/v1/")  
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        usernameInput = driver.find_element(By.ID, "user-name")
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.ID, "password")))
        loginInput = driver.find_element(By.ID, "password")
        usernameInput.send_keys("standard_user")
        loginInput.send_keys("secret_sauce")
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)    

testClass = Test_Demo()
testClass.test_invalid_login()
testClass.test_invalid2_login()
testClass.test_invalid3_login()
testClass.test_valid_login()
