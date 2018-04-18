# RaspberryPi Kits


* Weather Speaker
* Video Searcher

## pre

export your key to environment value

> [http://yuyin.baidu.com](http://yuyin.baidu.com)

> [https://www.seniverse.com](https://www.seniverse.com)

```bash
export BAIDU_KEY='xxx'
export BAIDU_S_KEY='xxx'
export WEATHER_KEY='xxx'
```

## build

```bash
virtualenv venv
venv/bin/pip install -r requestmetns.txt
```

## run

* weather speaker

```bash
venv/bin/python rpi/main.py weather -a '成都' -a '北京'
```

* movie searcher

```bash
venv/bin/python rpi/main.py movie -a 'Silicon valley'
```

## extends

More `WEATHER_DESC` see: [https://www.seniverse.com/doc#life](https://www.seniverse.com/doc#life)