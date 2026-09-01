from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from common import (
    create_driver,
    create_wait,
    login,
    pause,
    pass_test,
    fail_test,
    show_results
)


def run_cart_tests(show_popup=True):

    results = []

    driver = create_driver()
    wait = create_wait(driver)

    try:
        login(driver, wait)

        # -------------------------
        # ADD BACKPACK
        # -------------------------

        try:
            print("\nAdding backpack...")

            wait.until(
                EC.element_to_be_clickable(
                    (
                        By.ID,
                        "add-to-cart-sauce-labs-backpack"
                    )
                )
            ).click()

            pause()

            pass_test(
                results,
                "Add Backpack"
            )

        except Exception as error:
            fail_test(
                results,
                "Add Backpack",
                error
            )


        # -------------------------
        # VERIFY CART COUNT
        # -------------------------

        try:
            cart_badge = wait.until(
                EC.visibility_of_element_located(
                    (
                        By.CLASS_NAME,
                        "shopping_cart_badge"
                    )
                )
            )

            actual_count = cart_badge.text

            if actual_count == "2":

                pass_test(
                    results,
                    "Cart Count"
                )

            else:

                fail_test(
                    results,
                    "Cart Count",
                    f"Expected 2 item, found {actual_count}."
                )

        except Exception as error:
            fail_test(
                results,
                "Cart Count",
                error
            )


        # -------------------------
        # OPEN CART
        # -------------------------

        try:
            wait.until(
                EC.element_to_be_clickable(
                    (
                        By.CLASS_NAME,
                        "shopping_cart_link"
                    )
                )
            ).click()

            pause()

            backpack = wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//*[normalize-space()='Sauce Labs Backpack']"
                    )
                )
            )

            if backpack.is_displayed():

                pass_test(
                    results,
                    "Backpack Present in Cart"
                )

            else:

                fail_test(
                    results,
                    "Backpack Present in Cart",
                    "Backpack was not visible."
                )

        except Exception as error:
            fail_test(
                results,
                "Backpack Present in Cart",
                error
            )


        # -------------------------
        # REMOVE BACKPACK
        # -------------------------

        try:
            remove_button = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.ID,
                        "remove-sauce-labs-backpack"
                    )
                )
            )

            remove_button.click()

            pause()

            pass_test(
                results,
                "Remove Backpack"
            )

        except Exception as error:
            fail_test(
                results,
                "Remove Backpack",
                error
            )


        # -------------------------
        # VERIFY CART EMPTY
        # -------------------------

        try:
            badges = driver.find_elements(
                By.CLASS_NAME,
                "shopping_cart_badge"
            )

            if len(badges) == 0:

                pass_test(
                    results,
                    "Cart Empty"
                )

            else:

                fail_test(
                    results,
                    "Cart Empty",
                    "Cart badge still appears after removing item."
                )

        except Exception as error:
            fail_test(
                results,
                "Cart Empty",
                error
            )

    finally:
        driver.quit()

    if show_popup:
        show_results(
        results,
        "Cart Test Results"
    )

    return results