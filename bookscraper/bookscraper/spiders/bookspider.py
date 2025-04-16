import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.xpath('//article[@class="product_pod"]')
        for book in books:
            book_url = book.xpath('.//h3/a/@href').get()
            if book_url:
                yield response.follow(url=book_url, callback=self.book_parser)

        next_semi_url = response.xpath('//li[@class="next"]/a/@href').get()
        if next_semi_url:
            next_page = response.urljoin(next_semi_url)
            yield response.follow(url=next_page, callback=self.parse)

    def book_parser(self, response):
        availability_text = response.css('.table tr')[5].css('td::text').get()
        num_available = 0
        if availability_text:
            import re
            match = re.search(r'(\d+)', availability_text)
            if match:
                num_available = int(match.group(1))
            availability = availability_text.strip()
        else:
            availability = ''

        star_rating_class = response.css('p.star-rating::attr(class)').get()
        star_rating = ''
        if star_rating_class:
            parts = star_rating_class.split()
            if len(parts) > 1:
                star_rating = parts[1]
            else:
                star_rating = "Zero"

        yield {
            'title': response.css('div.product_main > h1::text').get(),
            'product_description': response.xpath('//div[@id = "product_description"]/following-sibling::p//text()').get(),
            'price': response.css('p.price_color::text').get(),
            'star_rating': star_rating,
            'type': response.xpath('//li[@class="active"]/preceding-sibling::li[2]/a/text()').get(),
            'category': response.xpath('//li[@class="active"]/preceding-sibling::li[1]/a/text()').get(),
            'price_excl_tax': response.css('.table tr')[2].css('td::text').get(),
            'price_inc_tax': response.css('.table tr')[3].css('td::text').get(),
            'tax': response.css('.table tr')[4].css('td::text').get(),
            'availability': availability,
            'num_available': num_available,
            'num_reviews': response.css('.table tr')[6].css('td::text').get()
        }
