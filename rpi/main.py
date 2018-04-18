# coding=utf-8

import argparse
from utils import weather_speaker
from utils import movie_searcher

KITS = {
    'weather': weather_speaker.broad_weather,
    'movie': movie_searcher.do_fetch
}


def main():
    parse = argparse.ArgumentParser(description=u'RaspberryPi Kit CLI')
    parse.add_argument('kit_name')
    parse.add_argument('-a', action='append', help='add arg', default=[], dest='arg_collection')
    args = parse.parse_args()
    kit_name = args.kit_name
    arg_collection = args.arg_collection
    kit_func = KITS.get(kit_name)
    if kit_func:
        kit_func(arg_collection)


if __name__ == '__main__':
    main()
