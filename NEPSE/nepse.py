import requests, lxml
from bs4 import BeautifulSoup as bs
import csv
import datetime

today = datetime.datetime.now()
today=str(today).replace('-','')[:8]
# print(today)
today='20200709'

page_index=1
req_no=0
total_page=0

fields = ['S.No:','Contract No:','Stock Symbol','Buyer Broker','Seller Broker','Quantity','Rate','Amount']
filename = "nepse.csv"
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)

def nepse(main_lnk='http://www.nepalstock.com/floorsheet'):
        global req_no
        try:
            main_source = requests.get(main_lnk).text
            s_code = bs(main_source, 'lxml')
            main_table=s_code.find('table',class_='table my-table')
            rows = main_table.find_all('tr')
        except:
            req_no=req_no+1
            print("Something went wrong. Retrying.....Request no: "+str(req_no))
            nepse(main_lnk)
            return
        datas = rows[2:-3]

        rows=[]
        for data in datas:
            data=data.find_all('td')
            row=[data[0].text,str('\'')+str(data[1].text)+str('\''),data[2].text,data[3].text,data[4].text,data[5].text,data[6].text,data[7].text]
            rows.append(row)

        with open(filename, 'a+', newline='') as write_obj:
            csv_writer = csv.writer(write_obj)
            csv_writer.writerows(rows)
            # print(rows)

def ScrapAll():
    global total_page, req_no

    main_lnk = 'http://www.nepalstock.com/floorsheet'
    main_source = requests.get(main_lnk).text
    s_code = bs(main_source, 'lxml')
    pager=s_code.find('div',class_='pager')
    last_pager=pager.find('a',title='Last Page')
    last_pager=last_pager['href']
    total_page=str(last_pager).split('/')
    total_page=total_page[6]
    total_page=int(total_page)

    nepse()

    for page_index in range(2,total_page+1,1):
        req_no=0
        lnk = 'http://www.nepalstock.com/main/floorsheet/index/' + str(page_index) + '/'
        # print(lnk)
        nepse(main_lnk=lnk)
        print(page_index)

ScrapAll()
