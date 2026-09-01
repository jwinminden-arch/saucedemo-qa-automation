from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from common import (
    create_driver,
    create_wait,
    login,
    pause,
    pass_test,
    fail_test,
    log
)


def run_cart_tests(result_callback=None):

    results = []

    driver = create_driver()
    wait = create_wait(driver)

    try:
        # =====================================================
        # LOGIN
        # =====================================================

        log("")
        log("Starting Cart Test Suite")
        log("=" * 40)

        log("Logging into SauceDemo...")

        try:
            login(driver, wait)

            log("Login successful.")

        except TimeoutException:
            fail_test(
                results,
                "Login",
                "Login page or inventory page did not load within 10 seconds."
            )

        except Exception as error:
            fail_test(
                results,
                "Login",
                f"Unexpected error during login: {error}"
            )


        # =====================================================
        # ADD BACKPACK
        # =====================================================

        log("")
        log("TEST: Add Backpack")
        log("Looking for Add to Cart button...")

        try:
            add_button = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.ID,
                        "add-to-cart-sauce-labs-backpack"
                    )
                )
            )

            log("Add to Cart button found.")
            log("Clicking Add to Cart...")

            add_button.click()

            pause()

            pass_test(
                results,
                "Add Backpack"
            )

        except TimeoutException:
            fail_test(
                results,
                "Add Backpack",
                "Add to Cart button was not found or "
                "was not clickable within 10 seconds."
            )

        except Exception as error:
            fail_test(
                results,
                "Add Backpack",
                f"Unexpected error while attempting "
                f"to add backpack: {error}"
            )


        # =====================================================
        # VERIFY CART COUNT
        # =====================================================

        log("")
        log("TEST: Cart Count")
        log("Looking for shopping cart badge...")

        try:
            cart_badge = wait.until(
                EC.visibility_of_element_located(
                    (
                        By.CLASS_NAME,
                        "shopping_cart_badge"
                    )
                )
            )

            log("Shopping cart badge found.")

            actual_count = cart_badge.text
            expected_count = "2"

            log(f"Expected cart count: {expected_count}")
            log(f"Actual cart count: {actual_count}")

            if actual_count == expected_count:

                pass_test(
                    results,
                    "Cart Count"
                )

            else:

                fail_test(
                    results,
                    "Cart Count",
                    f"Expected {expected_count} item, "
                    f"but found {actual_count}."
                )

        except TimeoutException:
            fail_test(
                results,
                "Cart Count",
                "Shopping cart badge did not appear "
                "within 10 seconds."
            )

        except Exception as error:
            fail_test(
                results,
                "Cart Count",
                f"Unexpected error while checking "
                f"cart count: {error}"
            )


        # =====================================================
        # OPEN CART
        # =====================================================

        log("")
        log("TEST: Open Cart")
        log("Looking for shopping cart link...")

        try:
            cart_link = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.CLASS_NAME,
                        "shopping_cart_link"
                    )
                )
            )

            log("Shopping cart link found.")
            log("Opening shopping cart...")

            cart_link.click()

            pause()

            pass_test(
                results,
                "Open Cart"
            )

        except TimeoutException:
            fail_test(
                results,
                "Open Cart",
                "Shopping cart link was not found or "
                "was not clickable within 10 seconds."
            )

        except Exception as error:
            fail_test(
                results,
                "Open Cart",
                f"Unexpected error while opening "
                f"cart: {error}"
            )


        # =====================================================
        # VERIFY BACKPACK IN CART
        # =====================================================

        log("")
        log("TEST: Backpack Present in Cart")
        log("Looking for Sauce Labs Backpack in cart...")

        try:
            backpack = wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//*[normalize-space()='Sauce Labs Backpack']"
                    )
                )
            )

            log("Backpack element found.")

            if backpack.is_displayed():

                pass_test(
                    results,
                    "Backpack Present in Cart"
                )

            else:

                fail_test(
                    results,
                    "Backpack Present in Cart",
                    "Backpack element was found, "
                    "but it was not visible."
                )

        except TimeoutException:
            fail_test(
                results,
                "Backpack Present in Cart",
                "Sauce Labs Backpack did not appear "
                "in the cart within 10 seconds."
            )

        except Exception as error:
            fail_test(
                results,
                "Backpack Present in Cart",
                f"Unexpected error while checking "
                f"for backpack: {error}"
            )


        # =====================================================
        # REMOVE BACKPACK
        # =====================================================

        log("")
        log("TEST: Remove Backpack")
        log("Looking for Remove Backpack button...")

        try:
            remove_button = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.ID,
                        "remove-sauce-labs-backpack"
                    )
                )
            )

            log("Remove Backpack button found.")
            log("Clicking Remove...")

            remove_button.click()

            pause()

            pass_test(
                results,
                "Remove Backpack"
            )

        except TimeoutException:
            fail_test(
                results,
                "Remove Backpack",
                "Remove Backpack button was not found "
                "or was not clickable within 10 seconds."
            )

        except Exception as error:
            fail_test(
                results,
                "Remove Backpack",
                f"Unexpected error while attempting "
                f"to remove backpack: {error}"
            )


        # =====================================================
        # VERIFY CART EMPTY
        # =====================================================

        log("")
        log("TEST: Cart Empty")
        log("Checking whether shopping cart badge remains...")

        try:
            badges = driver.find_elements(
                By.CLASS_NAME,
                "shopping_cart_badge"
            )

            log(f"Cart badges found: {len(badges)}")

            if len(badges) == 0:

                pass_test(
                    results,
                    "Cart Empty"
                )

            else:

                fail_test(
                    results,
                    "Cart Empty",
                    "Cart badge still appears after "
                    "removing the item."
                )

        except Exception as error:
            fail_test(
                results,
                "Cart Empty",
                f"Unexpected error while checking "
                f"whether cart was empty: {error}"
            )


        # =====================================================
        # SUMMARY
        # =====================================================

        log("")
        log("=" * 40)
        log("Cart Test Suite Complete")

        passed = sum(
            1 for result in results
            if result["passed"]
        )

        failed = sum(
            1 for result in results
            if not result["passed"]
        )

        log(f"Passed: {passed}")
        log(f"Failed: {failed}")
        log(f"Total: {len(results)}")

    finally:
        log("")
        log("Closing Chrome...")
        driver.quit()


    # -------------------------
    # SEND RESULTS BACK TO UI
    # -------------------------

    if result_callback is not None:
        result_callback(
            results,
            "Cart Test Results"
        )

    return results