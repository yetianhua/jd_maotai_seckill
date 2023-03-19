import sys
import os
from jd_spider_requests import SpiderSession
from jd_spider_requests import QrLogin
from jd_spider_requests import JdSeckill
from timer import Timer

timer = Timer()
print(timer.local_jd_time_diff())


# 验证cookies是否有效
# spider_session = SpiderSession()
# spider_session.load_cookies_from_local()
# qrlogin = QrLogin(spider_session)
# qrlogin._validate_cookies()

# python 装饰器

# 登录
# jd_seckill = JdSeckill()
# jd_seckill.login_by_qrcode()

# 预约
jd_seckill = JdSeckill()
jd_seckill.reserve()