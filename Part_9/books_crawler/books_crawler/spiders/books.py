# -*- coding: utf-8 -*-
from scrapy import Spider

from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class BooksSpider(Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']

    def start_requests(self):
        # define the webdriver
        # Chrome webdiver generally works better than mozilla
        self.driver = webdriver.Chrome('/Users/Joshl/Desktop/chromedriver')
        # get the book.toscrape.com webpage
        self.driver.get('http://books.toscrape.com/')
        
        sel = Selector(text=self.driver.page_source)
        books = sel.xpath('//h3/a/@href').extract()
        
        for book in books:
            url = 'http://books.toscrape.com/' + book
            yield Request(url, callback=self.parse_book)
         
        while True:
            try:
                # get next page button
                next_page = self.driver.find_element_by_xpath('//a[text()="next"]')
                # want to sleep to avoid clicking next page when current page
                # is still loading
                sleep(3)
                self.logger.info('Sleeping for 3 seconds.')
                # click on next page button
                next_page.click()
                
                sel = Selector(text=self.driver.page_source)
                books = sel.xpath('//h3/a/@href').extract()
                
                for book in books:
                    url = 'http://books.toscrape.com/catalogue/' + book
                    yield Request(url, callback=self.parse_book)
            except NoSuchElementException:
                # when we hit last page
                self.logger.info('No more pages to load.')
                self.driver.quit()
                break
       
    def parse_book(self, response):
        pass