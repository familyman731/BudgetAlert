from selenium import webdriver
import time
import datetime
import shutil
from bs4 import BeautifulSoup

def downloadMintData():

    browser = webdriver.Chrome("C:\ChromeDriver\chromedriver.exe")
    browser.get('https://accounts.intuit.com/index.html?offering_id=Intuit.ifs.mint&namespace_id=50000026&redirect_url=https%3A%2F%2Fmint.intuit.com%2Foverview.event%3Futm_medium%3Ddirect%26cta%3Dnav_login_dropdown')
    emailElem = browser.find_element_by_id('ius-userid')
    emailElem.send_keys('quinn.angrick@gmail.com')
    passwordElem = browser.find_element_by_id('ius-password')
    passwordElem.send_keys('G#UIg26skPBM%v')
    browser.find_element_by_id("ius-sign-in-submit-btn-text").click()
    time.sleep(10)

    html = browser.page_source
    soup = BeautifulSoup(html)
    # with open('test.txt','w+') as f:
    #     f.write(str(soup))
    balances = {}

    test = soup.findAll('li',{'class': 'accounts-data-li'})
    for li in soup.findAll('li',{'class': 'accounts-data-li'}):
        bank = li.find('span',{'class': 'nickname'}).contents[0]
        acct = li.find('a',{'class': 'accountName'}).contents[0]
        bal = li.find('span',{'class': 'balance'}).contents[0]
        balances[bank + " " + acct] = bal

    browser.get("https://mint.intuit.com/transactionDownload.event?queryNew=&offset=0&filterType=cash&comparableType=8")
    time.sleep(5)
    browser.close()

    transFileName = datetime.datetime.now().date().strftime("%Y-%m-%d") + ".csv"
    transPath = r"C:\Users\Quinn\PycharmProjects\Mint\Data/" + transFileName
    shutil.move(r"E:\Downloads\transactions.csv",transPath)

    return balances, transPath

if __name__ == "__main__":
    downloadMintData()