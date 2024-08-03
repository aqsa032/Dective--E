import requests 
import string
import openpyxl
import pandas as pd
import nltk
from nltk import sent_tokenize,word_tokenize


from bs4 import BeautifulSoup
#enter the url here to extract the content and perform data analysis
url = 'https://insights.blackcoffer.com/challenges-and-opportunities-of-big-data-in-healthcare/'
response = requests.get(url)


soup = BeautifulSoup(response.content, 'html.parser')
title = soup.find_all('title').get_text()
print(title)


a=soup.find(class_='td-post-content').get_text()
print(a)


with open('pos.txt', 'r') as f:
    positive_words = f.read().splitlines()

with open('neg.txt', 'r') as f:
    negative_words = f.read().splitlines()
    

words = a.lower().split()

pscore = 0
nscore = 0
for word in words:
    if word in positive_words:
        pscore += 1
    elif word in negative_words:
        nscore += 1
        


#printing positive and negetive score
print(pscore)
print(nscore)

totalscore=pscore+nscore
  
#polarity score
polarity = (pscore-nscore)/((pscore+nscore)+0.000001)
print(polarity)


#total sentence!!!
a_tokens=sent_tokenize(a)
s=len(a_tokens)
print(s)


#total word!!
a_tokens=word_tokenize(a)
a_tokens

t=len(a_tokens)
print(t)


#avg sentence!!!
avgsen=round(t/s)
print(avgsen)



#personal pronouns

with open('para.txt', 'r') as f:
     personalpro= f.read().splitlines()
    
     

pro=0
for word in words:
    if word in personalpro:
       
       pro += 1


print(pro)

#average word length
words=a.lower().split()
avrg=sum(len(word) for word in words)/len(words)
print(round(avrg))


#subjective score

#last part

wb = openpyxl.Workbook()
ws = wb.active
thisdict={
    "positive_score":pscore,
    "negitive_score":nscore,
    "polarity score":polarity,
    "total_sentance":s,
    "total_words":t,
    "avg_sentance":avgsen,
    "avg_word":avrg,
    "personalpronoun":pro

}
# convert into dataframe
df = pd.DataFrame(data=thisdict, index=[1])

#convert into excel
df.to_excel("thisdict.xlsx", index=False)
print("Dictionary converted into excel...")


# for i in data:
#     #print(data)
#     ws.append(i)



