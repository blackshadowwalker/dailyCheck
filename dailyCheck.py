# coding: UTF-8
# !/usr/bin/python


from Monitor import *

# 全局属性，否则变量会在方法退出后被销毁
global s

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s ',
                            datefmt='%Y-%m-%d %H:%M:%S', filename='dailyCheck.log', filemode='w')
    #定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-5s : %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    try:
        s = socket.socket()
        host = socket.gethostname()
        s.bind((host, 60123))
    except:
        print('already has an instance')
    else:
        config = Config()
        monitor = Monitor()
        propFile = os.path.split(os.path.realpath(__file__))[0] + "/dailyCheck.properties"
        config.setConfigFile(propFile)
        if config.display():
            print('inited')
            monitor.setConfig(config)
            monitor.setLogDir(config.getLogDir())
            monitor.start()
