import threading
import tkinter as tk
from tkinter import scrolledtext
from test_login import run_login_tests
from test_cart import run_cart_tests
from test_checkout import run_checkout_tests
from test_sorting import run_sorting_tests

from common import (
    build_report,
    show_full_report,
    show_results,
    set_log_callback
)

# =====================================================
# UI LOGGING
# =====================================================

def write_to_log(message):
    """
    This function may be called from a Selenium worker thread.

    Tkinter should only be modified from the main thread,
    so root.after() schedules the actual UI update.
    """

    root.after(
        0,
        update_log_box,
        message
    )


def update_log_box(message):
    """
    Actually writes the message into the Tkinter text box.
    This runs on the Tkinter main thread.
    """

    output_box.insert(
        tk.END,
        message + "\n"
    )

    output_box.see(
        tk.END
    )


def clear_log():

    output_box.delete(
        "1.0",
        tk.END
    )


set_log_callback(
    write_to_log
)


# =====================================================
# TEST RESULT CALLBACK
# =====================================================

def test_results_finished(
    results,
    suite_name
):

    root.after(
        0,
        show_individual_results,
        results,
        suite_name
    )


def show_individual_results(
    results,
    suite_name
):

    show_results(
        results,
        suite_name
    )


# =====================================================
# INDIVIDUAL TEST BUTTONS
# =====================================================

def login_tests():

    clear_log()

    write_to_log(
        "Starting Login Tests..."
    )

    write_to_log(
        "=" * 40
    )

    threading.Thread(
        target=run_login_tests,
        kwargs={
            "result_callback":
                test_results_finished
        },
        daemon=True
    ).start()


def cart_tests():

    clear_log()

    write_to_log(
        "Starting Cart Tests..."
    )

    write_to_log(
        "=" * 40
    )

    threading.Thread(
        target=run_cart_tests,
        kwargs={
            "result_callback":
                test_results_finished
        },
        daemon=True
    ).start()


def checkout_tests():

    clear_log()

    write_to_log(
        "Starting Checkout Tests..."
    )

    write_to_log(
        "=" * 40
    )

    threading.Thread(
        target=run_checkout_tests,
        kwargs={
            "result_callback":
                test_results_finished
        },
        daemon=True
    ).start()


def sorting_tests():

    clear_log()

    write_to_log(
        "Starting Product Sorting Tests..."
    )

    write_to_log(
        "=" * 40
    )

    threading.Thread(
        target=run_sorting_tests,
        kwargs={
            "result_callback":
                test_results_finished
        },
        daemon=True
    ).start()


# =====================================================
# RUN ALL TESTS
# =====================================================

def run_all_tests():

    clear_log()

    write_to_log(
        "RUNNING COMPLETE TEST SUITE"
    )

    write_to_log(
        "=" * 40
    )

    threading.Thread(
        target=run_all_tests_worker,
        daemon=True
    ).start()


def run_all_tests_worker():

    # -------------------------
    # LOGIN TESTS
    # -------------------------

    write_to_log("")
    write_to_log(
        "Starting Login Tests..."
    )
    write_to_log(
        "-" * 40
    )

    login_results = run_login_tests()


    # -------------------------
    # CART TESTS
    # -------------------------

    write_to_log("")
    write_to_log(
        "Starting Cart Tests..."
    )
    write_to_log(
        "-" * 40
    )

    cart_results = run_cart_tests()


    # -------------------------
    # CHECKOUT TESTS
    # -------------------------

    write_to_log("")
    write_to_log(
        "Starting Checkout Tests..."
    )
    write_to_log(
        "-" * 40
    )

    checkout_results = (
        run_checkout_tests()
    )


    # -------------------------
    # SORTING TESTS
    # -------------------------

    write_to_log("")
    write_to_log(
        "Starting Sorting Tests..."
    )
    write_to_log(
        "-" * 40
    )

    sorting_results = (
        run_sorting_tests()
    )


    # =================================================
    # BUILD COMPLETE REPORT
    # =================================================

    complete_report = ""

    complete_report += build_report(
        login_results,
        "LOGIN TESTS"
    )

    complete_report += "\n\n"

    complete_report += build_report(
        cart_results,
        "CART TESTS"
    )

    complete_report += "\n\n"

    complete_report += build_report(
        checkout_results,
        "CHECKOUT TESTS"
    )

    complete_report += "\n\n"

    complete_report += build_report(
        sorting_results,
        "SORTING TESTS"
    )


    # =================================================
    # OVERALL TOTALS
    # =================================================

    all_results = (
        login_results
        + cart_results
        + checkout_results
        + sorting_results
    )

    total_passed = sum(
        1
        for result in all_results
        if result["passed"]
    )

    total_failed = sum(
        1
        for result in all_results
        if not result["passed"]
    )

    complete_report += "\n\n"

    complete_report += (
        "OVERALL RESULTS\n"
    )

    complete_report += (
        "===============\n\n"
    )

    complete_report += (
        f"Total Passed: "
        f"{total_passed}\n"
    )

    complete_report += (
        f"Total Failed: "
        f"{total_failed}\n"
    )

    complete_report += (
        f"Total Tests: "
        f"{len(all_results)}\n"
    )


    # =================================================
    # UPDATE LIVE LOG
    # =================================================

    write_to_log("")
    write_to_log(
        "=" * 40
    )

    write_to_log(
        "TESTING COMPLETE"
    )

    write_to_log(
        "=" * 40
    )

    write_to_log(
        f"Passed: {total_passed}"
    )

    write_to_log(
        f"Failed: {total_failed}"
    )

    write_to_log(
        f"Total: {len(all_results)}"
    )


    # =================================================
    # SHOW FINAL REPORT
    # =================================================

    root.after(
        0,
        show_complete_report,
        complete_report
    )


def show_complete_report(report):

    show_full_report(
        report
    )


# =====================================================
# MAIN WINDOW
# =====================================================

root = tk.Tk()

root.title(
    "SauceDemo QA Automation"
)

root.geometry(
    "800x650"
)

root.minsize(
    700,
    550
)

# =====================================================
# TITLE
# =====================================================

title = tk.Label(
    root,
    text="SauceDemo QA Automation",
    font=("Arial", 18, "bold")
)

title.pack(
    pady=(15, 5)
)


subtitle = tk.Label(
    root,
    text="Select a test suite:"
)

subtitle.pack(
    pady=5
)


# =====================================================
# BUTTON FRAME
# =====================================================

button_frame = tk.Frame(
    root
)

button_frame.pack(
    pady=10
)


login_button = tk.Button(
    button_frame,
    text="Login Tests",
    width=18,
    command=login_tests
)

login_button.grid(
    row=0,
    column=0,
    padx=5,
    pady=5
)


cart_button = tk.Button(
    button_frame,
    text="Cart Tests",
    width=18,
    command=cart_tests
)

cart_button.grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)


checkout_button = tk.Button(
    button_frame,
    text="Checkout Tests",
    width=18,
    command=checkout_tests
)

checkout_button.grid(
    row=0,
    column=2,
    padx=5,
    pady=5
)


sorting_button = tk.Button(
    button_frame,
    text="Sorting Tests",
    width=18,
    command=sorting_tests
)

sorting_button.grid(
    row=1,
    column=0,
    padx=5,
    pady=5
)


run_all_button = tk.Button(
    button_frame,
    text="Run All Tests",
    width=18,
    command=run_all_tests
)

run_all_button.grid(
    row=1,
    column=1,
    padx=5,
    pady=5
)


clear_button = tk.Button(
    button_frame,
    text="Clear Log",
    width=18,
    command=clear_log
)

clear_button.grid(
    row=1,
    column=2,
    padx=5,
    pady=5
)


# =====================================================
# EXECUTION LOG
# =====================================================

log_label = tk.Label(
    root,
    text="Test Execution Log",
    font=("Arial", 11, "bold")
)

log_label.pack(
    anchor="w",
    padx=20,
    pady=(10, 5)
)


output_box = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Consolas", 10)
)

output_box.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=(0, 20)
)


# =====================================================
# START GUI
# =====================================================

root.mainloop()