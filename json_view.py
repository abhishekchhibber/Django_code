from dashboard.models import Organization, News, Investor, Segment, Trend, NewsFilter, Country
import datetime
import calender
data = [ ]
alldata = News.objects.all()
for data1 in alldata:
	dict = { }
	title = data1.news_title
	dict['Title'] = title
	link = data1.news_link
	dict['Link'] = link

	tr = data1.news_trend.all()
	tr_list = [ ]
	tr_len = len(tr)
	for i in range(0,tr_len):
		w = tr[i].trend
		tr_list.append(w)
	dict['Trend'] = tr_list

	ct = data1.news_country.all()
	ct_list = [ ]
	ct_len = len(ct)
	for i in range(0,ct_len):
		ct1 = ct[i].country
		ct_list.append(ct1)
	dict['Country'] = ct_list

	sg = data1.news_segment.all()
	sg_list = [ ]
	sg_len = len(sg)
	for i in range(0,sg_len):
		sg1 = sg[i].segment
		sg_list.append(sg1)
	dict['Segment'] = sg_list

	fulldate = data1.news_date
	dict['Year'] = fulldate.year
	monthy = calendar.month_abbr[fulldate.month]
	dict['Month'] = monthy
	mm = fulldate.month
	q = ((mm-1)//3)+1
	quat = "Quarter ",q
	dict['Quarter'] = quat
	dict['Month_year'] = monthy," ",fulldate.year
	
  data.append(dict)
