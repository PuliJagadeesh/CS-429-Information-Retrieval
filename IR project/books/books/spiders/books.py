from pathlib import Path

import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def __init__(self, max_pages=5, max_depth=5, *args, **kwargs):
        super(BooksSpider, self).__init__(*args, **kwargs)
        self.max_pages = int(max_pages) if max_pages is not None else None
        self.max_depth = int(max_depth) if max_depth is not None else None
        self.pages_visited = 0

    def start_requests(self):
        urls = [
            "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
            "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
            "https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if self.max_pages is not None and self.pages_visited >= self.max_pages:
            self.log(f"Reached maximum number of pages: {self.max_pages}")
            return

        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")

        self.pages_visited += 1

        if self.max_depth is not None and self.pages_visited < self.max_depth:
            # Extract links from the current page and follow them
            for next_page_url in response.css('li.next a::attr(href)').getall():
                yield response.follow(next_page_url, callback=self.parse)

    def closed(self, reason):
        self.log(f"Spider closed: {reason}")
