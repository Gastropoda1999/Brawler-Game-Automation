import profile
from re import I
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import *
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from time import sleep, time
from colorama import Fore , init
import time
import random
import os
from colorama import init , Fore
import requests
import sys

profilepath = r'C:\Users\Gastropoda\AppData\Roaming\Mozilla\Firefox\Profiles\o9urgzrk.test bot'
profile = webdriver.FirefoxProfile(profilepath)
option = webdriver.FirefoxOptions()
option.headless = True
driver = webdriver.Firefox(firefox_profile=profile , options=option )
init(autoreset=True)

token = 'BXZfVJeQ2n6LZI5CUO4156dUOQ5Bng4JmrtE0u2tX6c'   #line token

def clearpromp():
    clear = lambda: os.system('cls')
    clear()

#login bar
def login_progressbar(it, prefix="logging in ", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "█"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

def heal_progressbar(it, prefix="Healing ", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "█"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

clearpromp()

url = 'https://play.bcbrawlers.com/home'

driver.get(url)

#login in case needed
for i in login_progressbar(range(100)):
    time.sleep(0.05) # any calculation you need
try:
    login = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/button/div'))).click()
    login = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/span[1]'))).click()
    time.sleep(7)
    login = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/button/div'))).click()
    print('Login !')
    time.sleep(2)
    music = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[3]/div[1]/img'))).click()
    time.sleep(2)
    clearpromp()
except:
    pass

#check wam input health
wam = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[3]/div[1]/div/div/button'))).text
print(wam)
lowest_health_heal = input('heal when health = ')
lowest_health_heal = int(lowest_health_heal)

while True:
    try:
        #main mine
        clearpromp()
        Brawl_Button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[4]/div[3]/button[2]/div'))).click()
        time.sleep(5)
        Continue_Button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/button/div'))).click()
        time.sleep(5)

        #collect data and send to line
        Current_BrwlToken = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div[2]/div[1]/div[2]'))).text
        wax = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]'))).text
        usd = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[2]/div[3]/div[2]'))).text
        gold = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[1]/span[2]'))).text
        rate = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[3]/div[2]'))).text
        rate = rate.split()
        Current_health = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[4]/div[2]/div[2]/span'))).text
        payload = {'message' : '''
Brawling !
Brawl 💰 : {} Token 
Rate 💵 : {} wax
Gold ⭐ : {}
Health ❤️ : {}'''.format(Current_BrwlToken,rate[7],gold,Current_health)}
        r = requests.post('https://notify-api.line.me/api/notify'
            , headers={'Authorization' : 'Bearer {}'.format(token)}
            , params = payload)
        time.sleep(2)

        #heal function
        Current_health = Current_health.split('/')
        check_health = int(Current_health[0])

        if check_health <= lowest_health_heal:

            heal_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[2]/div/img'))).click()

            heal_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/input'))).click()

            heart_plus = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/span[2]'))).text

            heart_plus = heart_plus.split()
            heart_math = float(heart_plus[1])
            move_left = int(heart_math/0.05)
            #left arrow

            for i in range(move_left):
                    actions = ActionChains(driver)
                    actions.key_down(Keys.ARROW_LEFT).pause(0.001).key_up(Keys.ARROW_LEFT)
                    actions.perform()
                    i += 1

            heal = 10

            heal_amount = heal*20

            for i in range(heal_amount):
                actions = ActionChains(driver)
                actions.key_down(Keys.ARROW_RIGHT).pause(0.001).key_up(Keys.ARROW_RIGHT)
                actions.perform()
                i += 1

            heal_now = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[4]/button/div'))).click()

            healing_cost = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[1]/span[2]'))).text
            heart_plus = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[2]/span[2]'))).text
            print('--------------------')
            print(Fore.LIGHTYELLOW_EX +  "Healing Cost : {}".format(healing_cost))
            print(Fore.LIGHTRED_EX + "Health {}".format(heart_plus))
            print('--------------------')
            for i in heal_progressbar(range(100)):
                time.sleep(0.05)
            after_health = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[4]/div[2]/div[2]/span'))).text
            print(Fore.LIGHTRED_EX + 'Health : {}'.format(after_health))
            Current_BrwlToken = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div[2]/div[1]/div[2]'))).text
            print('')
            print('Done !')
            payload = {'message' : '''
Brawl Healing...
Healing Cost 💸 : {}
Increst Health {}
Brawl 💰 : {}
Health ❤️ : {}'''.format(healing_cost,heart_plus,Current_BrwlToken,after_health)}
            r = requests.post('https://notify-api.line.me/api/notify'
                , headers={'Authorization' : 'Bearer {}'.format(token)}
                , params = payload)
        else:
            pass

    except:
        clearpromp()
        print(Fore.LIGHTYELLOW_EX + 'Wallet : {}'.format(wam))
        print('')
        print(Fore.LIGHTRED_EX + 'Heal when health = {}'.format(lowest_health_heal))
        print('')
        #token
        Current_BrwlToken = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div[2]/div[1]/div[2]'))).text
        wax = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]'))).text
        usd = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[2]/div[3]/div[2]'))).text
        print(Fore.LIGHTMAGENTA_EX + 'Current Brawl : {} Token ({} wax) ({} USD)'.format(Current_BrwlToken,wax,usd))
        #rate
        rate = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[3]/div[2]'))).text
        rate = rate.split()
        print(Fore.LIGHTGREEN_EX + 'BRWL rate : {} wax'.format(rate[7]))
        #gold
        gold = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[1]/span[2]'))).text
        print(Fore.YELLOW + 'Gold : {}'.format(gold))
        #hp
        Current_health = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[4]/div[2]/div[2]/span'))).text
        print(Fore.LIGHTRED_EX + 'Health : {}'.format(Current_health))
        #ring
        Current_ring = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/span'))).text
        Current_ring = Current_ring.split()
        print(Fore.LIGHTBLUE_EX + 'Ring : {} Matches\n'.format(Current_ring[0]))


        Cooldown = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[4]/div[3]/span'))).text
        Cooldown = Cooldown.split(':')
        Min_CD = int(Cooldown[0])
        Sec_CD = int(Cooldown[1])
        Min_Convert = Min_CD * 60
        Total_CD = Min_Convert + Sec_CD
        t = Total_CD
        while t:
            mins, secs = divmod(t, 60)
            timer = 'Next Brawl : {:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1