##pytest --how to write thee test cases
##testcase/function name--'test_'
##file name--'test_'
##how to run in command prompt--pytest -v
##how to run in headless mode(without opening the browser)
##user assert to indicate test case status--pass/fail
##pytest -v -m sanity
## -m you can run the specific test cases which are under sanity marker..u can use any name at sanity
## -v is to show more details about test run
##  to give marker
##  to create html reports--> pytest -v -m sanity --html=report.html  -->this command run specific test case of  marker of sanity
##                            pytest -v --html=report.html     -->this command run all test cases
## to generate report-->pytest -v --html=Reports/report.html   ##in specific folder
## to run test cases parallely-->pytest -n=4


from selenium import webdriver
from selenium.webdriver.common.by import By

# import pytest
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headlesss')  ## headless means without opening browser it will run code


class Test_py:  ##########class

    # @pytest.mark.xfail
    def test_sum_1(
            self):  ##item--test case --start with 'test_'     ## in this method or function  is called as test case
        a = 5
        b = 3
        sum = a + b
        if sum == 8:
            print('test_sum_1 is passed')
            assert True
        else:
            print('test_sum_1 is failed')
            assert False

    # @pytest.mark.skip
    # @pytest.mark.sanity
    def test_google(self):
        # driver = webdriver.Chrome()
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.google.com/")
        logo = driver.find_element(By.CLASS_NAME, "lnXdpd").is_displayed()
        print(logo)
        if logo == True:
            assert True
        else:
            assert False
        driver.close()

# class Test_py:                                   ##Test_py made test cha T capital letter made pahije
#
#         def test_sum_1(self):    ##item--test case --start with 'test_'   ### ani function made test cha t small pahije
#             a = 5
#             b = 3
#             sum = a + b
#             if sum == 8:
#                 print('test_sum_1 is passed')
#                 assert True
#             else:
#                 print('test_sum_1 is failed')
#                 assert False


##    # def test_mul_2(self):
#     a = 3
#     b = 5
#     sum = a * b
#     if sum == 16:
#         print('test_mul_2 is passed')
#         assert True
#     else:
#         print('test_mul_2 is failed')
#         assert False
#

# def test_mul_2(self):
#     a = 3
#     b = 5
#     mul = a * b
#     print(mul)
#     if mul == 16:
#         print('test_mul_2 is passed')
#         assert True
#     else:
#         print('test_mul_2 is failed')
#         assert False

##    # def mul_2(self):       ##this item/function will not consider as testcase bcause of name
#     a = 3
#     b = 5
#     mul = a * b
#     if mul == 16:
#         print('test_mul_2 is passed')
#         assert True
#     else:
#         print('test_mul_2 is failed')
#         assert False
