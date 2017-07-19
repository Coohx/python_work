"""
pygal将“国家码”存储在模块i18n中，字典COUNTRIES的键和值分别为国家码和国家名
"""
from pygal.i18n import COUNTRIES

# 将字典的键(国家码)单独提出来按字母顺序排列
for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])

