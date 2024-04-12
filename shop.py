from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy as By
from time import sleep

desired_cap = {
  "platformName": "Android",
  "appium:deviceName": "Android Emulator",
  "appium:appPackage": "com.kazanexpress.ke_app",
  "appium:appWaitActivity": "com.ke_app.android.MainActivity",
  "appium:app": "C:\\Users\\artas\\AppData\\Local\\Android\\Sdk\\platform-tools\\shop.apk"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_cap)
driver.implicitly_wait(30)
sleep(1)
driver.back()
sleep(2)
driver.back()
sleep(2)
driver.back()
#search_field = driver.find_element(By.ID,'com.kazanexpress.ke_app:id/search_bar')
sleep(3)
first_element = driver.find_element(By.XPATH,'//android.widget.ImageView[@content-desc="Item card holder"][1]')
first_element.click()
#cosmetics = driver.find_element(By.CLASS_NAME,'android.widget.ImageView')
#cosmetics.click()
#driver.find_element(By.CLASS_NAME,'android.widget.ImageView').click()
add_btn = driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.View/android.view.View[5]/android.view.View/android.widget.Button")
add_to_cart_btn = driver.find_element(By.CLASS_NAME,'android.widget.Button')
add_to_cart_btn.click()
add_btn.click()
sleep(2)
#driver.execute_script('mobile: performEditorAction', {'action': 'done'})
