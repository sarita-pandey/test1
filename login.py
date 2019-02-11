'''
Created on Feb 2, 2019

@author: Arun Sarita
'''
import POM
import naukari_homepage
import time
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import ActionChains

#time.sleep(10)

def load_id():
    keys=naukari_homepage.load_keys()
    return((keys['uid']),(keys['pwd']))
time.sleep(5)
u,p=load_id() 

#geting id and pwd from object file
time.sleep(5)
uid=POM.f_id('eLoginNew')#driver.find_element_by_id('eLoginNew') 
uid.clear()
uid.send_keys(u)
time.sleep(5)

pwd=POM.f_id('pLogin')#driver.find_element_by_id('eLoginNew') 
pwd.clear()
pwd.send_keys(p)
time.sleep(5) 
POM.f_xpath('//*[@id="lgnFrmNew"]/div[9]/button').click()#driver.find_element_by_xpath('//*[@id="lgnFrmNew"]/div[9]/button').click()
time.sleep(10)
'''   
main_m=naukari_homepage.driver.find_element_by_xpath('/html/body/div[1]/div/div/ul[2]/li[2]/a/div[2]')
action1=ActionChains(naukari_homepage.driver)
action1.move_to_element(main_m)
action1.perform()
naukari_homepage.driver.find_element_by_xpath('/html/body/div[1]/div/div/ul[2]/li[2]/div/ul[1]/li[1]/a').click()
time.sleep(10)
'''



