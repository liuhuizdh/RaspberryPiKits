#! /usr/bin/env python
# coding=utf-8

import argparse
from bs4 import BeautifulSoup

import requests
from comm import str2unicode
from config import logger


def __get_soup(data):
    return BeautifulSoup(data, 'html5lib')


def fetch_by_dysfz(name):
    url = u'http://www.dysfz.cc/key/{}/'.format(name)
    headers = {
        'host': 'www.dysfz.cc',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
    }
    try:
        resp = requests.get(url, timeout=5, headers=headers)
        data = resp.content
        sp = __get_soup(data)
        ll = sp.find('ul', class_='movie-list reset')
        if not ll:
            return None
        items = []
        for item in ll.find_all('li'):
            for link in item.select('h2 > a'):
                title = link.get_text()
                l = link['href']
                items.append({
                    'title': title,
                    'link': l
                })
        return items
    except Exception as e:
        logger.error(e, exc_info=True)
    return None


def fetch_by_llduang(name):
    url = u'http://www.llduang.com/?s={}'.format(name)
    headers = {
        'host': 'www.llduang.com',
        'referer': 'http://www.llduang.com/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
    }
    try:
        resp = requests.get(url, timeout=5, headers=headers)
        data = resp.content
        sp = __get_soup(data)
        ll = sp.select('div.article')
        if not ll:
            return None
        items = []
        for item in ll:
            for i in item.select('h2 > a'):
                items.append({
                    'title': i.get_text(),
                    'link': i['href']
                })
        return items
    except Exception as e:
        logger.error(e, exc_info=True)
    return None


def __wrap_item(item):
    logger.info(u'{}\n{}\n'.format(item['title'], item['link']))
    return {
        "Title": item['title'],
        "Url": item['link']
    }


def do_fetch(names):
    for name in names:
        logger.info(name)
        name = str2unicode(name)
        links = fetch_by_llduang(name)
        result = None
        if not links:
            links = fetch_by_dysfz(name)
        if links:
            result = [__wrap_item(item) for item in links]
        return result


if __name__ == '__main__':
    do_fetch(['Silicon Valley'])
