from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import pandas as pd

webdriver = './chromedriver'

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = webdriver.(options=chrome_options)

driver = Chrome(webdriver)
driver.minimize_window()




pages = 10

url = "https://www.reformagkh.ru/opendata?gid=2208161&cids=house_management&page=1&pageSize=10"
driver.get(url)
try:
    # <a href="/opendata/export/101" class="text-decoration-underline">Экспорт</a>
    # lh-27 f-18 fw-700
    items = driver.find_element_by_class_name("wrapper").\
        find_element_by_id("opendata-form").find_element_by_tag_name("section").\
        find_element_by_class_name("container").find_element_by_tag_name("p").find_element_by_css_selector("lh-27 f-18 fw-700")





    print(items)
except Exception as error:
    print(error)

# for page in range(1, pages):
#     url = "https://www.reformagkh.ru/opendata?gid=2208161&cids=house_management&page=" + str(page) + "&pageSize=10"
#     driver.get(url)
#     items = driver.find_element_by_class_name("container").find_element_by_class_name("lh-27 f-18 fw-700")
#     print(items)


    # for item in range(items):
        # quotes = driver.find_elements_by_class_name("quote")
        # print (item)
        # for quote in quotes:
        #     quote_text = quote.find_element_by_class_name('text').text
        #     author = quote.find_element_by_class_name('author').text
        #     new = ((quote_text, author))
        #     total.append(new)
    # df = pd.DataFrame(total, columns=['quote', 'author'])
    # df.to_csv('quoted.csv')
driver.close()