from selenium import webdriver   
from bs4 import BeautifulSoup as bs 
import mysql.connector
driver=webdriver.Chrome("C:/Users/RIL/Desktop/chromedriver")
brand=''
name=''
dprice=0
oprice=0
mysql_="""INSERT INTO data (tittle,tpe,dprice,oprice) VALUES (%s, %s, %s, %s)"""
mydb=mysql.connector.connect(host="127.0.0.1",user="root",password="SYSTEM",database="myntra")
cur=mydb.cursor()
for i in range(1,50):
	url="https://www.myntra.com/men-tshirts?p=" + str(i)
	driver.get(url)
	content = driver.page_source
	soup = bs(content,"html.parser")
	container=soup.findAll('li',{'class':'product-base'})
	for con in container:
		c=con
		c1=c.findAll("a",href=True)
		c2=c1[0]
		c3=c2.findAll('div',{'class':'product-productMetaInfo'})
		brand=c3[0].h3.text
		name=c3[0].h4.text
		c4=c3[0]
		c5=c4.div.span
		if(c5.span!=None):
			dprice=int(c5.span.text[4:])
			c7=c5.findAll('span',{'class':'product-strike'})
			c8=c7[0]
			oprice=int(c8.text[4:])
		else:
			dprice=int(c5.text[4:])
			oprice=int(c5.text[4:])
		rt=(brand,name,dprice,oprice)	
		cur.execute(mysql_,rt)
mydb.commit()
cur.close()
print("updated")	    	
	

