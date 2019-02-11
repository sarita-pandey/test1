'''
Created on Feb 6, 2019

@author: Arun Sarita
'''
import POM
import naukari_homepage
import time
from selenium.webdriver.common.action_chains import ActionChains

import login
time.sleep(5)
main_m=POM.f_xpath('/html/body/div[1]/div/div/ul[2]/li[2]/a/div[2]')
action1=ActionChains(POM.driver)
action1.move_to_element(main_m)
action1.perform()
POM.f_xpath('/html/body/div[1]/div/div/ul[2]/li[2]/div/ul[1]/li[1]/a').click()
time.sleep(5)

def resu_head():
    POM.f_xpath('//*[@id="lazyResumeHead"]/div/div/div/div[1]/span[2]').click()
    time.sleep(5)
    res_he=input('Enter Your Resume Heading:=')
    time.sleep(5)
    rhl=POM.f_id('resumeHeadlineTxt')
    rhl.clear()
    rhl.send_keys(res_he)
    time.sleep(5)
    POM.f_xpath('/html/body/div[5]/div[5]/div[2]/form/div[3]/div/button').click()

def key_skill():
    POM.f_xpath('//*[@id="lazyKeySkills"]/div/div/div/div[1]/span[2]').click()
    time.sleep(10)
    ks=input('Enter Your Key Skills')
    time.sleep(5)
    ks1=POM.f_id('keySkillSugg')
    ks1.clear()
    ks1.send_keys(ks)
    time.sleep(5)
    POM.f_id('saveKeySkills').click()
    
def Add_emp():
    POM.f_xpath('//*[@id="lazyEmployment"]/div/div/div/div[1]/span[2]').click()
    time.sleep(5)
    desg=POM.f_id('designationSugg')
    time.sleep(5)
    desg1=input('Enter Your Designation')
    time.sleep(5)
    desg.clear()
    desg.send_keys(desg1)
    time.sleep(5) 
    your_org=POM.f_id('companySugg')
    you_org1=input('Enter Your Organization')
    time.sleep(5)
    your_org.clear()
    your_org.send_keys(you_org1)
    time.sleep(5)
    opt=input("Is this is your current company Yes or No")
    if opt=='Yes' or opt=='YES' or opt=='yes':
        POM.f_xpath('//*[@id="employmentForm"]/div[4]/div[2]/label').click()
    elif opt=='No' or opt=='no' or opt=='NO':
        POM.f_xpath('//*[@id="employmentForm"]/div[4]/div[3]/label').click()#driver.find_element_by_xpath('//*[@id="employmentForm"]/div[4]/div[3]/label').click()
    time.sleep(5)
    strtfrom=POM.f_id('startedYearFor')#driver.find_element_by_id('startedYearFor')
    time.sleep(5)
    str_f=input('Enter start Year')
    strtfrom.clear()
    strtfrom.send_keys(str_f)
    

resu_head()
time.sleep(10)
key_skill()
time.sleep(10)
Add_emp()

print('Log Out')