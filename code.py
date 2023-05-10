import time

from selenium import webdriver
import pandas as pd

# 用Selenium打开网页
driver = webdriver.Chrome(executable_path="./chromedriver.exe")
url = 'https://data.eastmoney.com/cjsj/yjtz/default.html'
driver.get(url)


# 爬取数据
columns = ['调整日期', '品种', '价格(元/吨)', '涨跌', '品种', '价格(元/吨)', '涨跌']
data = []
for page in range(1, 10):  # 爬取前5页
    # 搜索页面中的表格元素
    table = driver.find_element_by_xpath('//div[@id="cjsj_table"]/table')
    rows = table.find_elements_by_tag_name('tr')

    for row in rows:
        # 在每次迭代中重新搜索行中的所有列元素
        cols = row.find_elements_by_tag_name('td')
        cols = [col.text for col in cols]
        data.append(cols)

    # 点击下一页按钮
    next_page_btn = driver.find_element_by_xpath(
        '//div[@id="cjsj_table_pager"]/div[@class="pagerbox"]/a[text()="下一页"]')
    next_page_btn.click()

    # 等待新页面加载
    time.sleep(1)

# 将数据保存到Excel中
df = pd.DataFrame(data)
df.to_excel('oil_price.xlsx', index=False, header=columns)
