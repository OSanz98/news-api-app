import os
import requests
from send_email import send_email

api_key = os.getenv("NEWS_API_APP_KEY")
url = "https://newsapi.org/v2/everything?q=apple&from=2023-09-28&to=2023-09-28&sortBy=popularity&apiKey" \
       f"={api_key}"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

print(content)

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None and article["author"] is not None and article["url"] is not None:
        body = body + article["title"] + "\n" + article["author"] + "\n" + article["url"] + 2*"\n"

# body = body.encode("utf-8")
send_email(content=body)
