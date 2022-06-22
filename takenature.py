import scrapy

# search involving bioinformatics in germany
class takenature(scrapy.Spider):
    
    name="naturetaker"
    start_urls=['https://www.nature.com/naturecareers/jobs/search?text=Bioinformatics&location=Germany']
    
    
    def parse(self,response):
        for article in response.css('article'):
            try:
                yield{
                    'Title' :article.css('h3.p-card__info-title ::text').get(),
                    'Subtitle' :article.css('p.p-card__info-subtitle ::text').get(),
                    'Location':article.css('p.p-card__info-location ::text').get(),
                    'Time' : article.css('p.p-card__info-time::text').get()
                }
            except:
                yield{
                    'Title' :article.css('h3.p-card__info-title ::text').get(),
                    'Subtitle' :article.css('p.p-card__info-subtitle ::text').get(),
                    'Location':article.css('p.p-card__info-location ::text').get(),
                    'Time': 'Time not mentioned'
                }
            
            # parse to next page
            next_page=response.css('a.c-pagination__item.c-pagination__item--arrow-right').attrib['href']
            if next_page is not None:
                yield response.follow(next_page,callback=self.parse)
    