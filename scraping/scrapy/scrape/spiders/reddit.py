import scrapy


class QuotesSpider(scrapy.Spider):
    name = "reddit"

    def start_requests(self):
        urls = [
            'https://old.reddit.com/search?q=nlp&restrict_sr=&sort=relevance&t=all',
            'https://old.reddit.com/r/LanguageTechnology/comments/a1w7xk/efforts_to_crowdsource_linguistic_data/?st=jpbm595d&sh=e728b5b6',
        ]

        # Headers to mimic a browser visit
        headers = {'User-Agent': 'Mozilla/5.0'}

        for url in urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        print(response.body)
        page = response.url.split("/")[-2]
        filename = 'red-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)