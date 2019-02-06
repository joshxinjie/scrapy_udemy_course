# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    # will only scrape from these domains
    # original does not work. Must remove http:// at the beginning
    # and / at the end
    #allowed_domains = ['http://quotes.toscrape.com/']
    allowed_domains = ["quotes.toscrape.com"]
    # original does not work. Must remove http:// at the beginning
    # and / at the end
    #start_urls = ['http://http://quotes.toscrape.com//']
    # can be tuple or list
    start_urls = (
        'http://quotes.toscrape.com/',
    )

    def parse(self, response):
        # to parse the title 'Quotes to Scrape'
        h1_tag = response.xpath('//h1/a/text()').extract_first()
        # to scrape the 10 tags of the left
        tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()
        
        yield {'H1 Tag': h1_tag, 'Tags': tags}
