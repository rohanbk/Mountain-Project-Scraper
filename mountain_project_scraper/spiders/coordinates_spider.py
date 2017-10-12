import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CoordinatesSpider(scrapy.Spider):
    name = 'coordinates'
    domain = 'https://www.mountainproject.com'
    start_urls = [domain + '/v/washington/105708966'] #replace this with mountain project homepage
    allowed_domains = ['mountainproject.com']
    rules = [
        Rule(
            LinkExtractor(allow='v/(.+)'),
            callback='parse',
            follow=True
        )
    ]

    def parse(self, response):
        links = response.css('#viewerLeftNavColContent a[target="_top"] ::attr(href)').extract()
        for url in links:
            yield scrapy.Request(self.domain + url, callback=self.parse_coordinates)

    def parse_coordinates(self, response):
        area_name = response.css('h1.dkorange em ::text').extract_first().strip()
        lat_long_string = self.process_latitude_longitude(response)

        try:
            yield {
                'area_name': area_name,
                #'parents': response.css('#navBox div ::text').extract(),
                #'child_areas': response.css('#viewerLeftNavColContent a[target="_top"] ::text').extract(),
                'latitude' : lat_long_string.split(',')[0],
                'longitude' : lat_long_string.split(',')[1]
            }
        except IndexError:
            pass
        links = response.css('#viewerLeftNavColContent a[target="_top"] ::attr(href)').extract()
        for url in links:
            yield scrapy.Request(self.domain + url, callback=self.parse_coordinates)

    def process_latitude_longitude(self,response):
        if("Location" not in response.css('#rspCol800 div.rspCol table tr:nth-child(2) td ::text').extract()[0]):
            return response.css('#rspCol800 div.rspCol table tr:nth-child(3) td ::text').extract()[1].strip()
        else:
            return response.css('#rspCol800 div.rspCol table tr:nth-child(2) td ::text').extract()[1].strip()
