from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
import time

def login(github_url, github_username, github_password, github_username_field_id, github_password_field_id, github_login_button_id):
    
    # Set the path to the Edge WebDriver
    edge_driver_path = r"PATH_TO_MSEDGEDRIVER_HERE"

    # Set up the Edge service
    service = Service(edge_driver_path)

    # Initialize the Edge driver with the service
    driver = webdriver.Edge(service=service)

    # Maximize the browser window 
    driver.maximize_window()


# Open the login page
    driver.get(github_url)


# Find the username field and send the username 
    github_username_field = driver.find_element(By.ID, github_username_field_id)  
    github_username_field.send_keys(github_username) 

# Find the password field and send the password 
    github_password_field = driver.find_element(By.ID, github_password_field_id)   
    github_password_field.send_keys(github_password)
 
# Find the login button and click it 
    github_login_button = driver.find_element(By.NAME, github_login_button_id)
    github_login_button.click()




# exit loop


    # Keep the browser window open by waiting for user input 
    input("Press Enter to close     the browser...")
 
    # Close the browser 
    driver.quit()





# Replace the placeholder values with the actual values for GitHub login
login(
    github_url='https://github.com/login',
    github_username='YOUR_USERNAME_HERE',   # add username
    github_password='YOUR_PASSWORD_HERE',   # add password
    github_username_field_id='login_field',
    github_password_field_id='password',
    github_login_button_id='commit'
)
