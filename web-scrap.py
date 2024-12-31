import requests
from bs4 import BeautifulSoup

# Step 1: Send a request to the website
url = "https://www.w3schools.com/python/"  # Replace with the target URL
response = requests.get(url)

# Step 2: Parse the HTML content of the page
soup = BeautifulSoup(response.text, "html.parser")

# soup.find_all(name, attrs, recursive, string, limit)
# name: The tag name (like 'a', 'div', etc.).
# attrs: A dictionary of attributes to filter by (e.g., class, id, etc.).
# string: A string or regular expression to search for specific text within the tag.
# limit: Limits the number of results returned.

# How to Filter by Class or ID:
# By Class: Use the class_ keyword argument.
# By ID: Use the id keyword argument.

# Find all 'div' elements with class 'example-class'
# data = soup.find_all("h2")

# for i in data:
#     print(i.text)


links = soup.find_all("a")

# Loop through the links and print them
for link in links:
    href = link.get("href")
    print(href)
