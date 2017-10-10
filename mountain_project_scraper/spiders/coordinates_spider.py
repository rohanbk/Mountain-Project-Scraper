import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class CoordinatesSpider(scrapy.Spider):
    name = 'coordinates'
    start_urls = ['https://www.mountainproject.com/v/kansas/107235316'] #replace this with mountain project homepage
    allowed_domains = ['mountainproject.com']
    rules = [
        Rule(
            LinkExtractor(
                allow='/v/(.+)/'),
            callback='parse_coordinates'
        )
    ]

    def parse_coordinates(self, response):
        return {
            'sidebar_links': response.css('#viewerLeftNavColContent a[target="_top"]').extract(),
            'coordinates': self.process_gps_coordinates(response)
        }

    # helper function to take HTML response object and product object contains latitude and longitude
    def process_gps_coordinates(self, response):
        # produce string in format 'XXX.XXX,XXX.XXX'
        lat_long_string = re.search(r"q=[^&]*", response.css('#rspCol800 div.rspCol table tr:nth-child(2) td').extract()[1]).group(0)[2:]
        return {
            'latitude' : lat_long_string.split()[0],
            'longitude' : lat_long_string.split()[1]
        }


