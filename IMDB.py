import requests
import matplotlib.pyplot as plt 
from bs4 import BeautifulSoup as sp  
import re 
from wordcloud import WordCloud
from selenium import webdriver
browser = webdriver.Chrome('C:\\Users\\nidhchoudhary\\Downloads\\chromedriver_win32\\chromedriver.exe')
IM  = []
import time
url = ('https://www.imdb.com/title/tt0068646/reviews?ref_=tt_ql_3')

browser.get(url)
i= 1
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
while (i<2):
    try:
        button = browser.find_element_by_xpath('//*[@id="load-more-trigger"]')
        button.click()
        time.sleep(5)
        pag_content = browser.page_source
        pag_content_Clean = sp(pag_content,"html.parser")
        pag_content_Exact = pag_content_Clean.findAll('div',attrs= {'class':'text'})
        IM.extend(pag_content_Exact)
        i = i+1
    except NoSuchElementException:
    	break 
    except ElementNotVisibleException:
    	break 
pgc = []   	
for i in range(len(pag_content_Exact)):
	pgc.append(pag_content_Exact[i].text)



#print(pgc)

content = " ".join(pgc)

pag_content_Clean = re.sub("[^A-Za-z]"," ",content).lower()

pag_content_Clean = pag_content_Clean.split("/n")




with open ('C:\\Users\\nidhchoudhary\\Desktop\\Assignment\\NLP\\stop.txt','r') as st:
 	stopwords = st.read().split('\n')


IM_Clean_Str_stop =  [w for w in pag_content_Clean if not w in stopwords]

#print(IM_Clean_Str_stop)

with open ('C:\\Users\\nidhchoudhary\\Desktop\\Assignment\\NLP\\positive-words.txt','r') as pt:
    pos= pt.read().split("\n")


pos_word = pos[36:]

IM_Clean_Str_pos = [ w for w in pag_content_Clean if w in pos_word]


wordcloud_positive = " ".join(IM_Clean_Str_pos)

wordcloud_pos = WordCloud(background_color= 'red',
	width = '1500',
	height = '1500').generate(wordcloud_positive)

plt.imshow(wordcloud_pos)
plt.show()




