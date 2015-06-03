# coding=utf-8

import os
import re
import sys
import threading
import socket

from Email import *


class Monitor(threading.Thread):
    "监控模块"
    name = "监控模块"
    logDir = ""
    logList = []
    loopTime = 60
    email = Email()
    config = Config()

    def setLogDir(self, logDir):
        self.logDir = logDir

    def setConfig(self,config):
        self.config = config

    def __checkTimeIsOk(self):
        hour = time.localtime(time.time())[3]
        min = time.localtime(time.time())[4]
        if hour == 23 and min == 55:
            return True
        return False

    def run(self):
        logging.info(self.name + " 启动")
        time.sleep(1)
        dotsCount = 0
        while True:
            if self.__checkTimeIsOk():
                print('.')
                logging.info("logDir: %s" + self.logDir)
                #昨天
                yestday =  time.strftime('%Y-%m-%d',time.localtime(time.time() - 24*60*60))
                regstr = '(.*error\.log\.' + yestday + '\.log)|(.*error\.log$)'
                fileList = os.listdir(self.logDir)
                fileList.sort()
                logging.info("fileList: %s", fileList)
                self.logList.clear()
                for file in fileList:
                    if re.match(regstr, file):
                        self.logList.append(self.logDir + '/' + file)
                self.logList.sort()
                logging.info("logList: %s", self.logList)
                self.email.setConfig(self.config)
                hostname = socket.gethostname()
                ip = socket.gethostbyname(hostname)
                content = hostname + "/" + ip + "\r\n"
                if len(self.logList) > 0:
                    content += "错误日志列表: \r\n"
                    for file in self.logList:
                        content += file + "\r\n"
                else:
                    content += "暂无错误日志，其他日志列表: \r\n"
                    for file in fileList:
                        content += file + "\r\n"
                self.email.send_mail(self.config.getAppName()+"-错误日志", content, self.logList)
                logging.info('sleep  %d ', self.loopTime)
            else:
                sys.stdout.write( '.')
                sys.stdout.flush()
                dotsCount += 1
                if dotsCount >= 100:
                    sys.stdout.write('\n')
                    dotsCount = 0
            time.sleep(self.loopTime)

