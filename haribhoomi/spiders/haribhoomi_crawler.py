# -*- coding: utf-8 -*-
import scrapy
import os
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
dest='/home/lol/Desktop/haribhoomi/data'
class HaribhoomiCrawlerSpider(CrawlSpider):
	name = 'haribhoomi_crawler'
	allowed_domains = ['www.haribhoomi.com']
	start_urls = ['http://www.haribhoomi.com/']
	#Note:callback function name should always be something different from parse
	rules=(Rule(LxmlLinkExtractor(allow=(),deny=()),callback="parse_page",follow=True),)
	def parse_page(self, response):
		
		c=''.join(response.css('h1::text').extract())#heading
		print(c)		
		content = (''.join(response.xpath('//div[@class="mBottom30"]/h3/text()').extract())).encode("UTF-8")
		content1 = (''.join(response.xpath('//div[@class="mBottom30"]/div/text()').extract())).encode("UTF-8")
		content2 = (''.join(response.xpath('//div[@class="mBottom30"]/p/text()').extract())).encode("UTF-8")
		if (((len(c)!=0)) and (len(content)>20)):
			urlstr=response.url
			print(urlstr)
			print("\n\n")
			urlstrclean = ''.join(e for e in urlstr if e.isalnum())
			try:
				fil=open(os.path.join(dest,urlstrclean+'.txt'),'w')
				print("OPENED!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			except IOerror:
				print("couldnt open!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			fil.write(c[0].encode("UTF-8"))
			fil.write(content)
			fil.write(content1)
			fil.write(content2)
			fil.close()
			yield {'h1':urlstrclean}
