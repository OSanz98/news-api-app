import os
import requests

api_key = os.getenv("NEWS_API_APP_KEY")
url = ("https://newsapi.org/v2/everything?q=apple&from=2023-09-28&to=2023-09-28&sortBy=popularity&apiKey"
       "=4ac12bae2df943f98563f7e6f6221215")

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

print(content)

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["author"])
