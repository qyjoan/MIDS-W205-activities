from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from iSchool.items import iSchoolItem

class MySpider(Spider):
   name = "ischool"
   allowed_domains = ["berkeley.edu"]
   start_urls = ["http://www.ischool.berkeley.edu/people/faculty"]

   def parse(self, response):
      hxs = HtmlXPathSelector(response)
      titles = hxs.select("//div[@class='title']")
      items = []
      for title in titles:
         item = iSchoolItem()
         item["name"] = titles.select("a/text()").extract()
         item["link"] = titles.select("a/@href").extract()
         items.append(item)
      return items
