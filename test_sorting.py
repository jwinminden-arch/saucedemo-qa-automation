from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException
)

from common import (
    create_driver,
    create_wait,
    login,
    pause,
    pass_test,
    fail_test,
    log
)


# -------------------------
# GET PRODUCT NAMES
# -------------------------

def get_product_names(driver):

    elements = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item_name"
    )

    return [
        element.text
        for element in elements
    ]


# -------------------------
# GET PRODUCT PRICES
# -------------------------

def get_product_prices(driver):

    elements = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item_price"
    )

    prices = []

    for element in elements:

        price_text = element.text.replace(
            "$",
            ""
        )

        prices.append(
            float(price_text)
        )

    return prices


# -------------------------
# SELECT SORT OPTION
# -------------------------

def select_sort(driver, wait, sort_value):

    log(
        f"Looking for sort dropdown "
        f"with option '{sort_value}'..."
    )

    dropdown_element = wait.until(
        EC.element_to_be_clickable(
            (
                By.CLASS_NAME,
                "product_sort_container"
            )
        )
    )

    log("Sort dropdown found.")

    dropdown = Select(
        dropdown_element
    )

    log(
        f"Selecting sort option: {sort_value}"
    )

    dropdown.select_by_value(
        sort_value
    )

    pause()


# -------------------------
# MAIN SORTING TEST SUITE
# -------------------------

def run_sorting_tests(result_callback=None):

    results = []

    driver = create_driver()
    wait = create_wait(driver)

    try:

        log("")
        log("Starting Sorting Test Suite")
        log("=" * 40)

        # -------------------------
        # LOGIN
        # -------------------------

        log("Logging into SauceDemo...")

        try:
            login(
                driver,
                wait
            )

            log("Login successful.")

        except TimeoutException:
            fail_test(
                results,
                "Login",
                "Login page or inventory page "
                "did not load within 10 seconds."
            )

        except Exception as error:
            fail_test(
                results,
                "Login",
                f"Unexpected error during login: {error}"
            )


        # =================================================
        # TEST 1 - SORT A-Z
        # =================================================

        try:

            log("")
            log("TEST: Sort A-Z")

            select_sort(
                driver,
                wait,
                "az"
            )

            log(
                "Reading product names..."
            )

            actual = get_product_names(
                driver
            )

            expected = sorted(
                actual
            )

            log(
                f"Actual order: {actual}"
            )

            log(
                f"Expected order: {expected}"
            )

            if actual == expected:

                pass_test(
                    results,
                    "Sort A-Z"
                )

            else:

                fail_test(
                    results,
                    "Sort A-Z",
                    f"Expected {expected}, "
                    f"but found {actual}."
                )

        except TimeoutException:
            fail_test(
                results,
                "Sort A-Z",
                "Sort dropdown was not found or "
                "was not clickable within 10 seconds."
            )

        except StaleElementReferenceException:
            fail_test(
                results,
                "Sort A-Z",
                "A page element became stale while "
                "checking alphabetical sorting."
            )

        except Exception as error:
            fail_test(
                results,
                "Sort A-Z",
                f"Unexpected error during A-Z sort test: {error}"
            )


        # =================================================
        # TEST 2 - SORT Z-A
        # =================================================

        try:

            log("")
            log("TEST: Sort Z-A")

            select_sort(
                driver,
                wait,
                "za"
            )

            log(
                "Reading product names..."
            )

            actual = get_product_names(
                driver
            )

            expected = sorted(
                actual,
                reverse=True
            )

            log(
                f"Actual order: {actual}"
            )

            log(
                f"Expected order: {expected}"
            )

            if actual == expected:

                pass_test(
                    results,
                    "Sort Z-A"
                )

            else:

                fail_test(
                    results,
                    "Sort Z-A",
                    f"Expected {expected}, "
                    f"but found {actual}."
                )

        except TimeoutException:
            fail_test(
                results,
                "Sort Z-A",
                "Sort dropdown was not found or "
                "was not clickable within 10 seconds."
            )

        except StaleElementReferenceException:
            fail_test(
                results,
                "Sort Z-A",
                "A page element became stale while "
                "checking reverse alphabetical sorting."
            )

        except Exception as error:
            fail_test(
                results,
                "Sort Z-A",
                f"Unexpected error during Z-A sort test: {error}"
            )


        # =================================================
        # TEST 3 - PRICE LOW TO HIGH
        # =================================================

        try:

            log("")
            log("TEST: Price Low to High")

            select_sort(
                driver,
                wait,
                "lohi"
            )

            log(
                "Reading product prices..."
            )

            actual = get_product_prices(
                driver
            )

            expected = sorted(
                actual
            )

            log(
                f"Actual prices: {actual}"
            )

            log(
                f"Expected prices: {expected}"
            )

            if actual == expected:

                pass_test(
                    results,
                    "Price Low to High"
                )

            else:

                fail_test(
                    results,
                    "Price Low to High",
                    f"Expected {expected}, "
                    f"but found {actual}."
                )

        except TimeoutException:
            fail_test(
                results,
                "Price Low to High",
                "Sort dropdown was not found or "
                "was not clickable within 10 seconds."
            )

        except StaleElementReferenceException:
            fail_test(
                results,
                "Price Low to High",
                "A page element became stale while "
                "checking low-to-high price sorting."
            )

        except Exception as error:
            fail_test(
                results,
                "Price Low to High",
                f"Unexpected error during low-to-high "
                f"price test: {error}"
            )


        # =================================================
        # TEST 4 - PRICE HIGH TO LOW
        # =================================================

        try:

            log("")
            log("TEST: Price High to Low")

            select_sort(
                driver,
                wait,
                "hilo"
            )

            log(
                "Reading product prices..."
            )

            actual = get_product_prices(
                driver
            )

            expected = sorted(
                actual,
                reverse=True
            )

            log(
                f"Actual prices: {actual}"
            )

            log(
                f"Expected prices: {expected}"
            )

            if actual == expected:

                pass_test(
                    results,
                    "Price High to Low"
                )

            else:

                fail_test(
                    results,
                    "Price High to Low",
                    f"Expected {expected}, "
                    f"but found {actual}."
                )

        except TimeoutException:
            fail_test(
                results,
                "Price High to Low",
                "Sort dropdown was not found or "
                "was not clickable within 10 seconds."
            )

        except StaleElementReferenceException:
            fail_test(
                results,
                "Price High to Low",
                "A page element became stale while "
                "checking high-to-low price sorting."
            )

        except Exception as error:
            fail_test(
                results,
                "Price High to Low",
                f"Unexpected error during high-to-low "
                f"price test: {error}"
            )


        # =================================================
        # SUMMARY
        # =================================================

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
        log("Sorting Test Suite Complete")
        log(f"Passed: {passed}")
        log(f"Failed: {failed}")
        log(f"Total: {len(results)}")

    finally:

        log("")
        log("Closing Chrome...")
        driver.quit()


    # -------------------------
    # SEND RESULTS TO UI
    # -------------------------

    if result_callback is not None:
        result_callback(
            results,
            "Sorting Test Results"
        )

    return results