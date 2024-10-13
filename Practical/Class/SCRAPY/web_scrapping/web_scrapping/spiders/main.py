import scrapy

class StackOverflowSpider(scrapy.Spider):
      name = 'my_spider'
      start_urls = ['https://stackoverflow.com/questions']

      def parse(self, response):
          # Extract data from the current page
          questions = response.css('h3.s-post-summary--content-title a::text').getall()
          for question in questions:
              yield {'question': question}

          # Follow pagination links
          for page_num in range(2, 50):  # Example range for pages 2 to 10
              next_page = f'https://stackoverflow.com/questions/tagged/python?tab=newest&page={page_num}&pagesize=15'
              yield scrapy.Request(url=next_page, callback=self.parse)

