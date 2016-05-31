from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pymysql


config_currency = {
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'password':'19860112',
    'db':'currency',
    'charset':'utf8',
}

from datetime import datetime
present_date = datetime.now().date()

def delete_today_currency_data(config_currency):
    connection = pymysql.connect(**config_currency)
    try:
        with connection.cursor() as cursor:
            # 执行sql语句，插入记录
            sql = "DELETE FROM currency where date = %s"
            cursor.execute(sql,(present_date))
            # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    finally:
        connection.close()
    print('Executed on-----------',present_date,'\n','-----------------------delete success!----------------','\n')

def get_boc_currency_data(config_currency,source):
    url = 'http://www.boc.cn/sourcedb/whpj/'
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'lxml')
    # print(soup)
    names = soup.select('div.publish > div:nth-of-type(2) > table > tr > td:nth-of-type(1)')
    buy_xianchaoes = soup.select('div.publish > div:nth-of-type(2) > table > tr > td:nth-of-type(3)')
    buy_xianhuies = soup.select('div.publish > div:nth-of-type(2) > table > tr > td:nth-of-type(2)')
    sell_xianhuies = soup.select('div.publish > div:nth-of-type(2) > table > tr > td:nth-of-type(4)')
    sell_xianchaoes = soup.select('div.publish > div:nth-of-type(2) > table > tr > td:nth-of-type(5)')
    times = soup.select('div.publish > div:nth-of-type(2) > table > tr > td:nth-of-type(8)')
    for name,buy_xianchao,buy_xianhui,sell_xianchao,sell_xianhui,time in zip(names,buy_xianchaoes,buy_xianhuies,sell_xianchaoes,sell_xianhuies,times):
        name = name.get_text().encode('latin-1').decode('utf-8')
        buy_xianhui = buy_xianhui.get_text()
        print('buy_xianhui--------',buy_xianhui,type(buy_xianhui))
        buy_xianchao = buy_xianchao.get_text()
        sell_xianhui = sell_xianhui.get_text()
        sell_xianchao = sell_xianchao.get_text()
        time = time.get_text()
        if buy_xianchao == '':
            buy_xianchao = '0.0'
        if buy_xianhui == '':
            buy_xianhui = '0.0'
        if sell_xianchao == '':
            sell_xianchao = '0.0'
        if sell_xianhui == '':
            sell_xianhui = '0.0'
        print('name',name,'--buy_xianhui',buy_xianhui,'---buy_xianchao',buy_xianchao,'---sell_xianchao',sell_xianchao,'---sell_xianhui',sell_xianhui,'---time',time)
        connection = pymysql.connect(**config_currency)
        try:
            with connection.cursor() as cursor:
                # 执行sql语句，插入记录
                sql = 'INSERT INTO currency (name,buy_xianhui,buy_xianchao,sell_xianhui,sell_xianchao,date,time,source) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
                cursor.execute(sql, (name,buy_xianhui,buy_xianchao,sell_xianhui,sell_xianchao,present_date,time,source))
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
            connection.commit()
        finally:
            connection.close()

def get_cmb_currency_data(config_currency,source):
    url = 'http://fx.cmbchina.com/hq/'
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'lxml')
    # print(soup)
    names = soup.select('div.box.hq > div > table > tr > td:nth-of-type(1)')
    buy_xianchaoes = soup.select('div.box.hq > div > table > tr > td:nth-of-type(8)')
    buy_xianhuies = soup.select('div.box.hq > div > table > tr > td:nth-of-type(7)')
    sell_xianhuies = soup.select('div.box.hq > div > table > tr > td:nth-of-type(5)')
    sell_xianchaoes = soup.select('div.box.hq > div > table > tr > td:nth-of-type(6)')
    times = soup.select('div.box.hq > div > table > tr > td:nth-of-type(9)')
    for name,buy_xianchao,buy_xianhui,sell_xianchao,sell_xianhui,time in zip(names,buy_xianchaoes,buy_xianhuies,sell_xianchaoes,sell_xianhuies,times):
        name = name.get_text()
        name = name.strip()
        buy_xianhui = buy_xianhui.get_text()
        buy_xianchao = buy_xianchao.get_text()
        sell_xianhui = sell_xianhui.get_text()
        sell_xianchao = sell_xianchao.get_text()
        time = time.get_text().strip()
        if name == '交易币':
            continue
        print('---name',name,'--buy_xianhui',buy_xianhui,'---buy_xianchao',buy_xianchao,'---sell_xianchao',sell_xianchao,'---sell_xianhui',sell_xianhui,'---time',time)
        connection = pymysql.connect(**config_currency)
        try:
            with connection.cursor() as cursor:
                # 执行sql语句，插入记录
                sql = 'INSERT INTO currency (name,buy_xianhui,buy_xianchao,sell_xianhui,sell_xianchao,date,time,source) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
                cursor.execute(sql, (name,buy_xianhui,buy_xianchao,sell_xianhui,sell_xianchao,present_date,time,source))
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
            connection.commit()
        finally:
            connection.close()


source = ['boc','cmb']
delete_today_currency_data(config_currency)
get_boc_currency_data(config_currency,source[0])
get_cmb_currency_data(config_currency,source[1])