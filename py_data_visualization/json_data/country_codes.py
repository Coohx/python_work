# 导入国别码字典
from pygal.i18n import COUNTRIES

def get_country_code(country_name):
    """根据指定的国家名,返回Pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            # 如果字典中存在指定的国家名,则返回其国别码,程序结束
            return code
    # 如果没有找到指定的国家,就返回None,程序结束
    return None

