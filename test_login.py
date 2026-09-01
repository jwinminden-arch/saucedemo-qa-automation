from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from common import (
    create_driver,
    create_wait,
    slow_type,
    pause,
    pass_test,
    fail_test,
    log
)


def wait_for_login_result(driver):
    """
    After clicking Login, check for either:
    1. Successful login / inventory page
    2. Login error message

    Returning False tells WebDriverWait
    to keep waiting.
    """

    inventory = driver.find_elements(
        By.CLASS_NAME,
        "inventory_list"
    )

    if inventory:
        return (
            "success",
            inventory[0]
        )

    errors = driver.find_elements(
        By.CSS_SELECTOR,
        "[data-test='error']"
    )

    if errors:
        return (
            "error",
            errors[0]
        )

    return False


def run_login_tests(result_callback=None):

    results = []

    log("")
    log("Starting Login Test Suite")
    log("=" * 40)


    # =====================================================
    # TEST 1 - VALID LOGIN
    # =====================================================

    driver = create_driver()
    wait = create_wait(driver)

    try:
        log("")
        log("TEST: Valid Login")
        log("Opening SauceDemo...")

        driver.get(
            "https://www.saucedemo.com/"
        )

        log("Looking for username field...")

        username = wait.until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    "user-name"
                )
            )
        )

        log("Username field found.")

        log("Looking for password field...")

        password = wait.until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    "password"
                )
            )
        )

        log("Password field found.")

        log(
            "Entering username: standard_user"
        )

        slow_type(
            username,
            "standard_user"
        )

        log("Entering password...")

  
        slow_type(
            password,
            "secret_sauce"
        )

        pause()

        log("Looking for Login button...")

        login_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    "login-button"
                )
            )
        )

        log("Login button found.")
        log("Clicking Login...")

        login_button.click()

        log(
            "Waiting for login result..."
        )

        # Wait for EITHER successful login
        # OR an application error message.
        result_type, element = wait.until(
            wait_for_login_result
        )

        if result_type == "success":

            log(
                "Inventory page loaded."
            )

            pass_test(
                results,
                "Valid Login"
            )

        elif result_type == "error":

            actual_error = element.text

            log(
                f"Login error received: {actual_error}"
            )

            fail_test(
                results,
                "Valid Login",
                f"Login was rejected by the application. "
                f"Error message: {actual_error}"
            )

    except TimeoutException:

        fail_test(
            results,
            "Valid Login",
            "Neither the inventory page nor a login "
            "error message appeared within 10 seconds."
        )

    except Exception as error:

        fail_test(
            results,
            "Valid Login",
            f"Unexpected error during valid login test: {error}"
        )

    finally:

        log(
            "Closing browser for Valid Login test..."
        )

        driver.quit()


    # =====================================================
    # TEST 2 - INVALID PASSWORD
    # =====================================================

    driver = create_driver()
    wait = create_wait(driver)

    try:
        log("")
        log("TEST: Invalid Password")
        log("Opening SauceDemo...")

        driver.get(
            "https://www.saucedemo.com/"
        )

        username = wait.until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    "user-name"
                )
            )
        )

        password = wait.until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    "password"
                )
            )
        )

        log(
            "Entering username: standard_user"
        )

        slow_type(
            username,
            "standard_user"
        )

        log(
            "Entering intentionally incorrect password."
        )

        slow_type(
            password,
            "wrong_password"
        )

        log("Clicking Login...")

        wait.until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    "login-button"
                )
            )
        ).click()

        log(
            "Waiting for login error message..."
        )

        error_message = wait.until(
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "[data-test='error']"
                )
            )
        )

        expected_message = (
            "Username and password do not match"
        )

        actual_message = (
            error_message.text
        )

        log(
            f"Expected error: {expected_message}"
        )

        log(
            f"Actual error: {actual_message}"
        )

        if expected_message in actual_message:

            pass_test(
                results,
                "Invalid Password Rejected"
            )

        else:

            fail_test(
                results,
                "Invalid Password Rejected",
                f"Expected an error containing "
                f"'{expected_message}', "
                f"but found '{actual_message}'."
            )

    except TimeoutException:

        fail_test(
            results,
            "Invalid Password Rejected",
            "Expected invalid-password error message "
            "did not appear within 10 seconds."
        )

    except Exception as error:

        fail_test(
            results,
            "Invalid Password Rejected",
            f"Unexpected error during "
            f"invalid-password test: {error}"
        )

    finally:

        log(
            "Closing browser for Invalid Password test..."
        )

        driver.quit()


    # =====================================================
    # TEST 3 - LOCKED OUT USER
    # =====================================================

    driver = create_driver()
    wait = create_wait(driver)

    try:
        log("")
        log("TEST: Locked Out User")
        log("Opening SauceDemo...")

        driver.get(
            "https://www.saucedemo.com/"
        )

        username = wait.until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    "user-name"
                )
            )
        )

        password = wait.until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    "password"
                )
            )
        )

        log(
            "Entering username: locked_out_user"
        )

        slow_type(
            username,
            "locked_out_user"
        )

        log(
            "Entering password..."
        )

        slow_type(
            password,
            "secret_sauce"
        )

        log(
            "Clicking Login..."
        )

        wait.until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    "login-button"
                )
            )
        ).click()

        log(
            "Waiting for locked-out error message..."
        )

        error_message = wait.until(
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "[data-test='error']"
                )
            )
        )

        actual_message = (
            error_message.text
        )

        log(
            f"Actual error: {actual_message}"
        )

        if "locked out" in actual_message.lower():

            pass_test(
                results,
                "Locked Out User Rejected"
            )

        else:

            fail_test(
                results,
                "Locked Out User Rejected",
                f"Expected a locked-out message, "
                f"but found '{actual_message}'."
            )

    except TimeoutException:

        fail_test(
            results,
            "Locked Out User Rejected",
            "Expected locked-out-user error message "
            "did not appear within 10 seconds."
        )

    except Exception as error:

        fail_test(
            results,
            "Locked Out User Rejected",
            f"Unexpected error during "
            f"locked-out-user test: {error}"
        )

    finally:

        log(
            "Closing browser for Locked Out User test..."
        )

        driver.quit()


    # =====================================================
    # SUMMARY
    # =====================================================

    passed = sum(
        1
        for result in results
        if result["passed"]
    )

    failed = sum(
        1
        for result in results
        if not result["passed"]
    )

    log("")
    log("=" * 40)
    log("Login Test Suite Complete")
    log(f"Passed: {passed}")
    log(f"Failed: {failed}")
    log(f"Total: {len(results)}")


    # -------------------------
    # SEND RESULTS TO UI
    # -------------------------

    if result_callback is not None:

        result_callback(
            results,
            "Login Test Results"
        )

    return results