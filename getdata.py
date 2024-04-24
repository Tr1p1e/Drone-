import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome webdriver
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

# Load the webpage
url = "http://127.0.0.1:5500/map.html"
driver.get(url)

time.sleep(1)

# Extract latitude and longitude values
latitude_element = driver.find_element(By.ID, "latitude")
longitude_element = driver.find_element(By.ID, "longitude")

latitude = latitude_element.text.split(":")[-1].strip()
longitude = longitude_element.text.split(":")[-1].strip()

print("Latitude:", latitude)
print("Longitude:", longitude)

# Close the browser
driver.quit()
