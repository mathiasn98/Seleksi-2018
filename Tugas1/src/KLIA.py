#Mathias Novianto
#13516021
#Tugas Seleksi Lab Basis Data
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time
import json
import os

#make soup of all flight to json
def allFlightToDictionary(all_flight, type):
    dictionaryList = []
    for flight in all_flight:
        flightData = flight.findAll("td")
        flightDictionary = {}
        if(type == "arrival"):
            if(len(flightData)<7):
                continue
            flightDictionary['from'] = flightData[0].text
            flightDictionary['to'] = flightData[1].text
            flightDictionary['code'] = flightData[3].text
            flightDictionary['status'] = flightData[4].text
            flightDictionary['sta'] = flightData[5].text
            flightDictionary['eta'] = flightData[6].text
        else:
            if(len(flightData) < 9):
                continue
            flightDictionary['from'] = flightData[0].text
            flightDictionary['to'] = flightData[1].text
            flightDictionary['code'] = flightData[3].text
            flightDictionary['status'] = flightData[4].text
            flightDictionary['std'] = flightData[5].text
            flightDictionary['etd'] = flightData[6].text
            flightDictionary['gate'] = flightData[7].text
            flightDictionary['checkin'] = flightData[8].text
        dictionaryList.append(flightDictionary)
    return dictionaryList

def dumpToJSONFile(jsonFile,json_file):
    output_path = '.'
    with open(os.path.join(output_path,json_file),'w') as f_out:
        json.dump(jsonFile,f_out)

#example web
#http://www.klia.com.my/index.php?m=airport&c=flight_schedule_details&date=2018-05-01&flighttype=departure&aid=1
klia_base_web_beginning = "http://www.klia.com.my/index.php?m=airport&c=flight_schedule_details&date="
klia_base_web_end = "=departure&aid=1"
#date format : yyyy-mm-dd, example : date = '2018-05-07'
print("Please enter date you want to search : ")
date = input()
#can be departure or arrival, example : flightType = 'arrival'
print("Please enter type of flight you want to search (departure/arrival) : ")
flightType = input()

klia_full_web = klia_base_web_beginning+date+"&flighttype="+flightType+klia_base_web_end
open_klia_web = uReq(klia_full_web)
raw_html = open_klia_web.read()
klia_soup = soup(raw_html,'html.parser')
all_flight = klia_soup.findAll("tr")
data = allFlightToDictionary(all_flight[1:],flightType)
dumpToJSONFile(data, date + "_" + flightType+".json")
#print("Total data ada : " + str(len(data)))
#print(data)

print("Process done ! Please check the json file")
