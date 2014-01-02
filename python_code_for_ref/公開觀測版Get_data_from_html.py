import urllib.request 
print ("Hellow word")

company_number = 4908
search_year  = 101
search_season = 1
# get html data
Stock_page = urllib.request.urlopen('http://mops.twse.com.tw/mops/web/ajax_t05st34?encodeURIComponent=1&step=1&firstin=1&off=1&keyword4=&code1=&TYPEK2=&checkbtn=&queryName=co_id&TYPEK=all&isnew=false&co_id=4908&year=101&season=01')
Stock_data = Stock_page.read().decode('utf-8')
#print (Stock_data)

# write files test
from bs4 import BeautifulSoup 
soup = BeautifulSoup(Stock_data)
soup_formal = soup.prettify()
#get formal data format
Formal_data = open("Formal_data.txt", "wb")
Formal_data.write(soup_formal.encode("utf-8"))
Formal_data.close()

resouce_data = open("Formal_data.txt","rb")
parsing_data = open("parsing_data.txt","w")
stock_input_data = BeautifulSoup(resouce_data.read().decode("utf-8"))
td_sum=""
#skip top two table
for table in stock_input_data.findAll("table")[2:]:
    #skip top four tr
    for tr in table.findAll("tr")[4:]:
        for td in tr.findAll("td"):            
            td_sum = td_sum + td.text.strip() + ";"           
            #td_sum = td_sum.replace('\n',';')
            #print(td.text)
        print(td_sum)
        wait = input("PRESS ENTER TO CONTINUE.")
        parsing_data.write(td_sum+"\n")
        td_sum="" #clear data   
parsing_data.close()
