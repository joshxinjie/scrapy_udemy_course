# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import FormRequest

# this is just a practice site so any username and password will work

class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        csrf_token =\
        response.xpath('//*[@name="csrf_token"]/@value').extract_first()
        
        yield FormRequest('http://quotes.toscrape.com/login',
                          formdata={'csrf_token':csrf_token,
                                    'username': 'foobar',
                                    'password': 'foobar'
                                    },
                                    callback=self.parse_after_login
                                    )
    
    def parse_after_login(self, response):
        # to check if we have successfully login
        # if we did login, we will see a logout text
        if response.xpath('//a[text()="Logout"]'):
            self.log("You logged in!")
        
        # alternatively, open the logged in page in browser
        #open_in_browser(response)
