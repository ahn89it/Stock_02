
import requests
from bs4 import BeautifulSoup
import ALL_CODE_LIST

def MAL_Function(x):
    url = "http://finance.daum.net/item/quote_avg_yyyymmdd_sub2.daum?code={0}".format(x)
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    test = soup.select('td span')
    array = [test[i].text for i in range(len(test))]
    array2 = []
    array2.append(int(array[2].replace(",", "")))
    array2.append(int(array[4].replace(",", "")))
    if(array2[1] < array2[0]):
        cal = (array2[1] / array2[0] - 1) * 100
    else:
        cal = 1

    return cal


#
# for i in range(402,2400):
#     print(MAL_Function(ALL_CODE_LIST.ALL_CODE_LIST[i]),i)


index = 1
for i in range(len(ALL_CODE_LIST.ALL_CODE_LIST)):
    k=1
    if ((MAL_Function(ALL_CODE_LIST.ALL_CODE_LIST[i]) > -0.2) & (MAL_Function(ALL_CODE_LIST.ALL_CODE_LIST[i]) <= 0) ):
        print (ALL_CODE_LIST.ALL_CODE_LIST[i], i, index )
        index +=1



