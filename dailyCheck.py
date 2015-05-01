# coding: UTF-8
# !/usr/bin/python


from Monitor import *


if __name__ == '__main__':
        config = Config()
        monitor = Monitor()
        if config.display():
            print('inited')
            monitor.setConfig(config)
            monitor.setLogDir(config.getLogDir())
            monitor.start()

