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
```bash
venv/bin/python rpi/main.py weather -a '成都' -a '北京'
```

## extends

More `WEATHER_DESC` see: [https://www.seniverse.com/doc#life](https://www.seniverse.com/doc#life)