from pytrends.request import TrendReq
import os as os

pytrends = TrendReq(hl='ko-KR', tz=360)

file_path = "keywords.log"
absol_path = os.path.join(os.getcwd(),"parsed",file_path)
file = open(absol_path,"r",encoding='utf-8')
kw_list = file.read().split('\n')

pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='KR', gprop='')
data = pytrends.interest_over_time()
data.to_csv(os.path.join(os.getcwd(),"parsed",'keywordstats.csv'))