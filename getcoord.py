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

# Update the text file with the new latitude and longitude
with open('C:/Users/dheer/Documents/MissionPlanner/test - Copy - Copy.waypoints', 'r') as file:
    lines = file.readlines()

lines[2] = f"3\t0\t3\t20\t0.00000000\t0.00000000\t0.00000000\t0.00000000\t{latitude}\t{longitude}\t0.000000\t1\n"

with open('C:/Users/dheer/Documents/MissionPlanner/test - Copy - Copy.waypoints', 'w') as file:
    file.writelines(lines)

# Close the browser
driver.quit()
