# coding=utf-8

LOGGING_CONF = {
    'version': 1,
    'formatters': {
        '': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': ''
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console']
        }
    }

}

WEATHER_CODE = {
    "AP010001": u"API请求参数错误。",
    "AP010002": u"没有权限访问这个API接口。在此查看你有权访问的API接口。",
    "AP010003": u"API密钥key错误。",
    "AP010004": u"签名错误。",
    "AP010005": u"你请求的API不存在。",
    "AP010006": u"没有权限访问这个地点。",
    "AP010007": u"JSONP请求需要使用签名验证方式。",
    "AP010008": u"没有绑定域名。在此绑定域名。",
    "AP010009": u"API请求的user-agent与你设置的不一致。",
    "AP010010": u"没有这个地点。",
    "AP010011": u"无法查找到指定IP地址对应的城市。",
    "AP010012": u"你的服务已经过期。在此续费。",
    "AP010013": u"访问量余额不足。联系客服购买更多访问量。",
    "AP010014": u"免费用户超过了每小时访问量额度。一小时后自动恢复。",
    "AP010015": u"暂不支持该城市的车辆限行信息。",
    "AP100001": u"系统内部错误：数据缺失。",
    "AP100002": u"系统内部错误：数据错误。",
    "AP100003": u"系统内部错误：服务内部错误。"
}
WEATHER_DESC = {
    'travel': u'旅游',
    'uv': u'紫外线',
    'car_washing': u'洗车',
    'dressing': u'穿衣',
    'sport': u'运动',
}

BAIDU_KEY = 'Yoq0CToDINxZyGosBi9rsCSL'
BAIDU_S_KEY = '74b768788b82790645a1aaa0ba5a9a8e'
WEATHER_KEY = 'opmc13gzz833wulw'
