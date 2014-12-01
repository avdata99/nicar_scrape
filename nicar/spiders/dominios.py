#!/usr/bin/python
# -*- coding: utf-8 -*-



import datetime

#from scrapy import log
from scrapy.selector import Selector
from scrapy.spider import Spider
from urlparse import urlparse






from nicar.items import NicarItem

class DominiosSpider(Spider):

    name = "dominios"
    allowed_domains = ['www.boletinoficial.gov.ar']
    date = str(datetime.date.today())
    today= datetime.date.today()



    def __init__(self, date_str=None, *args, **kwargs):
        super(DominiosSpider, self).__init__(*args, **kwargs)

        #paginación max se puede obtener de la página por xpath
        pages = 4
        if not date_str:
            today_str = self.today.strftime("%d/%m/%y")
        else:
            today_str = date_str

        self.start_urls = [
            'http://www.boletinoficial.gov.ar/CuartaSeccion/ListarPortadas.Castle?idRubro=744' \
                '&Fecha=%s&page=%s&cntRegistrosXPagCustom=10'
            % (today_str,str(page)) for page in xrange(1,pages+1)
        ]



    def parse(self, response):

        self.log('parse_form_output url: <%s>' % response.url)

        hxs = Selector(response)

        rows = hxs.xpath('//tr[position()>1]')


        for row in rows:
            zona = urlparse(''.join(row.xpath('td/a/@href').extract())).query
            if '.com.ar' in zona:
                doms = NicarItem()
                doms['zona'] = zona
                doms['dominio'] = ''.join(row.xpath('td/a/div/text()').extract()).strip()
                doms['registrante'] = ''.join(row.xpath('td[@class="textoResaltado"]/div/text()').extract())
                doms['operacion'] = ''.join(row.xpath('td[3]/div/text()').extract())
                yield doms












