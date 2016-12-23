# -*- coding: utf-8 -*-
# Date: 2016-12-23

def get_formatted_name(first, last, middle=''):
    """General a neatly formatted full name"""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()

def custom_info(city, country, population=''):
    """统计游客所在的国家和城市"""
    if population:
        customer_info = city + ", " + country
        customer_info = customer_info.title()
        return customer_info + " - population " + population
    else:
        customer_info = city + ", " + country
        return customer_info.title()
