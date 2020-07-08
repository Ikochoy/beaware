from bs4 import BeautifulSoup
import requests

url_dow_jones = "https://ca.finance.yahoo.com/quote/%5Edji/"
url_chart = "https://ca.finance.yahoo.com/quote/%5EDJI/chart?p=%5EDJI#eyJpbnRlcn" \
            "ZhbCI6ImRheSIsInBlcmlvZGljaXR5IjoxLCJ0aW1lVW5pdCI6bnVsbCwiY2FuZGxl" \
            "V2lkdGgiOjgsInZvbHVtZVVuZGVybGF5Ijp0cnVlLCJhZGoiOnRydWUsImNyb3NzaGF" \
            "pciI6dHJ1ZSwiY2hhcnRUeXBlIjoibGluZSIsImV4dGVuZGVkIjpmYWxzZSwibWFya2V" \
            "0U2Vzc2lvbnMiOnt9LCJhZ2dyZWdhdGlvblR5cGUiOiJvaGxjIiwiY2hhcnRTY2FsZSI6" \
            "ImxpbmVhciIsInBhbmVscyI6eyJjaGFydCI6eyJwZXJjZW50IjoxLCJkaXNwbGF5IjoiX" \
            "kRKSSIsImNoYXJ0TmFtZSI6ImNoYXJ0IiwidG9wIjowfX0sInNldFNwYW4iOnt9LCJsaW5l" \
            "V2lkdGgiOjIsInN0cmlwZWRCYWNrZ3JvdWQiOnRydWUsImV2ZW50cyI6dHJ1ZSwiY29sb3Ii" \
            "OiIjMDA4MWYyIiwiZXZlbnRNYXAiOnsiY29ycG9yYXRlIjp7ImRpdnMiOnRydWUsInNwbGl0cy" \
            "I6dHJ1ZX0sInNpZ0RldiI6e319LCJzeW1ib2xzIjpbeyJzeW1ib2wiOiJeREpJIiwic3ltYm" \
            "9sT2JqZWN0Ijp7InN5bWJvbCI6Il5ESkkifSwicGVyaW9kaWNpdHkiOjEsImludGVydmFsI" \
            "joiZGF5IiwidGltZVVuaXQiOm51bGwsInNldFNwYW4iOnt9fV0sInN0dWRpZXMiOnsidm9s" \
            "IHVuZHIiOnsidHlwZSI6InZvbCB1bmRyIiwiaW5wdXRzIjp7ImlkIjoidm9sIHVuZHIiLCJka" \
            "XNwbGF5Ijoidm9sIHVuZHIifSwib3V0cHV0cyI6eyJVcCBWb2x1bWUiOiIjMDBiMDYxIiwiRG9" \
            "3biBWb2x1bWUiOiIjRkYzMzNBIn0sInBhbmVsIjoiY2hhcnQiLCJwYXJhbWV0ZXJzIjp7IndpZHR" \
            "oRmFjdG9yIjowLjQ1LCJjaGFydE5hbWUiOiJjaGFydCJ9fX19"
r = requests.get(url_dow_jones)
soup = BeautifulSoup(r.content, 'html5lib')
dow_jones_data = {}
real_time_figure = soup.find("span", {'class': 'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)'})
figure_change_red = soup.find("span", {'class': 'Trsdu(0.3s) Fw(500) Fz(14px) C($negativeColor)', 'data-reactid':'16'});
figure_change_green = soup.find("span", {'class': 'Trsdu(0.3s) Fw(500) Fz(14px) C($positiveColor)', 'data-reactid':'16'});
previous_close = soup.find("td", {'class': 'Ta(end) Fw(600) Lh(14px)',  'data-reactid': '14', 'data-test': 'PREV_CLOSE-value'})
open_p = soup.find("td", {'class': 'Ta(end) Fw(600) Lh(14px)', 'data-reactid':'19', 'data-test': 'OPEN-value'})
volume = soup.find("td", {'class':'Ta(end) Fw(600) Lh(14px)', 'data-reactid': '24', 'data-test': 'TD_VOLUME-value'})
avg_volume = soup.find("td", {'class': 'Ta(end) Fw(600) Lh(14px)', 'data-reactid':'40', 'data-test': 'AVERAGE_VOLUME_3MONTH-value'})
dow_jones_data['RTF'] = real_time_figure.text
if figure_change_red == None and figure_change_green == None:
    dow_jones_data['FC'] = "0.00"
elif figure_change_red == None:
    dow_jones_data['FC'] = figure_change_green.text
else:
    dow_jones_data['FC'] = figure_change_red.text
dow_jones_data['PC'] = previous_close.text
dow_jones_data['OP'] = open_p.text
dow_jones_data['VL'] = volume.text
dow_jones_data['AVGVL'] = avg_volume.text
dow_jones_data['IMG'] = url_chart


url_hsi = "https://ca.finance.yahoo.com/quote/%5Ehsi?ltr=1"
r_hk = requests.get(url_hsi)
url_chart_hk = "https://finance.yahoo.com/quote/%5EHSI/"
soup_hk = BeautifulSoup(r_hk.content, 'html5lib')
heng_seng_data = {}
rtf = soup_hk.find("span", {'class': 'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)', 'data-reactid':'14'})
fc_red = soup_hk.find("span", {'class': 'Trsdu(0.3s) Fw(500) Fz(14px) C($negativeColor)', 'data-reactid':'16'})
fc_green = soup_hk.find("span",{'class': 'Trsdu(0.3s) Fw(500) Fz(14px) C($positiveColor)', 'data-reactid':'16'})
pc = soup_hk.find("td", {'class': 'Ta(end) Fw(600) Lh(14px)',  'data-reactid': '14', 'data-test': 'PREV_CLOSE-value'})
op = soup_hk.find("td", {'class': 'Ta(end) Fw(600) Lh(14px)', 'data-reactid':'19', 'data-test': 'OPEN-value'})
vl = soup_hk.find("td", {'class':'Ta(end) Fw(600) Lh(14px)', 'data-reactid': '24', 'data-test': 'TD_VOLUME-value'})
avgvl = soup_hk.find("td", {'class': 'Ta(end) Fw(600) Lh(14px)', 'data-reactid':'40', 'data-test': 'AVERAGE_VOLUME_3MONTH-value'})
heng_seng_data["RTF"] = rtf.text
if fc_red == None and fc_green == None:
    heng_seng_data["FC"] = "0.00"
elif fc_red == None:
    heng_seng_data["FC"] = fc_green.text
else:
    heng_seng_data["FC"] = fc_red.text
heng_seng_data["PC"] = pc.text
heng_seng_data["OP"] = op.text
heng_seng_data["VL"] = vl.text
heng_seng_data["AVGVL"] = avgvl.text
heng_seng_data["IMG"] = url_chart_hk


url_london = "https://finance.yahoo.com/quote/%5EFTSE/"
r_london = requests.get(url_london)
soup_london = BeautifulSoup(r_london.content, 'html5lib')
london_data ={}
rtf = soup_london.find("span", {'class': 'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)', 'data-reactid':'14'})
fc_red = soup_london.find("span", {'class': 'Trsdu(0.3s) Fw(500) Fz(14px) C($negativeColor)', 'data-reactid':'16'})
fc_green = soup_london.find("span",{'class': 'Trsdu(0.3s) Fw(500) Fz(14px) C($positiveColor)', 'data-reactid':'16'})
pc = soup_london.find("td", {'class': 'Ta(end) Fw(600) Lh(14px)',  'data-reactid': '15', 'data-test': 'PREV_CLOSE-value'})
op = soup_london.find("td", {'class': 'Ta(end) Fw(600) Lh(14px)', 'data-reactid':'20', 'data-test': 'OPEN-value'})
vl = soup_london.find("td", {'class':'Ta(end) Fw(600) Lh(14px)', 'data-reactid': '25', 'data-test': 'TD_VOLUME-value'})
avgvl = soup_london.find("td", {'class': 'Ta(end) Fw(600) Lh(14px)', 'data-reactid':'41', 'data-test': 'AVERAGE_VOLUME_3MONTH-value'})
london_data['RTF'] = rtf.text
if fc_red == None and fc_green == None:
    london_data["FC"] = "0.00"
elif fc_red == None:
    london_data["FC"] = fc_green.text
else:
    london_data["FC"] = fc_red.text
london_data["PC"] = pc.text
london_data["OP"] = op.text
london_data["VL"] = vl.text
london_data["AVGVL"] = avgvl.text


url_commodities = "https://finance.yahoo.com/commodities/"
r_com = requests.get(url_commodities)
soup_com = BeautifulSoup(r_com.content, 'html5lib')


url_crudeOil = "https://finance.yahoo.com/quote/CL=F%3Fp=CL%3DF"
r_crudeOil = requests.get(url_crudeOil)
soup_energy = BeautifulSoup(r_crudeOil.content, 'html5lib')
crudeoil_data ={}
rtf_crudeOil = soup_energy.find("span", {'class': 'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)', 'data-reactid': '14'})
fc_red = soup_energy.find("span", {'class': 'Trsdu(0.3s) Fw(500) Fz(14px) C($negativeColor)', 'data-reactid':'16'})
fc_green = soup_energy.find("span",{'class': 'Trsdu(0.3s) Fw(500) Fz(14px) C($positiveColor)', 'data-reactid':'16'})
crudeoil_data['RTF'] = rtf_crudeOil.text
if fc_red == None and fc_green == None:
    crudeoil_data["FC"] = "0.00"
elif fc_red == None:
    crudeoil_data["FC"] = fc_green.text
else:
    crudeoil_data["FC"] = fc_red.text


# Brent Crude Oil
brent_data = {}
rtf_brent = soup_com.find("td", {'class': 'data-col2 Ta(end) Pstart(20px)', 'data-reactid': '335'})
fc_red = soup_com.find("span", {'class':'Trsdu(0.3s) C($negativeColor)', 'data-reactid': '338'})
fc_green = soup_com.find("span", {'class':'Trsdu(0.3s) C($positiveColor)', 'data-reactid': '338'})
brent_data['RTF'] = rtf_brent.text
if fc_red == None and fc_green == None:
    brent_data["FC"] = "0.00"
elif fc_red == None:
    brent_data["FC"] = fc_green.text
else:
    brent_data["FC"] = fc_red.text

# natural gas
ng_data = {}
rtf_ng = soup_com.find("td", {'class': 'data-col2 Ta(end) Pstart(20px)', 'data-reactid': '305'})
fc_red = soup_com.find("span", {'class':'Trsdu(0.3s) C($negativeColor)', 'data-reactid': '308'})
fc_green = soup_com.find("span", {'class':'Trsdu(0.3s) C($positiveColor)', 'data-reactid': '308'})
ng_data['RTF'] = rtf_ng.text
if fc_red == None and fc_green == None:
    ng_data["FC"] = "0.00"
elif fc_red == None:
    ng_data["FC"] = fc_green.text
else:
    ng_data["FC"] = fc_red.text


# corn
url_corn = url_commodities
r_corn = requests.get(url_corn)
soup_corn = BeautifulSoup(r_corn.content, 'html5lib')
corn_data = {}
rtf_corn = soup_corn.find("td", {'class': 'data-col2 Ta(end) Pstart(20px)', 'data-reactid':'365'})
fc_red = soup_corn.find("span", {'class':'Trsdu(0.3s) C($negativeColor)', 'data-reactid': '368'})
fc_green = soup_corn.find("span", {'class':'Trsdu(0.3s) C($positiveColor)', 'data-reactid': '368'})
corn_data['RTF'] = rtf_crudeOil.text
if fc_red == None and fc_green == None:
    corn_data["FC"] = "0.00"
elif fc_red == None:
    corn_data["FC"] = fc_green.text
else:
    corn_data["FC"] = fc_red.text

# wheat
wt_data = {}
rtf_wt = soup_com.find("td", {'class': 'data-col2 Ta(end) Pstart(20px)', 'data-reactid': '395'})
fc_red = soup_com.find("span", {'class':'Trsdu(0.3s) C($negativeColor)', 'data-reactid': '398'})
fc_green = soup_com.find("span", {'class':'Trsdu(0.3s) C($positiveColor)', 'data-reactid': '398'})
wt_data['RTF'] = rtf_wt.text
if fc_red == None and fc_green == None:
    wt_data["FC"] = "0.00"
elif fc_red == None:
    wt_data["FC"] = fc_green.text
else:
    wt_data["FC"] = fc_red.text

# rice
rice_data = {}
rtf_rice = soup_com.find("td", {'class': 'data-col2 Ta(end) Pstart(20px)', 'data-reactid': '410'})
fc_red = soup_com.find("span", {'class':'Trsdu(0.3s) C($negativeColor)', 'data-reactid': '413'})
fc_green = soup_com.find("span", {'class':'Trsdu(0.3s) C($positiveColor)', 'data-reactid': '413'})
rice_data['RTF'] = rtf_rice.text
if fc_red == None and fc_green == None:
    rice_data["FC"] = "0.00"
elif fc_red == None:
    rice_data["FC"] = fc_green.text
else:
    rice_data["FC"] = fc_red.text

# oats
oats_data = {}
rtf_oats = soup_com.find("td", {'class': 'data-col2 Ta(end) Pstart(20px)', 'data-reactid': '380'})
fc_red = soup_com.find("span", {'class':'Trsdu(0.3s) C($negativeColor)', 'data-reactid': '383'})
fc_green = soup_com.find("span", {'class':'Trsdu(0.3s) C($positiveColor)', 'data-reactid': '383'})
oats_data['RTF'] = rtf_oats.text
if fc_red == None and fc_green == None:
    oats_data["FC"] = "0.00"
elif fc_red == None:
    oats_data["FC"] = fc_green.text
else:
    oats_data["FC"] = fc_red.text


# gold
gold_data = {}
rtf_gold = soup_com.find("td", {'class': 'data-col2 Ta(end) Pstart(20px)', 'data-reactid': '170'})
fc_red = soup_com.find("span", {'class':'Trsdu(0.3s) C($negativeColor)', 'data-reactid': '173'})
fc_green = soup_com.find("span", {'class':'Trsdu(0.3s) C($positiveColor)', 'data-reactid': '173'})
gold_data['RTF'] = rtf_gold.text
if fc_red == None and fc_green == None:
    gold_data["FC"] = "0.00"
elif fc_red == None:
    gold_data["FC"] = fc_green.text
else:
    gold_data["FC"] = fc_red.text

# siver
sil_data = {}
rtf_silver = soup_com.find("td", {'class': 'data-col2 Ta(end) Pstart(20px)', 'data-reactid': '200'})
fc_red = soup_com.find("span", {'class':'Trsdu(0.3s) C($negativeColor)', 'data-reactid': '203'})
fc_green = soup_com.find("span", {'class':'Trsdu(0.3s) C($positiveColor)', 'data-reactid': '203'})
sil_data['RTF'] = rtf_silver.text
if fc_red == None and fc_green == None:
    sil_data["FC"] = "0.00"
elif fc_red == None:
    sil_data["FC"] = fc_green.text
else:
    sil_data["FC"] = fc_red.text

# copper
cu_data = {}
rtf_copper = soup_com.find("td", {'class': 'data-col2 Ta(end) Pstart(20px)', 'data-reactid': '245'})
fc_red = soup_com.find("span", {'class':'Trsdu(0.3s) C($negativeColor)', 'data-reactid': '248'})
fc_green = soup_com.find("span", {'class':'Trsdu(0.3s) C($positiveColor)', 'data-reactid': '248'})
cu_data['RTF'] = rtf_copper.text
if fc_red == None and fc_green == None:
    cu_data["FC"] = "0.00"
elif fc_red == None:
    cu_data["FC"] = fc_green.text
else:
    cu_data["FC"] = fc_red.text

# platinum
pt_data = {}
rtf_platinum = soup_com.find("td", {'class': 'data-col2 Ta(end) Pstart(20px)', 'data-reactid': '230'})
fc_red = soup_com.find("span", {'class':'Trsdu(0.3s) C($negativeColor)', 'data-reactid': '233'})
fc_green = soup_com.find("span", {'class':'Trsdu(0.3s) C($positiveColor)', 'data-reactid': '233'})
pt_data['RTF'] = rtf_platinum.text
if fc_red == None and fc_green == None:
    pt_data["FC"] = "0.00"
elif fc_red == None:
    pt_data["FC"] = fc_green.text
else:
    pt_data["FC"] = fc_red.text
#
# # 指數期貨
url_futures = "https://liveindex.org/futures/"
r_future = requests.get(url_futures)
soup_fut = BeautifulSoup(r_future.content, 'html5lib')
futures = {}
#

# 香港恆生 (最新）
rtf_hsi_f = soup_fut.find("a", {'title': 'Last Trade Price (HANG SENG FUTURES)'}).text
futures['HSI'] = rtf_hsi_f
# shanghai
url_ea = "https://liveindex.org/asia-pacific/"
r_ea = requests.get(url_ea)
soup_fut_ea = BeautifulSoup(r_ea.content, 'html5lib')
rtf_sh_f = soup_fut_ea.find("a", {'title': 'Last Trade Price (SHANGHAI COMPOSITE)'}).text
futures['SH'] = rtf_sh_f
#shenzhen
rtf_sz_f = soup_fut_ea.find("a", {'title': 'Last Trade Price (SHENZHEN COMPONENT)'}).text
futures['SZ'] = rtf_sz_f
# 道瓊斯30
rtf_dj_f = soup_fut.find("a", {'title': 'Last Trade Price (NASDAQ COMPOSITE FUTURES)'}).text
futures['DWJ'] = rtf_dj_f
# 德國DAX
rtf_dax_f = soup_fut.find("a", {'title': 'Last Trade Price (DAX FUTURES)'}).text
futures['DAX'] = rtf_dax_f
# 歐洲Stoxx 50
rtf_eu_f = soup_fut.find("a", {'title': 'Last Trade Price (EURO STOXX 50 FUTURES)'}).text
futures['EU'] = rtf_eu_f
# 日經225
rtf_jap_f = soup_fut.find("a", {'title': 'Last Trade Price (NIKKEI 225 FUTURES)'}).text
futures['JAP'] = rtf_jap_f
# 英國富時100
rtf_uk_f = soup_fut.find("a", {'title': 'Last Trade Price (FTSE 100 FUTURES)'}).text
futures['UK'] = rtf_uk_f
# 新加坡MSCI
rtf_sg_f = soup_fut.find("a", {'title': 'Last Trade Price (SGX NIFTY FUTURES)'}).text
futures['SG'] = rtf_sg_f

# currency
currency = {}
# USD
url_usd = "https://finance.yahoo.com/quote/usdhkd=X?ltr=1"
r_usd = requests.get(url_usd)
soup_usd = BeautifulSoup(r_usd.content, 'html5lib')
rtf_usd = soup_usd.find("span", {'class': 'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)', 'data-reactid': '14'})
fc_red = soup_usd.find("span", {'class': 'Trsdu(0.3s) Fw(500) Fz(14px) C($negativeColor)', 'data-reactid':'16'})
fc_green = soup_usd.find("span", {'class': 'Trsdu(0.3s) Fw(500) Fz(14px) C($positiveColor)', 'data-reactid':'16'})
if fc_red == None and fc_green == None:
    currency["USD"] = (rtf_usd.text, "0.00")
elif fc_red == None:
    currency["USD"] = (rtf_usd.text, fc_green.text)
else:
    currency["USD"] = (rtf_usd.text, fc_red.text)

# JAPAN
url_jpy = "https://finance.yahoo.com/quote/JPYHKD=X/"
r_jpy = requests.get(url_jpy)
soup_jpy = BeautifulSoup(r_jpy.content, 'html5lib')
rtf_jpy = soup_jpy.find("span", {'class': 'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)', 'data-reactid': '14'})
fc_red = soup_jpy.find("span", {'class': 'Trsdu(0.3s) Fw(500) Fz(14px) C($negativeColor)', 'data-reactid':'16'})
fc_green = soup_jpy.find("span", {'class': 'Trsdu(0.3s) Fw(500) Fz(14px) C($positiveColor)', 'data-reactid':'16'})
if fc_red == None and fc_green == None:
    currency["JPY"] = (rtf_jpy.text, "0.00")
elif fc_red == None:
    currency["JPY"] = (rtf_jpy.text, fc_green.text)
else:
    currency["JPY"] = (rtf_jpy.text, fc_red.text)

# Pounds
url_gbp = "https://finance.yahoo.com/quote/gbphkd=x/"
r_gbp = requests.get(url_gbp)
soup_gbp = BeautifulSoup(r_gbp.content, 'html5lib')
rtf_gbp = soup_gbp.find("span", {'class': 'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)', 'data-reactid': '14'})
fc_red = soup_gbp.find("span", {'class': 'Trsdu(0.3s) Fw(500) Fz(14px) C($negativeColor)', 'data-reactid':'16'})
fc_green = soup_gbp.find("span", {'class': 'Trsdu(0.3s) Fw(500) Fz(14px) C($positiveColor)', 'data-reactid':'16'})
if fc_red == None and fc_green == None:
    currency["GBP"] = (rtf_gbp.text, "0.00")
elif fc_red == None:
    currency["GBP"] = (rtf_gbp.text, fc_green.text)
else:
    currency["GBP"] = (rtf_gbp.text, fc_red.text)

# Euros
url_eur = "https://finance.yahoo.com/quote/EURHKD=X/"
r_eur = requests.get(url_eur)
soup_eur = BeautifulSoup(r_eur.content, 'html5lib')
rtf_eur = soup_eur.find("span", {'class': 'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)', 'data-reactid': '14'})
fc_red = soup_eur.find("span", {'class': 'Trsdu(0.3s) Fw(500) Fz(14px) C($negativeColor)', 'data-reactid':'16'})
fc_green = soup_eur.find("span", {'class': 'Trsdu(0.3s) Fw(500) Fz(14px) C($positiveColor)', 'data-reactid':'16'})
if fc_red == None and fc_green == None:
    currency["EUR"] = (rtf_eur.text, "0.00")
elif fc_red == None:
    currency["EUR"] = (rtf_eur.text, fc_green.text)
else:
    currency["EUR"] = (rtf_eur.text, fc_red.text)

# Yuan
url_yuan = "https://finance.yahoo.com/quote/CNYHKD=X/"
r_yuan = requests.get(url_yuan)
soup_yuan = BeautifulSoup(r_yuan.content, 'html5lib')
rtf_yuan = soup_yuan.find("span", {'class': 'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)', 'data-reactid': '14'})
fc_red = soup_yuan.find("span", {'class': 'Trsdu(0.3s) Fw(500) Fz(14px) C($negativeColor)', 'data-reactid':'16'})
fc_green = soup_yuan.find("span", {'class': 'Trsdu(0.3s) Fw(500) Fz(14px) C($positiveColor)', 'data-reactid':'16'})
if fc_red == None and fc_green == None:
    currency["RMB"] = (rtf_yuan.text, "0.00")
elif fc_red == None:
    currency["RMB"] = (rtf_yuan.text, fc_green.text)
else:
    currency["RMB"] = (rtf_yuan.text, fc_red.text)

# Taiwan
url_twd = "https://finance.yahoo.com/quote/TWDHKD=X/"
r_twd = requests.get(url_twd)
soup_twd = BeautifulSoup(r_twd.content, 'html5lib')
rtf_twd = soup_twd.find("span", {'class': 'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)', 'data-reactid': '14'})
fc_red = soup_twd.find("span", {'class': 'Trsdu(0.3s) Fw(500) Fz(14px) C($negativeColor)', 'data-reactid':'16'})
fc_green = soup_twd.find("span", {'class': 'Trsdu(0.3s) Fw(500) Fz(14px) C($positiveColor)', 'data-reactid':'16'})
if fc_red == None and fc_green == None:
    currency["NTD"] = (rtf_twd.text, "0.00")
elif fc_red == None:
    currency["NTD"] = (rtf_twd.text, fc_green.text)
else:
    currency["NTD"] = (rtf_twd.text, fc_red.text)


class DowJonesScrapper:
    def __init__(self):
        self.data = {1:dow_jones_data}
        self.img = url_chart

    def get_data(self):
        return self.data


class HSIScrapper:
    def __init__(self):
        self.data = {1: heng_seng_data}
        self.img = url_chart_hk

    def get_data(self):
        return self.data


class LSIScrapper:
    def __init__(self):
        self.data = {1: london_data}

    def get_data(self):
        return self.data


class CrudeOilScrapper:
    def __init__(self):
        self.data = {1: crudeoil_data}

    def get_data(self):
        return self.data


class NgScrapper:
    def __init__(self):
        self.data = {1: ng_data}

    def get_data(self):
        return self.data


class CornScrapper :
    def __init__(self):
        self.data = {1: corn_data}

    def get_data(self):
        return self.data


class WheatScrapper:
    def __init__(self):
        self.data = {1:wt_data}

    def get_data(self):
        return self.data


class RoughRiceScrapper:
    def __init__(self):
        self.data = {1: rice_data}

    def get_data(self):
        return self.data


class OatsScrapper:
    def __init__(self):
        self.data = {1: oats_data}

    def get_data(self):
        return self.data


class GoldScrapper:
    def __init__(self):
        self.data = {1: gold_data}

    def get_data(self):
        return self.data


class SilverScrapper:
    def __init__(self):
        self.data = {1:sil_data}

    def get_data(self):
        return self.data


class CopperScrapper:
    def __init__(self):
        self.data = {1: cu_data}

    def get_data(self):
        return self.data


class PlatinumScrapper:
    def __init__(self):
        self.data = {1: pt_data}

    def get_data(self):
        return self.data


class BrentScrapper:
    def __init__(self):
        self.data = {1:brent_data}

    def get_data(self):
        return self.data


class FuturesScrapper:
    def __init__(self):
        self.data = {1: futures}

    def get_data(self):
        return self.data


class CurrencyScrapper:
    def __init__(self):
        self.data = {1: currency}

    def get_data(self):
        return self.data

