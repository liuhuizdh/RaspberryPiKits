# RaspberryPi Kits

* Weather Speaker Dependencies
    * [http://yuyin.baidu.com](http://yuyin.baidu.com/app)
    * [https://www.seniverse.com/doc#now](https://www.seniverse.com/doc#now)

## pre

export your key to environment value

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