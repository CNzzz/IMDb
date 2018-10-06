# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from IMDb.items import MovieItem


class IMSpider(CrawlSpider):
    name = 'spider'
    allowed_domains = ['www.imdb.com']
    start_urls = ['http://www.imdb.com/chart/top']

    rules = (
        Rule(LinkExtractor(allow='title\/.*',restrict_xpaths="//tbody[@class='lister-list']//td[@class='titleColumn']"),callback='parse_item'),
    )
    def parse_item(self, response):
        item = MovieItem()
        item['Name'] = response.xpath("//div[@class='title_wrapper']/h1/text()").extract_first().strip()
        item['Director'] = response.xpath("//div[@class='credit_summary_item'][1]/a/text()").extract_first()
        item['Writers'] = response.xpath("//div[@class='credit_summary_item'][2]/a/text()").extract()
        item['Stars'] = response.xpath("//div[@class='credit_summary_item'][3]/a//text()").extract()
        item['Score'] = response.xpath("//div[@class='ratingValue']//span[@itemprop='ratingValue']/text()").extract_first()
        item['Time'] = response.xpath("//div[@class='titleBar']//div[@class='subtext']/a[last()]/text()").extract_first().strip('\n')
        item['Description'] = response.xpath("//div[@class='summary_text']/text()").extract_first().strip()
        item['URL'] = response.url
        yield item
