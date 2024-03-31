# import pytest

# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# class Test_credencesite:
#
#     def test_sum_8(self):
#         a = 4
#         b = 4
#         sum = a + b
#         if sum == 8:
#             assert True
#         else:
#             assert False
#
#     def test_credence(self):
#         driver = webdriver.Chrome()
#         driver.get("https://credence.in/")
#         driver.find_element(By.XPATH, "//img[@src='/website/images/enquiry.png']").click()
#         l = len(driver.find_element(By.XPATH, "//div[@class='quickfinder-description gem-text-output']"))
#         time.sleep(5)
#         for r in range(1, l + 1):
#             contact = driver.find_element(By.XPATH,"//div[@class='quickfinder-description gem-text-output']//p//a[" + str(1) + "]").text
#             if contact == "+91 8237916162":
#                 print(r)
#                 assert True
#                 break
#
#             else:
#                 assert False
