import scrapy


class QuotesSpider(scrapy.Spider):
    name = "twit"

    def start_requests(self):
        urls = [
            'https://twitter.com/search?vertical=news&q=data&src=typd&lang=en&lang=en',
            'https://twitter.com/search?vertical=news&q=nlp&src=typd&lang=en&lang=en',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'twit-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)