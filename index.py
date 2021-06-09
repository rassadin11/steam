import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

URLS = {
	"URLS_1": {
		'1': 'https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Exterior%5B%5D=tag_WearCategory0&category_730_Quality%5B%5D=tag_normal&appid=730#p1_popular_desc',
		'2': 'https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Exterior%5B%5D=tag_WearCategory0&category_730_Quality%5B%5D=tag_normal&appid=730#p2_popular_desc',
	}
}

def parse():

	coms = []

	for parts in URLS.keys():
		for value in URLS['{}'.format(parts)].values():
			ua = UserAgent()

			HEADERS = {
				'User-Agent': ua.random,
			}

			response = requests.get(value, headers = HEADERS);

			soup = BeautifulSoup(response.content, 'html.parser')
			items = soup.findAll('div', class_ = 'market_listing_row market_recent_listing_row market_listing_searchresult')

			for item in items: 
				title = item.find('span', class_ = 'market_listing_item_name').get_text(strip = True)
				cost = item.find('span', class_ = 'normal_price', attrs = {"data-currency": 1}).get_text()

				def get_quality():
					a = title.find('(')
					b = title.find(')')
					quality = title[a+1:b].strip()
					
					return quality

				coms.append({
					'title': title,
					'cost': cost,
					'quality': get_quality(),
				}) 

	for com in coms:
		print(com['title'], com['cost'], com['quality'])
				
parse()
