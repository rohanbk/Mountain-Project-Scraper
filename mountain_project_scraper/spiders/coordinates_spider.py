import scrapy
import json

class CoordinatesSpider(scrapy.Spider):
    name = 'coordinates'

    def start_requests(self):
        urls = [
            'https://www.mountainproject.com/v/kansas/107235316'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        sidebar_links = response.css('#viewerLeftNavColContent a[target="_top"]').extract()
        lat_long_dirty = response.css('#rspCol800 div.rspCol table tr').extract()[1] #find out how to process this and extract lat/long


