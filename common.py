import time
import tkinter as tk
from tkinter import messagebox

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading

# -------------------------
# PRESENTATION SETTINGS
# -------------------------

TYPE_DELAY = 0
STEP_DELAY = 0.5
PAGE_DELAY = 0.5


def slow_type(element, text, delay=TYPE_DELAY):
    for character in text:
        element.send_keys(character)
        time.sleep(delay)


def pause(seconds=STEP_DELAY):
    time.sleep(seconds)

# -------------------------
# UI LOGGING
# -------------------------

log_callback = None


def set_log_callback(callback):
    global log_callback
    log_callback = callback


def log(message=""):
    print(message)

    if log_callback:
        log_callback(message)

# -------------------------
# BROWSER SETUP
# -------------------------

def create_driver():
    options = webdriver.ChromeOptions()

    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }
    )

    options.add_argument(
        "--disable-features=PasswordLeakDetection"
    )

    return webdriver.Chrome(options=options)


def create_wait(driver):
    return WebDriverWait(driver, 10)


# -------------------------
# TEST RESULTS
# -------------------------

def pass_test(results, test_name):
    results.append(
        {
            "name": test_name,
            "passed": True,
            "reason": ""
        }
    )

    log(f"PASS - {test_name}")


def fail_test(results, test_name, reason):
    results.append(
        {
            "name": test_name,
            "passed": False,
            "reason": str(reason)
        }
    )

    log(f"FAIL - {test_name}")
    log(f"Reason: {reason}")


# -------------------------
# LOGIN HELPER
# -------------------------

def login(driver, wait):
    driver.get("https://www.saucedemo.com/")

    pause(PAGE_DELAY)

    username = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "user-name")
        )
    )

    password = driver.find_element(
        By.ID,
        "password"
    )

    slow_type(username, "standard_user")
    slow_type(password, "secret_sauce")

    pause()

    driver.find_element(
        By.ID,
        "login-button"
    ).click()

    wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_list")
        )
    )

    pause(PAGE_DELAY)


# -------------------------
# BUILD RESULT TEXT
# -------------------------

def build_report(results, suite_name):
    passed = sum(
        1 for result in results
        if result["passed"]
    )

    failed = sum(
        1 for result in results
        if not result["passed"]
    )

    report = f"{suite_name}\n"
    report += "=" * len(suite_name)
    report += "\n\n"

    for result in results:

        if result["passed"]:
            report += f"PASS - {result['name']}\n"

        else:
            report += f"FAIL - {result['name']}\n"
            report += f"Reason: {result['reason']}\n"

    report += "\n"
    report += f"Passed: {passed}\n"
    report += f"Failed: {failed}\n"

    return report


# -------------------------
# INDIVIDUAL TEST POPUP
# -------------------------

def show_results(results, suite_name):
    report = build_report(
        results,
        suite_name
    )

    failed = sum(
        1 for result in results
        if not result["passed"]
    )

    root = tk.Tk()
    root.withdraw()

    if failed == 0:
        messagebox.showinfo(
            suite_name,
            report
        )
    else:
        messagebox.showerror(
            suite_name,
            report
        )

    root.destroy()


# -------------------------
# COPYABLE COMPLETE REPORT
# -------------------------

def show_full_report(report):
    window = tk.Toplevel()

    window.title(
        "SauceDemo Complete Test Results"
    )

    window.geometry(
        "750x600"
    )

    title = tk.Label(
        window,
        text="SauceDemo Complete Test Results",
        font=("Arial", 14, "bold")
    )

    title.pack(
        pady=10
    )

    text_box = tk.Text(
        window,
        wrap="word",
        font=("Consolas", 10)
    )

    text_box.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    text_box.insert(
        "1.0",
        report
    )

    # Leave the text selectable/copyable.
    # Users can Ctrl+A and Ctrl+C.

    close_button = tk.Button(
        window,
        text="Close",
        command=window.destroy
    )

    close_button.pack(
        pady=10
    )