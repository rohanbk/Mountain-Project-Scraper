import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

AREA_PREFIXES = re.compile(r'(\([A-Za-z0-9\.]+\))|\"|\u0092|\u0091')


class CoordinatesSpider(scrapy.Spider):
    name = 'coordinates'
    domain = 'https://www.mountainproject.com'

    # format should be /destinations or /v/STATENAME/ID
    relativeURL = '/v/hawaii/106316122'

    start_urls = [domain + relativeURL]
    allowed_domains = ['mountainproject.com']
    rules = [
        Rule(
            LinkExtractor(allow='v/(.+)'),
            callback='parse',
            follow=True
        )
    ]

    def parse(self, response):
        # use the following links variable if testing from an individual state page (e.g. WA states routes)
        links = response.css('#viewerLeftNavColContent a[target="_top"] ::attr(href)').extract()

        # use the following links variable if testing from the homepage
        # links = response.css('span.destArea a::attr(href)').extract()
        for url in links:
            yield scrapy.Request(self.domain + url, callback=self.parse_coordinates)

    def parse_coordinates(self, response):
        area_name = re.sub(AREA_PREFIXES, '', response.css('h1.dkorange em ::text').extract_first()).strip()
        lat_long_string = self.process_latitude_longitude(response)

        try:
            yield {
                'area_name': area_name,
                'id': response.url.split('com')[1],
                'parents': response.css('#navBox div a::attr(href)').extract(),
                'child_areas': response.css('#viewerLeftNavColContent a[target="_top"] ::attr(href)').extract(),
                'latitude': lat_long_string.split(',')[0],
                'longitude': lat_long_string.split(',')[1]
            }
        except IndexError:
            pass
        links = response.css('#viewerLeftNavColContent a[target="_top"] ::attr(href)').extract()
        for url in links:
            yield scrapy.Request(self.domain + url, callback=self.parse_coordinates)

    def process_latitude_longitude(self,response):
        if 'Location' not in response.css('#rspCol800 div.rspCol table tr:nth-child(2) td ::text').extract()[0]:
            return response.css('#rspCol800 div.rspCol table tr:nth-child(3) td ::text').extract()[1].strip()
        else:
            return response.css('#rspCol800 div.rspCol table tr:nth-child(2) td ::text').extract()[1].strip()
