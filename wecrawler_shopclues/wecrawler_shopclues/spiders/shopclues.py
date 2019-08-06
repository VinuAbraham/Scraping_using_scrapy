# -*- coding: utf-8 -*-
import scrapy


class ShopcluesSpider(scrapy.Spider):
    name = 'shopclues'
    allowed_domains = ['www.shopclues.com/mobiles-smartphones.html?facet_network_type[]=4G']
    start_urls = ['http://www.shopclues.com/mobiles-smartphones.html?facet_network_type[]=4G/']

    def parse(self, response):
        pass
