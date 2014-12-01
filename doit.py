# -*- coding: utf-8 -*-
import os
from datetime import timedelta, datetime

start_date = datetime.today()
day_count = 300
for single_date in (start_date - timedelta(n) for n in range(day_count)):
    date2 = single_date.strftime("%d/%m/%y")
    date1 = single_date.strftime("%y%m%d")
    dest = 'tests/dominios-%s.csv' % date1
    if os.path.exists(dest):
        print "Already exists"
    else:
        print "Scrapyng %s" %date2
        cmd = 'scrapy crawl dominios -t csv -o %s -a date_str=%s' % (dest, date2)
        os.system(cmd)



