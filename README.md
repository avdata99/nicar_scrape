nicar_scrape
============

Scrape of Domains in Argentina (zone=.com.ar) from www.boletinoficial.gov.ar

* Using Scrapy 0.24.4

Install scrapy

scrapy crawl dominios -t json -o dominios.json

#for another date
scrapy crawl dominios -t json -o dominios-20131231.json -a date_str=12/31/2013

#bulk scrape
python doit.py #for setting day's amount and output format check the file
