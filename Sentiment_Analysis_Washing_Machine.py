import requests 
import re
from bs4 import BeautifulSoup as bs
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib 
print(matplotlib.get_backend())
matplotlib.use('Qt5Agg')

WM = []


for i in range(1,7):
    WM_Reviews = []
    url = 'https://www.amazon.in/Samsung-Fully-Automatic-Loading-WW80J4243MW-TL/product-reviews/B07G4TCDQ5/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber='+str(i)
    response = requests.get(url)
    #print(response)
    reviews = response.content
    #print(reviews)
    reviews = bs(reviews,"html.parser")
    #print(reviews)
    reviews_body = reviews.findAll('span',attrs={'class':'a-size-base review-text review-text-content'})
    #print(reviews_body)
    for i in range(len(reviews_body)):
    	WM_Reviews.append(reviews_body[i].text)
    	#ip.append(reviews[i].text)  
    	
    WM = WM + WM_Reviews
    #print(WM)
#with open("Washin_Machine_reviews.txt","w",encoding= 'utf-8') as output:
    #output.write(str(WM))
# as output:
    #output.write(str(WM))
    #WM = WM + WM_Reviews
print('First...............................................') 
print(WM)   
print('End...............................................') 
Washing_Machine_Single = " ".join(WM)
print(Washing_Machine_Single)
Washing_Machine = re.sub("[^A-Za-z0-9" "]+"," ",Washing_Machine_Single).lower()
#print('start...............................................')
#print(Washing_Machine)
#Washing_Machine = re.sub("[0-9" "]+"," ",Washing_Machine_Single)
with open ('C:\\Users\\nidhchoudhary\\Desktop\\Assignment\\NLP\\stop.txt','r') as st:
	stopwords = st.read()
#stopwords =stopwords.words("english")
   
stopwords = stopwords.split("\n")
Washing_Machine_Words = Washing_Machine.split(" ")
Washing_Machine_Words_req = (i for i in Washing_Machine_Words if not i in stopwords)

#print('End...............................................')
#print(Washing_Machine_Words)

Washing_Machine_Wd =" ".join(Washing_Machine_Words_req)
#print(Washing_Machine_Wd)
from os import environ

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

if __name__ == "__main__":
    suppress_qt_warnings()
#print('ABCD')
#qputenv("QT_AUTO_SCREEN_SCALE_FACTOR", "1");
wordcloud_ip = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(Washing_Machine_Wd)

plt.imshow(wordcloud_ip)
plt.show()

with open('C:\\Users\\nidhchoudhary\\Desktop\\Assignment\\NLP\\positive-words.txt','r') as pos:
	positive_words = pos.read().split("\n")
positive_words = positive_words[36:]
#print(positive_words)

washing_machine_splitted =  Washing_Machine_Wd.split(" ")
washing_machine_senti = (w for w in washing_machine_splitted if w in positive_words)
washing_machine_senti_join = " ".join(washing_machine_senti)

wordcloud_ip_pos = WordCloud(
	                            background_color='black',
                                width=1800,
                                height=1400
                                ).generate(washing_machine_senti_join)

plt.imshow(wordcloud_ip_pos)
plt.show()

with open('C:\\Users\\nidhchoudhary\\Desktop\\Assignment\\NLP\\negative-words.txt','r') as neg:
	negative_words = neg.read().split("\n")
negative_words = negative_words[37:]

Washin_Machine_negative = (w for w in washing_machine_splitted if w in negative_words)
washing_machine_senti_neg = " ".join(Washin_Machine_negative)

wordcloud_ip_neg = WordCloud(
                               background_color = 'black',
                               width=1800,
                               height = 1400
                               ).generate(washing_machine_senti_neg)
plt.imshow(wordcloud_ip_neg)
plt.show()
