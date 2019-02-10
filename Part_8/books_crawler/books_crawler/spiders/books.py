# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class BooksSpider(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']
    
    # LinkExtractor object will grab all the urls when we are in a specific
    # page
    # follow is a boolean expression. If true, will process all pages.
    # If false, will process only homepage
    rules = (Rule(LinkExtractor(), callback='parse_page', follow=False),)
    
    # to ignore all google related pages and domains
    # good idea to avoid domains and pages such as google, social media
    # (facebook, Instagram, Google+, Twitter, LinkedIn, etc)
    # might get you banned or thrown captcha
    #rules = (Rule(LinkExtractor(deny_domains='google.com'),\
    #              callback='parse_page', follow=False),)
    
    # only process pages with music in the url
    #rules = (Rule(LinkExtractor(allow='music'),\
    #              callback='parse_page', follow=True),)

    def parse_page(self, response):
        #yield = {'URL': response.url}
        pass
