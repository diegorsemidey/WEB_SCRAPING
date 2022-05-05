import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

class SERP_Google(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")

	def test_toplist(self):
		driver = self.driver
		driver.get("https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue")
		time.sleep(5)
		clist = list()
		for i in range(1,10):
			company = driver.find_element_by_xpath("//*[@id='mw-content-text']/div[1]/table[2]/tbody/tr["+str(i)+"]/td[1]/a").text
			clist.append(company)
		driver.execute_script("window.open('');")
		driver.switch_to.window(driver.window_handles[1])
		driver.get("https://www.google.com")
		search = driver.find_element_by_name("q")
		serp = list()
		for i in clist:
			search.send_keys(i)
			time.sleep(1)
			for i in range(1,10):
				result=driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/ul/li["+str(i)+"]/div/div[2]/div[1]/span").text
				serp.append(result)
			search.clear()

		df = pd.DataFrame({'serp':serp})
		print(df)
		df.to_csv('serp.csv',index=False)

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()
		
		