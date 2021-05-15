import requests, lxml
from bs4 import BeautifulSoup as bs
import csv


main_lnk='https://www.facebook.com/messages/t/anushka.pokharel.3304'
main_source = requests.get(main_lnk).text
print(main_source)
s_code = bs(main_source, 'lxml')
print(s_code.find('span', data_text="true"))


# main_table = s_code.find('table', class_='table my-table')
# rows = main_table.find_all('tr')

# rows = []
# for data in datas:
#     data = data.find_all('td')
#     row = [data[0].text, str('\'') + str(data[1].text) + str('\''), data[2].text, data[3].text, data[4].text,
#            data[5].text, data[6].text, data[7].text]
#     rows.append(row)
