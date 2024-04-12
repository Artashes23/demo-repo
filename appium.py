from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_cap = {
  "platformName": "Android",
  "appium:deviceName": "Android Emulator",
  "appium:appPackage": "com.kazanexpress.ke_app",
  "appium:appWaitActivity": "com.ke_app.android.MainActivity",
  "appium:app": "C:\\Users\\artas\\AppData\\Local\\Android\\Sdk\\platform-tools\\shop.apk"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)

driver.hide_keyboard()
driver.implicitly_wait(30)

element = driver.find_element(AppiumBy.ID, 'com.sand.aircast:id/btnConnect')
# element.click()  # Uncomment if necessary
how_to_start = driver.find_element(AppiumBy.ID, 'com.sand.aircast:id/tvHowToUse')
# how_to_start.click()  # Uncomment if necessary
dropdown = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options')
dropdown.click()

# The following lines were commented out, uncomment them if necessary
# elem = driver.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout')
# elem.click()

settings_btn = driver.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView')
settings_btn.click()

elem_for_text = driver.find_element(AppiumBy.ID, 'com.sand.aircast:id/subTitle')
print(elem_for_text.text)
