# SauceDemo QA Automation TEST

A Python and Selenium test automation project built around the SauceDemo website.

The project provides a simple desktop interface for launching automated QA test suites, viewing live execution logs, and reviewing PASS/FAIL results.

## Features

* Tkinter desktop test runner
* Selenium WebDriver browser automation
* Live execution logging
* PASS/FAIL reporting
* Threaded test execution so the UI remains responsive
* Explicit waits for dynamic page elements
* Human-readable failure messages

## Automated Test Suites

### Login Tests

Tests authentication behavior including:

* Valid login
* Invalid password rejection
* Locked-out user rejection
* Application error reporting when login fails

### Cart Tests

Tests shopping cart behavior including:

* Adding a product to the cart
* Verifying the cart item count
* Opening the shopping cart
* Verifying the selected product
* Removing the product
* Verifying that the cart is empty

### Checkout Tests

Tests checkout validation and successful purchases including:

* Missing first name validation
* Missing last name validation
* Missing ZIP/postal code validation
* Successful checkout
* Confirmation message verification

### Sorting Tests

Tests product sorting including:

* Name: A to Z
* Name: Z to A
* Price: Low to High
* Price: High to Low

## Technologies Used

* Python
* Selenium WebDriver
* Tkinter
* Chrome
* PyInstaller

## Project Structure

```text
SeleniumTestProject/
├── main.py
├── common.py
├── test_login.py
├── test_cart.py
├── test_checkout.py
├── test_sorting.py
├── requirements.txt
└── README.md
```

## Installation

Python and Google Chrome are required.

Install the project dependencies with:

```bash
pip install -r requirements.txt
```

If a `requirements.txt` file is not being used, Selenium can be installed directly with:

```bash
pip install selenium
```

## Running the Application

Run the application with:

```bash
python main.py
```

The desktop interface allows individual test suites to be launched or all tests to be run sequentially.

## Running All Tests

Select **Run All Tests** from the application.

The application will run:

1. Login tests
2. Cart tests
3. Checkout tests
4. Sorting tests

A complete report is displayed when execution finishes.

## Executable Version

The project can also be packaged as a Windows executable using PyInstaller.

Install PyInstaller:

```bash
pip install pyinstaller
```

Build the executable with Selenium dependencies included:

```bash
pyinstaller --clean --onefile --windowed --name SauceDemoQA --collect-all selenium main.py
```

The finished executable will be created in:

```text
dist/SauceDemoQA.exe
```

Google Chrome and internet access are still required for the Selenium tests to run.

## Purpose

This project was created as a hands-on exercise in QA test automation, including test-case design, Selenium browser interaction, error handling, reporting, GUI development, and packaging a Python application for Windows.
