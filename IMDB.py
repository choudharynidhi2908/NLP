import requests
import matplotlib.pyplot as plt 
from bs4 import BeautifulSoup as sp  
import re 
from wordcloud import WordCloud


IM  = []






url = ('https://www.imdb.com/title/tt0068646/reviews?ref_=tt_ql_3')
response = requests.get(url)
#print(response)
reviews =response.content
#print(reviews)

reviews = sp(reviews,'html.parser')

#print(reviews)


reviews_only = reviews.findAll('div',attrs={'class':'text show-more__control'})

#print(reviews_only)

print(len(reviews_only))
for i in range((len(reviews_only))):
	reviews_only_str = (reviews_only[i].text)
	IM.append(reviews_only_str)


#print(reviews_only_str)

#IM_Clean = IM.split(" ")

#print(IM)

#IM_Clean = IM.split(" ")

IM_Clean_Single = " ".join(IM)
#print(IM_Clean_Single)

#IM_Clean_Single

IM_Clean_Single = re.sub("[^A-Za-z0-9]"," ",IM_Clean_Single).lower()



IM_Clean_Str = IM_Clean_Single.split(" ")

#print(IM_Clean_Str)

with open ('C:\\Users\\nidhchoudhary\\Desktop\\Assignment\\NLP\\stop.txt','r') as st:
	stopwords = st.read().split('\n')

print(stopwords)


IM_Clean_Str_stop =  (w for w in IM_Clean_Str if not w in stopwords)

print(IM_Clean_Str_stop)



