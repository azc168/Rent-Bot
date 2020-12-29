from selenium import webdriver
from config import keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def order(k):
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome('./chromedriver', options=chr_options)
    driver.get(k['product_url'])

    driver.find_element_by_xpath('//*[@id="user_email"]').send_keys(k["email"])
    driver.find_element_by_xpath('//*[@id="user_password"]').send_keys(k["user_password"])
    driver.find_element_by_xpath('//*[@id="new_user"]/div/div/div[3]/input').click()
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/main/section/div[3]/div[1]/section[1]/div[2]/div[1]/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="add-another"]').click()
    time.sleep(1)
    #driver.find_element_by_xpath('//*[@id="payment_account_information_routing_number"]').send_keys(k["routing_number"])
    #driver.find_element_by_xpath('//*[@id="payment_account_information_account_number"]').send_keys(k["account_number"])
    #driver.find_element_by_xpath('//*[@id="payment_account_information_account_number_confirmation"]').send_keys(k["account_number"])
    #driver.find_element_by_xpath('/html/body/div[2]/div[2]/main/section/div[2]/div/div/section/form/section/input').click()
    #driver.find_element_by_xpath('//*[@id="new_payment"]/section/input').click()
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/main/section/div[2]/div/div/section/form/section[3]/input').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="new_payment"]/section/input').click()



if __name__ == '__main__':
    order(keys)
