'''
Created on Jan 31, 2019

@author: Arun Sarita
'''

from selenium import webdriver
import time
import POM
keys={}  
def load_keys():
    f = open(POM.obj_file,'r')
    ####read data from file 
    data = f.readlines()
    for line in data:
            col=line.split('\t')
            keys[col[0]]= col[1].replace('\n','')
    return keys 


def open_browser():
    keys = load_keys()
    return(keys['url'])#driver)

def w_close():
    n = POM.driver.window_handles
    l=len(n)
    print('Naukri has==>'+str(l)+'  Popup Windows')
    parent_handle = POM.driver.current_window_handle
    for x in range(l):
        if n[x] != parent_handle:
            POM.driver.switch_to_window(n[x])#switch_to.window(handles[x]);
            print(POM.driver.title)
            POM.driver.close()
                  
            #break
    POM.driver.switch_to_window(parent_handle)
    time.sleep(5)
    POM.f_id('login_Layer').click()
    #time.sleep(5)
    #driver.find_element_by_id('login_Layer').click()
   
u=open_browser()
POM.driver.get(u)
POM.driver.maximize_window()
time.sleep(5)
w_close()
print(POM.driver.current_url)

