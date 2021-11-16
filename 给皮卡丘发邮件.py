#此程序是在非常仓促的情况下给女朋友写的，而且是初稿，不太能代表本人的编程水平，特此告知
#主要是因为和女朋友异国，时差比较长，但微信的api接口又关了，所以只能写一个定时发送邮件来哄一下

import smtplib
from email.mime.text import MIMEText
import schedule
import time
import random
import threading

def auto_email(title, content):
    host = 'smtp.163.com'
    user = 'miao_lucks'
    passcode = 'TFVCQAUHCWXRKKOD'
    sender = 'miao_lucks@163.com'
    receivers = ['miao_lucks@163.com']

    message = MIMEText(str(content), 'plain', 'utf-8')
    message['Subject'] = str(title)
    message['From'] = sender
    message['To'] = receivers[0]

    # 登录并发送邮件
    try:
        smtpObj = smtplib.SMTP()
        # 连接到服务器
        smtpObj.connect(host, 25)
        # 登录到服务器
        smtpObj.login(user, passcode)
        # 发送
        smtpObj.sendmail(
            sender, receivers, message.as_string())
        # 退出
        smtpObj.quit()
        print('success')
    except smtplib.SMTPException as e:
        print('error', e)  # 打印错误


def random_time():
    hour = random.randint(0, 7)
    minute = random.randint(0, 59)
    return str(hour + ":" + minute)


def context(index):
    greeting = "亲爱的皮卡丘大人，您好\n"
    testing = """特此告知：此邮件由喵拉克斯大人的小助手羊驼发出，小助手还在被调教中，这个时间亲爱的喵拉克丝大人应该已经睡觉觉了，但有什么不满还是可以跟羊驼说哟～\n
另外，羊驼小助手刚刚被开发，如果丘大人想要羊驼小助手有什么功能，都可以找猫猫提出的，猫猫也会抽时间去继续给羊驼增加功能"""
    tab = "\n"
    message_bank = ['听说猫猫一族一旦睡着，就会有灵魂出窍，漂洋过海的力量，就可以飘到两万里外的皮卡丘身边了。那今天晚上猫猫能不能"嗖"的一下飞过去亲一下皮卡丘，再"嗖"的一下再飞回来呢？']

    sign = """想玩皮卡丘屁股的喵拉克丝大人\n
11月16日\n
羊驼小助手测试版上线第一天"""

    return str(greeting+tab+testing+tab+tab+tab+message_bank[0]+tab+tab+tab+sign)



# auto_email("来自亲爱的喵拉克丝大人",context(1))


# interval = 1000
#
# timer = threading.Timer(interval, auto_email("来自亲爱的喵拉克丝大人",context(1)) , args=None, kwargs=None)

# schedule.every().day.at("11:59").do(auto_email("来自亲爱的喵拉克丝大人",context(1)))


def job_that_executes_once():
    print('Hello')
    return schedule.CancelJob
    schedule.every().minute.at('00:05').do("来自亲爱的喵拉克丝大人",context(1))

while True:
    schedule.run_pending()
    time.sleep(1)

main()









# schedule.every(10).minutes.do(job)               # 每隔 10 分钟运行一次 job 函数
# schedule.every().hour.do(job)                    # 每隔 1 小时运行一次 job 函数
# schedule.every().day.at("10:30").do(job)         # 每天在 10:30 时间点运行 job 函数
# schedule.every().monday.do(job)                  # 每周一 运行一次 job 函数
# schedule.every().wednesday.at("13:15").do(job)   # 每周三 13：15 时间点运行 job 函数
# schedule.every().minute.at(":17").do(job)        # 每分钟的 17 秒时间点运行 job 函数

