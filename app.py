from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


import time
import os


from flask import Flask, request



def browserLoad(link):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.binary_location = os.environ.get["GOOGLE_CHROME_BIN"]
    drvr = webdriver.Chrome(options = options,executable_path= os.environ.get["CHROMEDRIVER_PATH)"])
    drvr.get(link)
    return drvr

# link = input("Enter the sheets url- ")
# name = input("Enter name- ")
# email = input("Enter email- ")
def update(name,email):
    link = 'https://docs.google.com/spreadsheets/d/1f3tTMc9CnTgEqugBT5UtR57RE2Pj49Q1r0RlCrrXevI/edit#gid=0'
    drvr = browserLoad(link)

    xpath = '//*[@id="t-formula-bar-input"]/div'

    bar = drvr.find_element_by_xpath(xpath)


    try:
        present_count = int(bar.text)
    except:
        raise TypeError("Invalid count")

    new_count  = present_count + 1

    print(new_count)

    bar.send_keys(Keys.BACKSPACE)
    bar.send_keys(new_count)
    bar.send_keys(Keys.ENTER)

    for _  in range(new_count):
        bar.send_keys(Keys.ENTER)

    bar.send_keys(new_count)
    time.sleep(2)
    bar.send_keys(Keys.TAB)

    bar.send_keys(name)
    time.sleep(2)
    bar.send_keys(Keys.TAB)

    bar.send_keys(email)
    time.sleep(5)
    bar.send_keys(Keys.TAB)
    time.sleep(5)

    drvr.close()




app = Flask(__name__)


@app.route("/",methods = ['POST', 'GET'])
def hey():
    data = request.json
    print(request.json)
    update(data["name"],data["email"])
    return "Test"



if __name__ == "__main__":
    app.run(host='0.0.0.0')
