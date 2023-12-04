from pytrends.request import TrendReq

pytrends = TrendReq(hl='ko-KR', tz=360)

file_path = "keywords.txt"
file = open(file_path,"r",encoding='utf-8')
kw_list = file.read().split('\n')

kw_list = ['T익스프레스','사파리월드','로스트밸리']

pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='KR', gprop='')
data = pytrends.interest_over_time()
data.to_csv('keywordstats.csv')