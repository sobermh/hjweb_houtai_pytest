"""
@author:maohui
@time:2022/6/17 14:34
  　　　　　　　 ┏┓    ┏┓+ +
  　　　　　　　┏┛┻━━━━┛┻┓ + +
  　　　　　　　┃        ┃ 　 
  　　　　　　　┃     ━  ┃ ++ + + +
  　　　　　 　████━████ ┃+
  　　　　　　　┃        ┃ +
  　　　　　　　┃   ┻    ┃
  　　　　　　　┃        ┃ + +
  　　　　　　　┗━┓   ┏━━┛
  　　　　　　　  ┃   ┃
  　　　　　　　  ┃   ┃ + + + +
  　　　　　　　  ┃   ┃　　　Code is far away from bug with the animal protecting
  　　　　　　　  ┃   ┃+ 　　　　神兽保佑,代码无bug
  　　　　　　　  ┃   ┃
  　　　　　　　  ┃   ┃　　+
  　　　　　　　  ┃   ┗━━━━━━━┓ + +     
  　　　　　　　  ┃           ┣┓
  　　　　　　　  ┃           ┏┛
  　　　　　　　  ┗┓┓┏━━━━━┳┓┏┛ + + + +
  　　　　　　　   ┃┫┫     ┃┫┫
  　　　　　　　   ┗┻┛     ┗┻┛+ + + +
"""
import logging
import logging.handlers
import datetime

def logger():
    logger=logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)

    rf_handler=logging.handlers.TimedRotatingFileHandler('all.log',when='midnight',interval=1,backupCount=7,atTime=datetime.time(0, 0, 0, 0))
    rf_handler.setFormatter(logging.Formatter("%(asctime)s-%(levelname)s-%(message)s"))

    f_handler=logging.FileHandler('error.log')
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s[:%(lineno)d]-%(message)s"))

    # my_format='%(asctime)s-%(filename)s-%(module)s-%(lineno)d'

    # logging.basicConfig(
    #     filename='my.log',
    #     level=logging.INFO,
    #     format=my_format
    # )
    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)
    return logger