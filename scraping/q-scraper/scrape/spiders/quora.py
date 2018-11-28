import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quora"

    def start_requests(self):
        urls = [
            'https://www.quora.com/topic/Marketing-Strategy/',
            'https://www.quora.com/topic/Marketing-Strategy/top_questions/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quora-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)