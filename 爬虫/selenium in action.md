## selenium in action

https://www.selenium.dev/documentation/en/



#### 1. windows and tabs 

https://www.selenium.dev/documentation/en/webdriver/browser_manipulation/#windows-and-tabs



```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start the driver
with webdriver.Firefox() as driver:
    # Open URL
    driver.get("https://seleniumhq.github.io")

    # Setup wait for later
    wait = WebDriverWait(driver, 10)

    # Store the ID of the original window
    original_window = driver.current_window_handle

    # Check we don't have other windows open already
    assert len(driver.window_handles) == 1

    # Click the link which opens in a new window
    driver.find_element(By.LINK_TEXT, "new window").click()

    # Wait for the new window or tab
    wait.until(EC.number_of_windows_to_be(2))

    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    # Wait for the new tab to finish loading content
    wait.until(EC.title_is("SeleniumHQ Browser Automation"))
```

> \# 等待搜索页显示(通过查找id为goodsList的节点判断搜索页面是否显示)
>
> wait.util(EC.presence_of_all_elements_located((By.ID, 'J_goodList')))



**Closing a window or tab**

```python
#Close the tab or window
driver.close()

#Switch back to the old tab or window
driver.switch_to.window(original_window)
```



**Quitting the browser at the end of a session**

When you are finished with the browser session you should call quit, instead of close: 

```python
driver.quit()
```



Python’s WebDriver now supports the python context manager, which when using the `with` keyword can automatically quit the driver at the end of execution. 

```python
with webdriver.Firefox() as driver:
  # WebDriver code here...

# WebDriver will automatically quit after indentation
```



#### 2. Frames and Iframes

https://www.selenium.dev/documentation/en/webdriver/browser_manipulation/#frames-and-iframes



> **frameset不用切，frame需层层切**
>
> https://blog.csdn.net/huilan_same/article/details/52200586



#### 3. Window management

https://www.selenium.dev/documentation/en/webdriver/browser_manipulation/#window-management

屏幕分辨率可能会影响Web应用程序的呈现方式，因此WebDriver提供了用于移动和调整浏览器窗口大小的机制



**TakeScreenshot**

Used to capture screenshot for current browsing context. The WebDriver endpoint [screenshot](https://www.w3.org/TR/webdriver/#dfn-take-screenshot) returns screenshot which is encoded in Base64 format. 

```python
from selenium import webdriver

driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.example.com")

# Returns and base64 encoded string into image
driver.save_screenshot('./image.png')

driver.quit()
```



**TakeElementScreenshot**

Used to capture screenshot of an element for current browsing context. The WebDriver endpoint [screenshot](https://www.w3.org/TR/webdriver/#take-element-screenshot) returns screenshot which is encoded in Base64 format. 

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.example.com")

ele = driver.find_element(By.CSS_SELECTOR, 'h1')

# Returns and base64 encoded string into image
ele.screenshot('./image.png')

driver.quit()
```





#### 4. 三种等待方式

https://www.jb51.net/article/92672.htm



```python
## 隐性等待
driver.implicitly_wait(15)  

## 显性等待
from selenium.webdriver.support.ui import WebDriverWait
WebDriverWait(driver, timeout=3).until(some_condition) 
```





#### 5. 补充参考

https://blog.csdn.net/weixin_36279318/article/details/79475388



---

#### action : 自动打卡

[call.py](./call.py)



每天一早要到工位上，打开电脑浏览器，登陆打卡？ 这怎么能忍，用一个脚本配合定时任务帮自己打卡吧。

