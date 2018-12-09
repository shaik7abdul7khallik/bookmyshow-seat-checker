from selenium import webdriver
from selenium.webdriver.common.keys import Keys

site = "https://in.bookmyshow.com/buytickets/2-0-hyderabad/movie-hyd-ET00042213-MT/"
date="20181205"
venue ='ADHY'
show='07:15 PM'
driver = webdriver.Firefox()
driver.get(site+date);
print driver.title
elem=driver.find_element_by_id("venuelist");
elem1=elem.find_element_by_xpath("//li[@data-id='"+venue+"']");
elem2=elem1.find_element_by_link_text(show);
print elem2
elem2.send_keys(Keys.ENTER);
