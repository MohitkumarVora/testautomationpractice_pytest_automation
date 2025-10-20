import time

def wait_for(seconds):
    time.sleep(seconds)

def take_screenshot(page, name="screenshot"):
    page.screenshot(path=f"screenshots/{name}.png")