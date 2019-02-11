'''
Created on Feb 7, 2019

@author: Arun Sarita
'''
from selenium import webdriver

obj_file=r'C:\Users\Arun Sarita\Desktop\Python FrameworkSetup\naukari.txt'
driver= webdriver.Chrome(executable_path='F:/selenium/chromedriver.exe')
f_id=driver.find_element_by_id
f_xpath=driver.find_element_by_xpath
f_name=driver.find_element_by_name
def dismiss():
    driver.switch_to_alert().dismiss()
    
def accept():
    driver.switch_to_alert().accept()
    #driver._switch_to().fr
