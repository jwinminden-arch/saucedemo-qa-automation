import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from common import (
    create_driver,
    create_wait,
    login,
    slow_type,
    pause,
    pass_test,
    fail_test,
    log
)


def get_to_checkout(driver, wait):

    log("Logging into SauceDemo...")
    login(driver, wait)
    log("Login successful.")

    log("Adding backpack to cart...")

    wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "add-to-cart-sauce-labs-backpack"
            )
        )
    ).click()

    log("Opening shopping cart...")

    wait.until(
        EC.element_to_be_clickable(
            (
                By.CLASS_NAME,
                "shopping_cart_link"
            )
        )
    ).click()

    log("Opening checkout...")

    wait.until(
        EC.element_to_be_clickable(
            (
                By.ID,
                "checkout"
            )
        )
    ).click()


def run_checkout_tests(result_callback=None):

    results = []

    log("")
    log("Starting Checkout Test Suite")
    log("=" * 40)


    # =====================================================
    # TEST 1 - MISSING FIRST NAME
    # =====================================================

    driver = create_driver()
    wait = create_wait(driver)

    try:
        log("")
        log("TEST: Missing First Name")
        log("Preparing checkout...")

        get_to_checkout(
            driver,
            wait
        )

        log("Entering last name...")

        slow_type(
            driver.find_element(
                By.ID,
                "last-name"
            ),
            "Smith"
        )

        log("Entering ZIP code...")

        slow_type(
            driver.find_element(
                By.ID,
                "postal-code"
            ),
            "71111"
        )

        log("Leaving first name blank.")
        log("Clicking Continue...")

        driver.find_element(
            By.ID,
            "continue"
        ).click()

        log("Waiting for validation message...")

        error = wait.until(
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "[data-test='error']"
                )
            )
        )

        expected_message = "First Name is required"
        actual_message = error.text

        log(
            f"Expected error: {expected_message}"
        )

        log(
            f"Actual error: {actual_message}"
        )

        if expected_message in actual_message:

            pass_test(
                results,
                "Missing First Name Validation"
            )

        else:

            fail_test(
                results,
                "Missing First Name Validation",
                f"Expected an error containing "
                f"'{expected_message}', "
                f"but found '{actual_message}'."
            )

    except TimeoutException:
        fail_test(
            results,
            "Missing First Name Validation",
            "Expected first-name validation message "
            "did not appear within 10 seconds."
        )

    except Exception as error:
        fail_test(
            results,
            "Missing First Name Validation",
            f"Unexpected error during test: {error}"
        )

    finally:
        log("Closing browser for Missing First Name test...")
        driver.quit()


    # =====================================================
    # TEST 2 - MISSING LAST NAME
    # =====================================================

    driver = create_driver()
    wait = create_wait(driver)

    try:
        log("")
        log("TEST: Missing Last Name")
        log("Preparing checkout...")

        get_to_checkout(
            driver,
            wait
        )

        log("Entering first name...")

        slow_type(
            driver.find_element(
                By.ID,
                "first-name"
            ),
            "John"
        )

        log("Entering ZIP code...")

        slow_type(
            driver.find_element(
                By.ID,
                "postal-code"
            ),
            "71111"
        )

        log("Leaving last name blank.")
        log("Clicking Continue...")

        driver.find_element(
            By.ID,
            "continue"
        ).click()

        log("Waiting for validation message...")

        error = wait.until(
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "[data-test='error']"
                )
            )
        )

        expected_message = "Last Name is required"
        actual_message = error.text

        log(
            f"Expected error: {expected_message}"
        )

        log(
            f"Actual error: {actual_message}"
        )

        if expected_message in actual_message:

            pass_test(
                results,
                "Missing Last Name Validation"
            )

        else:

            fail_test(
                results,
                "Missing Last Name Validation",
                f"Expected an error containing "
                f"'{expected_message}', "
                f"but found '{actual_message}'."
            )

    except TimeoutException:
        fail_test(
            results,
            "Missing Last Name Validation",
            "Expected last-name validation message "
            "did not appear within 10 seconds."
        )

    except Exception as error:
        fail_test(
            results,
            "Missing Last Name Validation",
            f"Unexpected error during test: {error}"
        )

    finally:
        log("Closing browser for Missing Last Name test...")
        driver.quit()


    # =====================================================
    # TEST 3 - MISSING ZIP
    # =====================================================

    driver = create_driver()
    wait = create_wait(driver)

    try:
        log("")
        log("TEST: Missing ZIP Code")
        log("Preparing checkout...")

        get_to_checkout(
            driver,
            wait
        )

        log("Entering first name...")

        slow_type(
            driver.find_element(
                By.ID,
                "first-name"
            ),
            "John"
        )

        log("Entering last name...")

        slow_type(
            driver.find_element(
                By.ID,
                "last-name"
            ),
            "Smith"
        )

        log("Leaving ZIP code blank.")
        log("Clicking Continue...")

        driver.find_element(
            By.ID,
            "continue"
        ).click()

        log("Waiting for validation message...")

        error = wait.until(
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "[data-test='error']"
                )
            )
        )

        expected_message = "Postal Code is required"
        actual_message = error.text

        log(
            f"Expected error: {expected_message}"
        )

        log(
            f"Actual error: {actual_message}"
        )

        if expected_message in actual_message:

            pass_test(
                results,
                "Missing ZIP Validation"
            )

        else:

            fail_test(
                results,
                "Missing ZIP Validation",
                f"Expected an error containing "
                f"'{expected_message}', "
                f"but found '{actual_message}'."
            )

    except TimeoutException:
        fail_test(
            results,
            "Missing ZIP Validation",
            "Expected ZIP-code validation message "
            "did not appear within 10 seconds."
        )

    except Exception as error:
        fail_test(
            results,
            "Missing ZIP Validation",
            f"Unexpected error during test: {error}"
        )

    finally:
        log("Closing browser for Missing ZIP test...")
        driver.quit()


    # =====================================================
    # TEST 4 - SUCCESSFUL CHECKOUT
    # =====================================================

    driver = create_driver()
    wait = create_wait(driver)

    try:
        log("")
        log("TEST: Successful Checkout")
        log("Preparing checkout...")

        get_to_checkout(
            driver,
            wait
        )

        random_zip = str(
            random.randint(
                10000,
                99999
            )
        )

        log("Entering first name: John")

        slow_type(
            driver.find_element(
                By.ID,
                "first-name"
            ),
            "John"
        )

        log("Entering last name: Smith")

        slow_type(
            driver.find_element(
                By.ID,
                "last-name"
            ),
            "Smith"
        )

        log(
            f"Entering ZIP code: {random_zip}"
        )

        slow_type(
            driver.find_element(
                By.ID,
                "postal-code"
            ),
            random_zip
        )

        pause()

        log("Clicking Continue...")

        wait.until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    "continue"
                )
            )
        ).click()

        log("Waiting for Finish button...")

        finish_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    "finish"
                )
            )
        )

        log("Finish button found.")
        log("Clicking Finish...")

        finish_button.click()

        log("Waiting for confirmation message...")

        confirmation = wait.until(
            EC.visibility_of_element_located(
                (
                    By.CLASS_NAME,
                    "complete-header"
                )
            )
        )

        expected = "Thank you for your order!"
        actual = confirmation.text

        log(
            f"Expected confirmation: {expected}"
        )

        log(
            f"Actual confirmation: {actual}"
        )

        if actual == expected:

            pass_test(
                results,
                "Successful Checkout"
            )

        else:

            fail_test(
                results,
                "Successful Checkout",
                f"Expected '{expected}', "
                f"but found '{actual}'."
            )

    except TimeoutException:
        fail_test(
            results,
            "Successful Checkout",
            "A required checkout element or "
            "confirmation message did not appear "
            "within 10 seconds."
        )

    except Exception as error:
        fail_test(
            results,
            "Successful Checkout",
            f"Unexpected error during checkout: {error}"
        )

    finally:
        log("Closing browser for Successful Checkout test...")
        driver.quit()


    # =====================================================
    # SUMMARY
    # =====================================================

    passed = sum(
        1 for result in results
        if result["passed"]
    )

    failed = sum(
        1 for result in results
        if not result["passed"]
    )

    log("")
    log("=" * 40)
    log("Checkout Test Suite Complete")
    log(f"Passed: {passed}")
    log(f"Failed: {failed}")
    log(f"Total: {len(results)}")


    # -------------------------
    # SEND RESULTS TO UI
    # -------------------------

    if result_callback is not None:
        result_callback(
            results,
            "Checkout Test Results"
        )

    return results