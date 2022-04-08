import time

'''
Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。
时间间隔是以秒为单位的浮点小数。
每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示
'''

ticks = time.time()
print('当前时间戳为：', ticks)


'''
从返回浮点数的时间戳方式向时间元组转换 
tm_year:年份    tm_mon:月   tm_mday:日
tm_hour:小时(0~23)        tm_min:分(0~59)  tm_sec: 秒(0~61,60或61 是闰秒)
tm_wday:周(0到6(0是周一))  tm_yday:天数(1到366(儒略历))   	tm_isdst:(-1, 0, 1, -1是决定是否为夏令时的旗帜)
'''
localetime = time.localtime(time.time())
print('当前时间为：', localetime)


#格式化时间--最简单的获取可读的时间模式的函数是asctime()
localetime = time.asctime(time.localtime(time.time()))
print('当前时间为：', localetime)


'''strftime 方法来格式化日期'''
# 格式化成2022-04-08 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Fri Apr 08 11:05:15 2022形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Fri Apr 08 11:05:15 2022"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))


'''
python中时间日期格式化符号：

%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00-59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''


'''
time.sleep(secs)
推迟调用线程的运行，secs指秒数。
'''
time.sleep(10)  #延时10秒
print("END")
