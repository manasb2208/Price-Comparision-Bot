from selenium import webdriver
import time
cd = "C:\\Users\\Manas\\Desktop\\chromedriver.exe" #replace this with your chromedriver location
driver = webdriver.Chrome(cd)
driver.get("https://www.flipkart.com/hp-omen-core-i5-10th-gen-8-gb-512-gb-ssd-windows-10-home-4-graphics-nvidia-geforce-gtx-1650-15-ek0015tx-gaming-laptop/p/itmbe839a51c8391?pid=COMFTRJFSTNBR4JS&lid=LSTCOMFTRJFSTNBR4JSWZWCNB&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=36d6feb8-2912-495c-80e7-55715dd40147.COMFTRJFSTNBR4JS.SEARCH&ppt=sp&ppn=sp&ssid=0a6h17rs680000001606296024349&qH=fbb680d39c2bc7e1")#replace with the flipkart product url of your choice 
time.sleep(5)
fp = driver.find_element_by_xpath('//div[@class = "_30jeq3 _16Jk6d"]').text
#print(fp)
#print(type(fp))
fp = fp[1:].split(',')
fp3 =""
for i in fp:
	fp3 = fp3 + i
fp3 = float(fp3)
#print(fp4, type(fp4))
driver.get('https://www.amazon.in/HP-Processor-15-6-inch-i5-10300H-15-ek0015TX/dp/B08CGLDF1S/ref=sr_1_1_sspa?adgrpid=77115748924&dchild=1&ext_vrnc=hi&gclid=CjwKCAiAnvj9BRA4EiwAuUMDf23eF3oMkrA1JMRnq47Eq4AJ3tgSS3CzUDR_-gI5nr72CFVsQ75eYhoCKz4QAvD_BwE&hvadid=379961472673&hvdev=c&hvlocphy=9301995&hvnetw=g&hvqmt=b&hvrand=7026440480501416510&hvtargid=kwd-544347035472&hydadcr=15673_1973939&keywords=hp+omen+15+amazon&qid=1606295889&sr=8-1-spons&tag=googinhydr1-21&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNjU5OTRLRzg2Slc0JmVuY3J5cHRlZElkPUEwNzYxNzczM1A1UDJZOFo0MlFCMSZlbmNyeXB0ZWRBZElkPUEwMzcyMzY4Nk5DOURLNjdYWERQJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==')#replace with the amazon product url of your choice 
time.sleep(10)
ap = driver.find_element_by_xpath('//span[@class = "a-size-medium a-color-price priceBlockBuyingPriceString"]').text
#print(ap)
ap  = ap[1:].split(',')
ap3 = ""
for i in ap:
	ap3 = ap3 + i
ap3 = float(ap3)
#print(ap4, type(ap4))
if ap3 > fp3:
	print('buy from flipkart')
elif ap3<fp3:
	print('buy from amazon')
else:
	print('buy from anywhere')