# 전체 댓글이 아니라 일부분만 가져오게 짜놓은 코드입니다.
# 크롬이 설치되어 있어야 함
# Mac SSL certificate verify failed 에러 뜬 경우
# http://corazzon.github.io/python_ssl_error
# finder에서 Applications/Python 3.9 가서 저 파일 더블클릭

# pip install chromedriver-autoinstaller
# pip install openpyxl -y
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
import pandas as pd
import chromedriver_autoinstaller




# 유투브 주소
url = 'https://www.youtube.com/watch?v=C-qXqJKIh1A'
data = []

chromedriver_autoinstaller.install()

options = ChromeOptions()
options.add_argument('ignore-certificate-errors')
options.add_argument("--start-maximized") #이거 추가


with Chrome(chrome_options=options) as driver:
    wait = WebDriverWait(driver, 3)
    driver.get(url)

    for _ in range(6):
        wait.until(EC.visibility_of_element_located(
            (By.TAG_NAME, "body"))).send_keys(Keys.PAGE_DOWN)
        time.sleep(2)

    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content-text"))):
        data.append(comment.text)

data_df = pd.DataFrame(data,columns=['contents']) #이거 추가
# print(type(data_df))
# print(data_df.columns)
# print(data_df)

data_df.to_excel('오늘댓글.xlsx', index=False,)
print("오늘댓글.xlsx 파일로 댓글이 잘 저장되었습니다.")
