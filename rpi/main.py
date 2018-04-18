# coding=utf-8

from utils.weather_broadecast import broad_weather

import argparse

KITS = {
    'weather': broad_weather
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
