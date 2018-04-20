from selenium import webdriver
import time
import subprocess
import sys
import csv
from cmd import Cmd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
driver = webdriver.Chrome()
# example.py


username = 'ccfongaa3'
password = 'pwwww'

q1 = '你求學時最喜愛的科目?'
q2= '你兒時住在哪區?'
q3 = '你最喜愛的嗜好?'
q1ans = 'computer'
q2ans = 'wong tai sin'
q3ans = 'guitar'

# matchid_HAD_(H/D/A)_c                  eg: 125904_HAD_H_c/ 125904_HAD_D_c/
# matchid_HDC_(H/A)_c                    eg: 125904_HDC_A_c/ 125904_HDC_H_c
type = '_HAD_H_c'
matchid = '125953'
bet = '10'

loginFlag= ''


def buy(type,matchid,bet,remainingBets):
    print(loginFlag)
    if(loginFlag == False):
        login()

    driver.switch_to.parent_frame()
    driver.switch_to.frame(driver.find_element_by_id('info'))

    driver.find_element_by_xpath(str('//*[@id="rmid' + matchid +'"]/td[1]/span/a')).click()

    # matchid_HAD_(H/D/A)_c                  eg: 125904_HAD_H_c/ 125904_HAD_D_c/
    # matchid_HDC_(H/A)_c                    eg: 125904_HDC_A_c/ 125904_HDC_H_c
    try:
        driver.switch_to.parent_frame()
        myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'info')))

    except TimeoutException:
        print("Loading took too much time!")
    driver.switch_to.frame(driver.find_element_by_id('info'))
    temp = matchid + type

    try:

        myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, temp )))

    except TimeoutException:
        print("Loading took too much time!")
    driver.find_element_by_id(temp).click()

    driver.find_element_by_xpath('//*[@id="oHeader_ALL"]/table/tbody/tr/td[4]/a/img').click()

    print(matchid, " ", type," ", bet+"HKD")

    # submit bets
    driver.switch_to.parent_frame()
    try:
        driver.switch_to.frame(driver.find_element_by_id('betSlipFrame'))
        driver.find_element_by_xpath('//*[@id="inputAmount0"]').click()
        driver.find_element_by_xpath('//*[@id="inputAmount0"]').clear()
        driver.find_element_by_xpath('//*[@id="inputAmount0"]').send_keys(bet)
        driver.find_element_by_xpath('//*[@id="pic_preview"]').click()
        driver.implicitly_wait(2)
        driver.switch_to.frame(driver.find_element_by_id('previewFrame'))
        if(remainingBets != 0):
            driver.find_element_by_xpath('//*[@id="pic_back"]').click()

        '''
        driver.find_element_by_xpath('//*[@id="pic_send_bet"]').click()
    
        driver.implicitly_wait(2)
    
        if(driver.find_elements_by_xpath(str("//*[contains(text(), 'BET REJECTED : 1')]"))):
            print('Bet Rejected!')
            if (driver.find_elements_by_xpath(str("//*[contains(text(), 'INSUFFICIENT BALANCE')]"))):
                print('INSUFFICIENT BALANCE')
    
        else:
            print('Bet Accepted!')
    
        '''
    except:
        print("Betting system close")
    time.sleep(3)
    driver.switch_to.parent_frame()
    driver.switch_to.parent_frame()
    driver.switch_to.frame(driver.find_element_by_id('info'))
    driver.find_element_by_xpath('//*[@id="topMenu"]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/a/img').click()

    time.sleep(3)




def login():

    driver.switch_to.frame(driver.find_element_by_id('betSlipFrame'))
    driver.find_element_by_id('account').click()
    driver.find_element_by_id('account').send_keys(username)
    driver.implicitly_wait(3)
    driver.find_element_by_id('passwordInput1').click()
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('pic_login').click()
    if (driver.find_elements_by_xpath(str("//*[contains(text(), '" + q1 + "')]"))):
        driver.find_element_by_id('ekbaDivInput').send_keys(q1ans)

    elif (driver.find_elements_by_xpath(str("//*[contains(text(), '" + q2 + "')]"))):
        driver.find_element_by_id('ekbaDivInput').send_keys(q2ans)

    else:
        driver.find_element_by_id('ekbaDivInput').send_keys(q3ans)
    driver.find_element_by_id('pic_confirm').click()
    driver.find_element_by_id('btn_enter').click()

    print('Login Successful')
    print(driver.find_element_by_id('valueAccName').text)
    print(driver.find_element_by_id('valueAccBal').text)
    loginFlag = True


def main():
    driver.get("http://bet.hkjc.com/football/default.aspx?lang=en")
    driver.implicitly_wait(1)
    login()
    buy(type,matchid,bet,1)
    buy(type, '125954',bet,0)
    driver.close()


main()



