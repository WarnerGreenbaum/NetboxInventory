Program README

This program is designed to automate the process of creating new devices in a web application using Selenium and Pandas libraries in Python.
Prerequisites

Before running the program, ensure that you have the following modules installed:

    -Python
    -Pandas library
    -Selenium library
    -Firefox browser (or any other browser supported by Selenium)

Installation

    Clone or download the program files to your local machine.
    Install the required libraries by running the following command:

    pip install pandas selenium

    Make sure you have the latest version of the Firefox browser installed on your machine.

Usage

    Prepare the input data:
        Create a CSV file named 'MacAndSerial.csv' in the 'netbox_inputs' folder.
        Enter the MAC addresses in the 'MAC' column and the corresponding serial numbers in the 'SERIAL' column.
        Save the file.

    Configure your login and device information:
        Open the Python file in a text editor.
        Replace the placeholders in the following lines with your actual login credentials and device information:

        makefile

    your_username = "ENTER USERNAME HERE"
    your_password = "ENTER PASSWORD HERE"
    your_po_number = "ENTER PO NUMBER HERE"
    your_example_device_link = "YOUR EXAMPLE DEVICE LINK HERE"

Run the program:

    Open a terminal or command prompt.
    Navigate to the directory where the program files are located.
    Execute the following command:

        python csvTesting.py

    Sit back and relax:
        The program will automate the process of creating new devices in the specified web application using the provided data.
        It will log in to the application, clone the example device, fill in the necessary details (including the purchase order number and device information from the CSV file), and create the device.
        The process will be repeated for each entry in the CSV file.

Notes

    -Make sure to replace the placeholder values in the program with your actual login credentials, device information, and CSV file path before running the program.
    -Ensure that the web application's structure and element identifiers match those used in the program. If not, modify the XPath and element IDs accordingly.
    -You can modify the program to work with different web applications by adapting the element locators and actions to match the target application's user interface.

Disclaimer

    This program is provided as-is without any warranty. Use it at your own risk.
    The program may require adjustments to work with specific web applications and may break if the application's structure or user interface changes.
