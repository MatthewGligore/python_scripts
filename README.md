# GitHub Login Automation Script

This script automates the process of logging into a GitHub account using Selenium and the Edge WebDriver.

## Prerequisites

- Python 3.x
- Selenium library (`pip install selenium`)
- Edge WebDriver (download from [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/))

## Script Description

The script opens the GitHub login page, enters the provided username and password, and logs into the account. It uses Selenium to control the Edge browser.

## Configuration

1. **Download and install the Edge WebDriver**:
    - Download the Edge WebDriver that matches your Edge browser version from [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).
    - Extract the downloaded file to a known location on your computer.

2. **Install Selenium**:
    - If you haven't already installed Selenium, you can do so using pip:
      ```bash
      pip install selenium
      ```

3. **Update the script with your details**:
    - Replace the placeholder values in the script with your actual GitHub login details.
    - Update the path to the Edge WebDriver in the script.

### Example

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
import time

def login(github_url, github_username, github_password, github_username_field_id, github_password_field_id, github_login_button_id):
    
    # Set the path to the Edge WebDriver
    edge_driver_path = r"C:\Users\JohnDoe\Downloads\msedgedriver.exe"

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

    # Keep the browser window open by waiting for user input 
    input("Press Enter to close the browser...")
 
    # Close the browser 
    driver.quit()

# Replace the placeholder values with the actual values for GitHub login
login(
    github_url='https://github.com/login',
    github_username='username',
    github_password='password',
    github_username_field_id='login_field',
    github_password_field_id='password',
    github_login_button_id='commit'
)
