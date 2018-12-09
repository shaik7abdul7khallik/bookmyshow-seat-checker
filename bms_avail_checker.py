from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
date='20181209'
site = 'https://in.bookmyshow.com/buytickets/2-0-hyderabad/movie-hyd-ET00088720-MT/'+date
venue ='ADHY'
show='10:45 PM'
# rows=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
rows=['A','B','C','D','E','F']
numOfSeats='1'
driver = webdriver.Firefox()
driver.get(site)
cityelem=driver.find_element_by_link_text("Hyderabad")
cityelem.click()
elem=driver.find_element_by_id("venuelist")
elem1=elem.find_element_by_xpath("//li[@data-id='"+venue+"']")
elem2=elem1.find_element_by_link_text(show)
elem2.click()
AcceptPopUp=driver.find_element_by_id("tnc")
AcceptButton=driver.find_element_by_link_text("Accept")
AcceptButton.click()
SeatsPopUp=driver.find_element_by_id("qty-sel")	
time.sleep(5)
SeatsNumberLayoutClass=SeatsPopUp.find_element_by_class_name("__list")
SeatsNumberLayout=SeatsNumberLayoutClass.find_element_by_id("popQty")
seats1=SeatsNumberLayout.find_element_by_id("pop_1")
seats1.click()
proceed=SeatsPopUp.find_element_by_id("proceed-Qty")
proceed.click()
seatsTablePage=driver.find_element_by_id("seatcall")
seatsLayout=seatsTablePage.find_element_by_id("layout")
seatsTable=seatsLayout.find_element_by_class_name("setmain")
seatsTableBody=seatsTable.find_element_by_tag_name('tbody')
seatsRowsArray=seatsTableBody.find_elements_by_tag_name('tr')
for seatRowIndex in range(1,len(seatsRowsArray)):
	seatTDs=seatsRowsArray[seatRowIndex].find_elements_by_tag_name('td')
	if seatTDs[0].text in rows:
		print('-------------')
		print(seatTDs[0].text)
		print('Available Seats')
		seatsArr=seatTDs[1].find_elements_by_tag_name('div')
		for seat in seatsArr:
			try:
				seataRef=seat.find_element_by_class_name('_available')
				print(seataRef.text)
			except:
				pass
