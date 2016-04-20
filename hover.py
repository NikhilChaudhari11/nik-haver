from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import win32api
from win32con import *


##driver = webdriver.Chrome('C:\\Users\\Research18\\Documents\\py projects\\chromedriver.exe')
##driver.get('http://87.101.205.104:6855/en/BulkDownload')
##time.sleep(10)
##driver.set_window_size(300, 500)
##driver.set_window_position(200, 200)
####element = driver.find_element_by_id('14621425')
####
####hover = ActionChains(driver).move_to_element(element)
####
####hover.perform()
##
##driver.execute_script("document.body.style.zoom='30%'")
##


from selenium.webdriver.common.keys import Keys    

##br = webdriver.Firefox()
##br.get('http://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python')
##br.maximize_window()
##time.sleep(10)
##zoomAction = ActionChains(br)
##body = br.find_element_by_xpath('//*[@id="gsr"]')
##
##
##for i in range(6):
##    zoomAction.send_keys_to_element(body,Keys.CONTROL,win32api.mouse_event(MOUSEEVENTF_WHEEL, x, y, -1, 0)).perform()
##
#br.execute_script("window.scrollTo(0, document.body.scrollHeight);")
##scheight = .1
##while scheight < 9.9:
##    br.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
##    scheight += .01

##lis5 = ['22595525', '16816025']
##for i in range(16816625, 16817826,100):
##    i = str(i)
##    lis5.append(i)
##
##
##print(lis5)
#br.execute_script("window.scrollTo(0, document.body.scrollHeight/3.5);window.scrollTo(0, document.body.scrollHeight/3.7);")

#----scroll within a web element----------------------
##def scroll_down_element(self, element, times):
##    try:
##        action = ActionChains(self.browser)
##        action.move_to_element(element).perform()
##        element.click() 
##        for _ in range(times):
##            element.send_keys(Keys.SPACE)
##            sleep(0.1)
##    except Exception as e:
##        print ('error scrolling down web element', e)
#---------------------------------------------------------------------
def genn(start,end,inte):
    lis = []
    for i in range(start,end+inte,inte):
        i = str(i)
        lis.append(i)
    return(lis)

y = genn(100,900,100)
print(y)

