# -*- coding: utf-8 -*-
# @Time    : 2018/3/23 23:39
# @Author  : Winspain
# @File    : wxpy.py
# @Software: PyCharm
# 导入模块
from wxpy import *
import requests,json
import time
def weatherApi():
    #调用和风天气的API city可以通过https://cdn.heweather.com/china-city-list.txt城市列表获取
    url = 'https://free-api.heweather.com/v5/weather?city=CN101210410&key=8a439a7e0e034cdcb4122c918f55e5f3'
    #用urllib2创建一个请求并得到返回结果
    req = requests.get(url)
    resp = req.text
    #将JSON转化为Python的数据结构
    json_data = json.loads(resp)
    city_data=json_data['HeWeather5'][0]
    hourly_data= json_data['HeWeather5'][0]['hourly_forecast']
    daily_data = json_data['HeWeather5'][0]['daily_forecast']

    t1 = u'当前时间：' + daily_data[0]['date']
    t2 = u'城市：' + city_data['basic']['city']
    t3 = u'PM指数：' + city_data['aqi']['city']['pm25']
    t4 = u'白天天气：' + daily_data[0]['cond']['txt_d']
    t5 = u'夜间天气：' + daily_data[0]['cond']['txt_n']
    t6 = u'今天{0}: 气温：{1}°/{2}°'.format(str(daily_data[0]['date']),daily_data[0]['tmp']['min'],daily_data[0]['tmp']['max'])
    t7 = u'未来小时天气：{0} {1}'.format(str(hourly_data[0]['date']).split()[1],hourly_data[0]['cond']['txt'])
    t8 = u'未来小时天气：{0} {1}'.format(str(hourly_data[1]['date']).split()[1],hourly_data[1]['cond']['txt'])
    t9 = u'未来小时天气：{0} {1}'.format(str(hourly_data[2]['date']).split()[1],hourly_data[2]['cond']['txt'])
    t10 = u'未来{0} 天气：{1}°/{2}°'.format(daily_data[1]['date'],daily_data[1]['tmp']['min'],daily_data[1]['tmp']['max'])
    t11 = u'未来{0} 天气：{1}°/{2}°'.format(daily_data[2]['date'],daily_data[1]['tmp']['min'],daily_data[2]['tmp']['max'])
    t12 = u'穿衣建议：' + json_data['HeWeather5'][0]['suggestion']['drsg']['txt']

    weather = t1+'\n'+t2+'\n'+t3+'\n'+t4+'\n'+t5+'\n'+t6+'\n'+t7+'\n'+t8+'\n'+t9+'\n'+t10+'\n'+t11+'\n'+t12
    #print(weather)
    return weather

def persistenceLogin():
    while True:
        bot = Bot(cache_path=True)
        return bot
if __name__ == '__main__':
    # 初始化机器人，扫码登陆
    bot = persistenceLogin()
    #bot = Bot(cache_path=True,console_qr=False)
    # xiaomilu = bot.friends().search('小麋鹿')[0]
    # for i in range(24):
    #     xiaomilu.send(weatherApi())
    #     time.sleep((i+1)*1800)
    for i in range(24):
        go = bot.groups().search('测试')[0]
        # go.send(weatherApi())
        t = time.ctime()
        go.send(t)
        time.sleep(1800)
    embed()