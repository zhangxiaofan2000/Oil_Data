from selenium import webdriver
import pandas as pd

# 设置 Chrome driver 路径
chromedriver_path = './chromedriver.exe'

# 创建 Chrome driver
driver = webdriver.Chrome(chromedriver_path)

# 打开网页
driver.get('https://data.eastmoney.com/cjsj/yjtz/default.html')

# 等待表格加载完成
driver.implicitly_wait(10)

# 找到油价表格
table = driver.find_element_by_id('cjsj_table')

# 获取表格中的数据
data = []
rows = table.find_elements_by_tag_name('tr')
for row in rows:
    cols = row.find_elements_by_tag_name('td')
    cols_data = []
    for col in cols:
        cols_data.append(col.text)
    data.append(cols_data)

# 关闭浏览器
driver.quit()

# 将数据保存到 Excel 文件
df = pd.DataFrame(data[1:], columns=data[0])
df.to_excel('oil_prices.xlsx', index=False)
