import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")


class Test_credencesite:

    def test_sum_7(self):
        a = 3
        b = 4
        sum = a + b
        if sum == 7:
            assert True
        else:
            assert False

    def test_credence1(self):

        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://credence.in/")
        offers = driver.find_element(By.XPATH, "//span[@class='text-white b label']").text
        print(offers)
        print(driver.title)

        if driver.title == "Credence":
            driver.close()
            assert True
        else:
            driver.close()
            assert False




    # def test_credence2(self):
    #     driver = webdriver.Chrome(options=chrome_options)
    #     # driver=webdriver.Chrome()
    #     driver.get("https://credence.in/")
    #     driver.find_element(By.XPATH, "//img[@src='/website/images/enquiry.png']").click()
    #     time.sleep(5)
    #     l = len(driver.find_element(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//h4//p//a"))
    #     list=[]
    #     time.sleep(2)
    #     print(l)
    #     for r in range(1, l + 1):
    #         contact = driver.find_element(By.XPATH,"//div[@class='quickfinder-description gem-text-output']//p//a[" + str(r) + "]").text
    #         print(contact)
    #         list.append(contact)
    #
    #     if "+91 8237916162" in list:
    #         print(r)
    #         # break
    #         # assert True
    #
    #     else:
    #         print(r)
    #         # assert False





