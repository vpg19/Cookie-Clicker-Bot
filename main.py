from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.ID, "cookie")
timeout = time.time() + 5
five_min = time.time() + 60 * 5  # 5 minutes

while True:
    cookie.click()
    
    if time.time() > timeout:
        # Get all upgrade items
        items = driver.find_elements(By.CSS_SELECTOR, "#store div")
        item_ids = [item.get_attribute("id") for item in items if item.get_attribute("id")]
        
        # Get current money amount
        money_element = driver.find_element(By.ID, "money").text
        money = int(money_element.replace(",", ""))
        
        # Find all affordable upgrades
        affordable_upgrades = {}
        for item_id in item_ids:
            if item_id:  # Skip empty IDs
                try:
                    price_element = driver.find_element(By.CSS_SELECTOR, f"#{item_id} b")
                    price_text = price_element.text
                    if "-" in price_text:
                        price = int(price_text.split("-")[1].strip().replace(",", ""))
                        affordable_upgrades[item_id] = price
                except:
                    continue
        
        # Purchase the most expensive affordable upgrade
        if affordable_upgrades:
            # Sort upgrades by price (highest first)
            sorted_upgrades = sorted(affordable_upgrades.items(), key=lambda x: x[1], reverse=True)
            for upgrade_id, price in sorted_upgrades:
                if money >= price:
                    try:
                        driver.find_element(By.ID, upgrade_id).click()
                        break
                    except:
                        continue
        
        timeout = time.time() + 5
    
    if time.time() > five_min:
        cps = driver.find_element(By.ID, "cps").text
        print(f"Cookies/second: {cps}")
        driver.quit()
        break