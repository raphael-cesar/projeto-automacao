import json
import pytest
import time
import os
import pytest_html
from selenium import webdriver
from pathlib import Path
from Utils.data_loader import load_json_data
import csv

report_data = []


#fixture = pre setups de configurações

# @pytest.fixture(scope="session")
# def test_data():
#     with open("Data/test_data.json") as f:
#         return json.load(f)



LOG_FILE = Path("test_durations.log")

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    '''
        Get the time execution of the test
    '''
    item.start_time = time.time()
    item.start_str = time.strftime("%H:%M:%S", time.localtime())
    msg = f"\n[START] Test '{item.nodeid}' - {item.start_str}"
    print(msg)
    
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(msg + "\n")

@pytest.hookimpl(trylast=True)
def pytest_runtest_teardown(item):
    '''
        Get the duration of the test
    '''
    duration = time.time() - item.start_time
    msg = f"[END] Test '{item.nodeid}' finished in {duration:.2f} seconds."
    print(msg)

    # salva em arquivo
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(msg + "\n")


# #Choose your browser
# def pytest_addoption(parser):
#     '''
#         Choose your browser when running pytest
#         pytest --browser = your_browser
#     '''
#     parser.addoption("--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)")

@pytest.fixture(params=["chrome", "firefox"],scope="function")
def driver(request):
    '''
        Define your browsers options with a Selenium WebDriver instance
    '''
    #browser = request.config.getoption("--browser").lower()
    browser = request.param
    if browser == "chrome":
        driver_instance = webdriver.Chrome()
    elif browser == "firefox":
        driver_instance = webdriver.Firefox()
    else:
        raise ValueError(f"Browser '{browser}' is not supported.")
    
    # attach the chosen browser name to the test item so other hooks can access it
    try:
        request.node.browser = browser
    except Exception:
        # if for any reason we cannot attach, continue without failing
        pass

    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()
    
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call": # and report.failed:

        status = 'Passed' if report.passed else 'Failed'
        # Try to read browser name attached to the item (set in the driver fixture)
        browser = getattr(item, 'browser', None)
        # Fallback: try to derive browser from the webdriver instance capabilities
        if not browser:
            drv = item.funcargs.get('driver') if hasattr(item, 'funcargs') else None
            if drv:
                try:
                    caps = getattr(drv, 'capabilities', {}) or {}
                    browser = caps.get('browserName') or caps.get('browser')
                except Exception:
                    browser = None
        if not browser:
            browser = 'N/A'
        test_name = item.name
        duration = f"{report.duration:.4f}s"

        if report.failed:
            # Create screenshots directory if it doesn't exist
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            # Take screenshot
            driver = item.funcargs['driver']
            screenshot_file = os.path.join("screenshots", f"{item.name}_error.png")
            driver.save_screenshot(screenshot_file)
            # Add screenshot to the HTML report
            if screenshot_file:
                html = f'<div><img src="{screenshot_file}" alt="screenshot" style="width:304px;height:228px;" ' \
            f'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))
        
        report_data.append({
            "browser": browser.capitalize(),
            "test_case_name": test_name,
            "status": status,
            "timestamp": duration
        })

    report.extra = extra

def pytest_sessionfinish(session):
    """
    Hook executed in the end of test session to create the CSV report.
    """
    if not report_data:
        return
        
    sorted_reports = sorted(report_data, key=lambda x: x['browser'])
    
    keys = sorted_reports[0].keys()
    
    with open('test_report.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(sorted_reports)

    print("\nReport 'test_report.csv' generated successfully")
    
@pytest.fixture(scope="class")
def class_resource():
    print("\n[SETUP] class_resource")
    yield "class fixture"
    print("[TEARDOWN] class_resource")

@pytest.fixture(scope="module")
def module_resource():
    print("\n[SETUP] module_resource")
    yield "module fixture"
    print("[TEARDOWN] module_resource")

@pytest.fixture(scope="session")
def session_resource():
    print("\n[SETUP] session_resource")
    yield "session fixture"
    print("[TEARDOWN] session_resource")

# #SCREENSHOT ON FAILURE
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     '''
#         Take a screenshot when a test fail
#     '''
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call" and report.failed:
#         # Create screenshots directory if it doesn't exist
#         if not os.path.exists("screenshots"):
#             os.makedirs("screenshots")
#         # Take screenshot
#         driver = item.funcargs['driver']
#         screenshot_file = os.path.join("screenshots", f"{item.name}_error.png")
#         driver.save_screenshot(screenshot_file)
#         # Add screenshot to the HTML report
#         if screenshot_file:
#             html = f'<div><img src="{screenshot_file}" alt="screenshot" style="width:304px;height:228px;" ' \
#            f'onclick="window.open(this.src)" align="right"/></div>'
#             extra.append(pytest_html.extras.html(html))
#     report.extra = extra