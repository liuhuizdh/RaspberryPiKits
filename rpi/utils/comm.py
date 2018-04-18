# coding=utf-8

from config import logger


def str2unicode(s):
    try:
        if not isinstance(s, unicode):
            s = s.decode('utf-8')
    except Exception as e:
        logger.error(e, exc_info=True)
    finally:
        return s
