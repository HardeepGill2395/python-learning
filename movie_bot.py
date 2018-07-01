import requests
import bs4
import os
import sys
url = "http://www.imdb.com/search/title?release_date=2016&sort=user_rating,desc&ref_=adv_nxt&page="

titles_data = [] 
ratings_data = []
generes_data = []

def scrapData():
    title_class = ".lister-item-header"
    rating_class = ".ratings-bar"
    genre_class = ".genre"
        
    print("fetching...")
    for num in range(1,3):

        r = requests.get(url+str(num))
        rsoup = bs4.BeautifulSoup(r.text,from_encoding='utf-8')
        titles = rsoup.select(title_class)
        ratings = rsoup.select(rating_class)
        genres = rsoup.select(genre_class)

        for i in range(len(titles)):
                    t = titles[i].find('a').getText()
                    titles_data.append(t)

        for i in range(len(genres)):
                   generes_data.append(genres[i].getText().replace('\n',''))

        for i in range(len(ratings)):
                   ratings_data.append(ratings[i].find('strong').getText())
        
        print("Received...",len(titles_data),len(ratings_data),len(generes_data))
    print(len(titles_data))
    with open('imdb_database.txt','w') as f:
        for i in range( min( len(titles_data),min(len(ratings_data),len(generes_data))) ) :
            f.write(str(titles_data[i])+","+str(ratings_data[i])+","+str(generes_data[i])+"\n")

scrapData()
