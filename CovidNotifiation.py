from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C://Users//Anil j//Desktop//GUI Chatbot//coronavirus.ico",
        timeout = 10
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    while True:
        # notifyMe("Anil", "Lets stop the spread of this virus together")
        myHtmlData = getData('https://www.mohfw.gov.in/')

        soup = BeautifulSoup(myHtmlData, 'html.parser')
   
        myDataStr = ""
        for tr in soup.find_all('tbody')[1].find_all('tr'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]
        itemList = myDataStr.split("\n\n")

        states = ['Maharashtra', 'Telengana', 'Kerala']
        for item in itemList[0:26]:
            dataList = item.split('\n')
            if dataList[1] in states: 
                nTitle = 'Cases of Covid-19'
                nText = f"State {dataList[1]}\nIndian Nationals: {dataList[2]} \n Foreign Nationals : {dataList[3]}\nCured :  {dataList[4]}\nDeaths :  {dataList[5]}"
                notifyMe(nTitle, nText)
                time.sleep(2)
        time.sleep(3600)
