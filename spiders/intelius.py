import scrapy
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import HtmlXPathSelector

people_sites = ['www.whitepages.net', 'www.intelius.com','www.peoplefinder.com' ]

for site in list(people_sites):
    if not random.randint(0,2):
        print('Completed all sites')
        break
    else:
class Intelius_Bhart(Spider):
    name = "intelius"
    allowed_domains = ["intelius.com"]
    start_urls = ['https://www.intelius.com/people-search/Benjamin-Smith/MT']
   #Results = name() #Name search results field

def parse(self, response):
    hxs = HtmlXPathSelector(response)
    items = []
    item = InteliusItem()
    item["Results"] = response.xpath('//*[@id="pagecontent"]/div[4]/div/div/div/div[1]/div/div[2]/span/a').extract()
    return item

