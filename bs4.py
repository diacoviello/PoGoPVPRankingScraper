
# from bs4 import BeautifulSoup
# import requests
#
# # Example URL (replace this with the URL you want to scrape)
# url = 'https://pvpoke.com/rankings/all/2500/overall/'
#
# # Fetch the page content
# response = requests.get(url)
# html_content = response.text
#
# # Parse the HTML content with BeautifulSoup
# soup = BeautifulSoup(html_content, 'html.parser')
#
# # Find the div you are interested in
# # Replace 'my-div' with the actual class, id, or other attribute you are looking for
# div = soup.find('div', {'class': 'rankings-container'})
#
# if div:
#     print("Found div:")
#     print(div.prettify())  # Print the div with its children in a formatted way
# else:
#     print("Div not found")
#
# # Optionally, find specific children within the div
# if div:
#     children = div.find_all(recursive=True)  # Finds only direct children
#     for child in children:
#         print("Child tag:")
#         print(child.prettify())

