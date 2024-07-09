from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# URL of the page to be tested
URL = "https://jqueryui.com/droppable/"

# Function to perform drag and drop operation
def perform_drag_and_drop():
    # Create a WebDriver instance (for Chrome in this case)
    driver = webdriver.Chrome()
    
    try:
        # Open the URL
        driver.get(URL)
        
        # Switch to the iframe containing the draggable elements
        driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))
        
        # Locate the draggable element (white box)
        draggable = driver.find_element(By.ID, "draggable")
        
        # Locate the droppable element (yellow box)
        droppable = driver.find_element(By.ID, "droppable")
        
        # Use ActionChains for drag and drop operation
        action_chains = ActionChains(driver)
        
        # Perform drag and drop
        action_chains.drag_and_drop(draggable, droppable).perform()
        
        # Verify if the text in droppable element has changed after drop
        assert "Dropped!" in droppable.text
        
        print("Drag and Drop successful!")
        
    finally:
        # Close the WebDriver session
        driver.quit()

# Entry point of the script
if __name__ == "__main__":
    perform_drag_and_drop()
