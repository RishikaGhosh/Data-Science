import scrapy

class BooksSpider(scrapy.Spider):
    name="books"

    def start_requests(self):
        urls=['http://books.toscrape.com/catalogue/page-1.html',
        ]

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)



        # "div.image_container a img::attr(src)"
        #  all_stuff.css("h3 a::attr(title)").getall()
        #  all_stuff.css("div.product_price p.price_color::text").getall()
        # response.css("ul.pager li.next a::attr(href)").getall()
    def parse(self,response):
        for all_stuff in response.css('article.product_pod'):
            yield{
                'image_url':all_stuff.css("div.image_container a img::attr(src)").get(),
                'book_title':all_stuff.css("h3 a::attr(title)").get(),
                'product_price':all_stuff.css("div.product_price p.price_color::text").get(),

            }
        next_page=response.css("ul.pager li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
            
