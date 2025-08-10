from selenium.webdriver.common.by import By
import time

class Home:
    def __init__(self, driver):
        self.driver = driver

    TITLE = (By.XPATH, "//h3[normalize-space()='Featured']")

    def get_title(self):
        print("title is :",self.driver.find_element(*self.TITLE).text)
        return self.driver.find_element(*self.TITLE).text
    
    def test_all_products(self):
        print("\n🔍 Starting product checks...\n")

        total = len(self.driver.find_elements(By.CLASS_NAME, "product-layout"))
        print(f"Total featured products: {total}\n")

        for i in range(total):
            try:
                print(f"\n📦 Checking product #{i + 1}")

                # Re-fetch product to avoid stale element
                product = self.driver.find_elements(By.CLASS_NAME, "product-layout")[i]

                # UI Checks
                image = product.find_element(By.CLASS_NAME, "img-responsive")
                print("🖼️ Image:", image.get_attribute("src"))

                title = product.find_element(By.TAG_NAME, "h4")
                print("🏷️ Title:", title.text)

                try:
                    description = product.find_element(By.TAG_NAME, "p")
                    print("📝 Description:", description.text)
                except Exception:
                    print("⚠️ No description")

                price = product.find_element(By.CLASS_NAME, "price")
                print("💲 Price:", price.text)

                # ✅ Functional Button Clicks (each time re-fetch to avoid stale)
                # Add to Cart
                product = self.driver.find_elements(By.CLASS_NAME, "product-layout")[i]
                buttons = product.find_elements(By.XPATH, ".//button")
                buttons[0].click()
                print("🛒 Clicked: Add to Cart")
                time.sleep(1)

                # Wishlist
                product = self.driver.find_elements(By.CLASS_NAME, "product-layout")[i]
                buttons = product.find_elements(By.XPATH, ".//button")
                buttons[1].click()
                print("💖 Clicked: Wishlist")
                time.sleep(1)

                # Compare
                product = self.driver.find_elements(By.CLASS_NAME, "product-layout")[i]
                buttons = product.find_elements(By.XPATH, ".//button")
                buttons[2].click()
                print("📊 Clicked: Compare")
                time.sleep(1)

            except Exception as e:
                print(f"❌ Error on product #{i + 1}: {e}")