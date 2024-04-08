import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Provide the path to the ChromeDriver executable
chromedriver_path = r'C:\Users\RK307977\Downloads\chromedriver_win32\chromedriver.exe'

# Create a service object with the correct path
s = Service(chromedriver_path)

# Create WebDriver instance with the service
driver = webdriver.Chrome(service=s)

# Navigate to the URL
driver.get("https://sephora.service-now.com/incident_list.do?sysparm_query=assignment_group%3D257bfc7946556762017405a980103927%5Eincident_state%3D1%5EORincident_state%3D2%5EORincident_state!%3D7%5")
