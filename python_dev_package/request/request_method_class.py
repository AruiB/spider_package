# -*- coding: utf-8 -*-
# author：arui
# file：request_method_class.py
# Editing software: pycharm
# Editing Time: 2019-12-04
# Document describing: -- 爬虫请求的方法的封装


import requests
import urllib.parse


class Request(object):
    """
    基于python3.x
    """
    request_protocol = ["http", "https"]

    def __init__(self, url, urls):
        if self.__parse_url(url):
            self.url = url
        else:
            new_urls = []
            for url in urls:
                if self.__parse_url(url):
                    new_urls.append(url)
            self.urls = new_urls

    def requests_method(self):
        """
        以requests模块请求url方法
        :return:response
        """
        pass

    def selenium_method(self):
        """
        以selenium框架获取response
        :return: response
        """
        pass

    def __parse_url(self, url):
        """
        检测是否是合格的url，支持http, https
        :param url: 将要请求的url
        :return: True or False
        """
        if isinstance(url, str):
            protocol = urllib.parse.urlparse(url).scheme
            if protocol:
                if protocol in self.request_protocol:
                    return True
            return False
        raise ValueError("url")

