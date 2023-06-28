from pandas import * 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Read the input data from csv file
data = read_csv('netbox_inputs/MacAndSerial.csv')


# Get the mac addresses and serial numbers into lists
mac_addresses = data['MAC'].to_list()
serial_no = data['SERIAL'].to_list()


# Get the number of devices
y = len(mac_addresses)


# -----ENTER YOUR LOGIN AND DEVICE BELOW-----
your_username = "ENTER USERNAME HERE"
your_password = "ENTER PASSWORD HERE"
# ---------------------------------------------


# ------ENTER DEVICE AND PO INFO HERE------
your_po_number = "ENTER PO NUMBER HERE"
your_example_device_link = "YOUR EXAMPLE DEVICE LINK HERE"
# ------------------------------------------


# Initialize the webdriver
driver = webdriver.Firefox()


# Open the device link
driver.get(your_example_device_link)


# Locate the username, password, and login button elements on the page
Username = driver.find_element(By.ID, 'id_username')
Password = driver.find_element(By.ID, 'id_password')
Login = driver.find_element(By.XPATH, '/html/body/main/div[2]/form/button')

# Enter the username and password
Username.send_keys(your_username)
Password.send_keys(your_password)


# Click the login button
Login.click()


# Loop through the number of devices
for x in range(int(y)):
    # Locate the clone button and click it
    clone = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[4]/div[2]/div[1]/a[1]')
    clone.click()

    # Enter the purchase order number
    po_number_input = driver.find_element(By.ID, 'id_cf_Purchase Order Number')
    po_number_input.send_keys(your_po_number)

    # Locate and fill in the device name, serial number, and comments
    dev_name = driver.find_element(By.ID,'id_name')
    dev_serial = driver.find_element(By.ID, 'id_serial')
    dev_comments = driver.find_element(By.ID, 'id_comments')
    dev_comments.send_keys("Mac address: " + mac_addresses[x])
    dev_name.send_keys(serial_no[x])
    dev_serial.send_keys(serial_no[x])

    # Locate the create button and click it
    create = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[4]/div/div/form/div[11]/button[1]')
    create.click()



