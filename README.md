#### 京东商城网络爬虫 
  
docker环境搭建
```commandline  
# sudo docker run -it -d --name jd_spider_01 -p 2201:22 -p 6801:6800 jdspider:0.1 bash
# sudo docker run --name jd_mysql -e MYSQL_ROOT_PASSWORD=123456 -d -p 3308:3306 daocloud.io/library/mysql:latest  
# sudo docker run --name jd_redis -d -p 6380:6379 daocloud.io/library/redis:latest  
# sudo docker run -d --hostname rabbitmq --name jd_rabbitmq -p 5676:5672 rabbitmq:latest
```
  
  
Celery模块测试  

```commandline  
# cd Manage
# celery -A celery_schedule.application worker -l info
# celery -B -A celery_schedule.application worker -l info
```

爬虫模块运行测试
```commandline  
# cd ScrapyJd
# python3 run_dev.py
```
爬虫模块测试  
```commandline  
# vim /usr/local/lib/python3.5/dist-packages/scrapyd/default_scrapyd.conf
bind_address = 0.0.0.0
# cd ScrapyJingDong
# python3 scrapyd-deploy 100 -p ScrapyJD --version 0.1
```
