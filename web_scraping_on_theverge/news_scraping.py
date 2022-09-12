# Importing required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Accessing the HTML content from webpage
url = "https://www.theverge.com/"
response = requests.get(url)
if response.status_code == 200:
    print("Successfully connected to the website.")
else:
    print("Not connected to the website.")

# Parsing the HTML content
soup = BeautifulSoup(response.content, 'html5lib')

# Searching and navigating through the parse tree
urls, headlines, authors, dates = [], [], [], []
table = soup.find('main', attrs={'id':'content'})
if table is not None:
  for main in table.findAll('div', attrs={'class':'c-compact-river'}):
      for row in main.findAll('div', attrs={'class':'c-compact-river__entry'}):
          element = row.find('h2', attrs={'class':'c-entry-box--compact__title'})
          url = element.a['href']
          if url is not None:
              text = url
          else:
              text = None
          urls.append(text)

          headline = element.a.text   
          if headline is not None:
              text = headline
          else:
              text = None
          headlines.append(text)

          author = row.find('span', attrs={'class':'c-byline__author-name'})
          if author is not None:
              text = author.text
          else:
              text = None
          authors.append(text)

          element = row.find('div', attrs={'class':"c-byline"})
          if element is not None:
              ele = element.find('time', attrs={'data-ui':"timestamp"})                 
              if ele is not None:
                  datetime = ele['datetime']
                  if datetime is not None:
                    date = datetime.split('T')[0]
                    text = date
                  else:
                    text = None
              else:
                  text = None
          else:
              text = None
          dates.append(text)

# Creating Dataframe
column_names = ['url', "headline", "author", "date"]  
news = pd.DataFrame(columns=column_names)
news['url'] = urls
news['headline'] = headlines
news['author'] = authors
news['date'] = dates

# Creating CSV file
csv_file_path = "news.csv"
new_file = open(csv_file_path, "x")

# Storing data in a created csv file
# Remover column header and index
news.to_csv(csv_file_path, index=False)
