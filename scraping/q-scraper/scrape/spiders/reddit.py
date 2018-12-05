import scrapy


class QuotesSpider(scrapy.Spider):
    name = "reddit"

    def start_requests(self):
        urls = [
            'https://www.reddit.com/r/LanguageTechnology/',
            'https://www.reddit.com/r/LanguageTechnology/comments/a2obq0/out_of_vocabulary_word_embedding_in_a_pretrained/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'red-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)