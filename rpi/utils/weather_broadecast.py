# coding=utf-8

import datetime
import logging.config

import pygame
import requests

from config import WEATHER_CODE, WEATHER_DESC, LOGGING_CONF, BAIDU_KEY, BAIDU_S_KEY, WEATHER_KEY

logging.config.dictConfig(LOGGING_CONF)
logger = logging.getLogger('')

VOICE_SPEED = 3
VOICE_VOL = 15

VOICE_DIR = '.'


class BaiDuVoice(object):
    def __init__(self):
        self._key = BAIDU_KEY
        self._s_key = BAIDU_S_KEY
        self._token = None
        self.filename = None

    def _get_token(self):
        url = "https://openapi.baidu.com/oauth/2.0/token"
        querystring = {"grant_type": "client_credentials", "client_id": self._key,
                       "client_secret": self._s_key}
        try:
            response = requests.get(url, params=querystring)
            data = response.json()
            token = data.get('access_token')
            self._token = token
        except Exception as e:
            logger.error(e.message)

    def get_voice(self, text):
        self._get_token()
        if not self._token:
            return
        url = "https://tsn.baidu.com/text2audio"
        querystring = {"tok": self._token, "tex": text, "cuid": "ji", "ctp": "1", "lan": "zh", "spd": VOICE_SPEED,
                       "vol": VOICE_VOL}

        resp = requests.get(url, params=querystring)
        chunk_size = 200
        path = '{}/{}.mp3'.format(VOICE_DIR, datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
        with open(path, 'wb') as fd:
            for chunk in resp.iter_content(chunk_size):
                fd.write(chunk)
        self.filename = path


class WeatherFetcher(object):
    def __init__(self, location=u'成都'):
        self._key = WEATHER_KEY
        self._location = location

    def get_weather(self):
        """
        获取实时天气
        :param location:
        :return:
        """
        params = {
            "key": self._key,
            "location": self._location,
            "language": "zh-Hans",
            "unit": "c"
        }
        url = 'https://api.seniverse.com/v3/weather/now.json'
        try:
            resp = requests.get(url, params=params, timeout=5)
            if resp.status_code == 200:
                results = resp.json().get('results')
                items = []
                for item in results:
                    logger.info(item)
                    now = item.get('now')
                    desc = now.get('text')
                    temp = now.get('temperature')
                    content = u'{},今天:{},温度:{} 摄氏度'.format(self._location, desc, temp)
                    items.append(content)
                return u'。'.join(items)
            else:
                status_code = resp.json().get('status_code')
                msg = WEATHER_CODE.get(status_code)
                return msg or u'天气获取失败'
        except Exception as e:
            logger.error(e.message)
            return e.message

    def get_suggestion(self):
        """
        获取生活指数
        :return:
        """
        params = {
            "key": self._key,
            "location": self._location,
            "language": "zh-Hans"
        }
        url = 'https://api.seniverse.com/v3/life/suggestion.json'
        try:
            resp = requests.get(url, params=params, timeout=5)
            if resp.status_code == 200:
                results = resp.json().get('results')
                items = []
                for item in results:
                    suggestion = item.get('suggestion')
                    data = []
                    for k in suggestion.keys():
                        name = WEATHER_DESC.get(k)
                        if not name:
                            continue
                        v = suggestion.get(k)
                        logger.info(u"{}_{}".format(k, v))
                        value = u';'.join(v.values())
                        data.append(u'{},{}'.format(name, value))
                    items.append(u'。'.join(data))
                return u'。'.join(items)
            else:
                status_code = resp.json().get('status_code')
                msg = WEATHER_CODE.get(status_code)
                return msg or u'生活指数获取失败'
        except Exception as e:
            logger.error(e.message)
            return e.message


def broad_weather(location):
    wf = WeatherFetcher(location=location)
    weather = wf.get_weather()
    suggestion = wf.get_suggestion()
    logger.info(u'天气:{}'.format(weather))
    logger.info(u'建议:{}'.format(suggestion))
    bd = BaiDuVoice()
    bd.get_voice(u"{},以下是建议:{}".format(weather, suggestion))
    if bd.filename:
        pygame.mixer.init()
        pygame.mixer.music.load(bd.filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue


if __name__ == '__main__':
    broad_weather(u'成都')
