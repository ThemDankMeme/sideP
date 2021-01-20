import requests
import bs4

base = 'https://books.toscrape.com/catalogue/page-{}.html'
two_star = []
for n in range(1,51):
	scrape_url = base.format(n)
	res = requests.get(scrape_url)
	soup = bs4.BeautifulSoup(res.text, 'lxml')
	books = soup.select('.product_pod')
	for book in books:
		if len(book.select('.star-rating.Two')) != 0:
			book_title = book.select('a')[1]['title']
			two_star.append(book_title)
for book in two_star:
	print(book)
