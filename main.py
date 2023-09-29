import os

api_key = os.getenv("NEWS_API_APP_KEY")
print(api_key)
# url = ("https://newsapi.org/v2/everything?q=apple&from=2023-09-28&to=2023-09-28&sortBy=popularity&apiKey"
#        f"={api_key}")
#
# # Make a request
# request = requests.get(url)
#
# # Get a dictionary with data
# content = request.json()

# Access the article titles and description
# for article in content["articles"]:
#     print(article["title"])
