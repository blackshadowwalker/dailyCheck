# coding=utf-8

import os
import re
import time
import threading

from Email import *


class Monitor(threading.Thread):
    "监控模块"
    name = "监控模块";
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
        hour = time.localtime(time.time())[3];
        min = time.localtime(time.time())[4];
        print(hour, min)
        if hour == 18 and min == 27:
            return True
        return False

    def run(self):
        print(self.name + " 启动")
        while True:
            if self.__checkTimeIsOk():
                print("logDir:" + self.logDir)
                #昨天
                localTime =  time.strftime('%Y-%m-%d',time.localtime(time.time() - 24*60*60))
                regstr = '.*error.log.' + localTime +'.log'
            #    print('regstr: ' + regstr)
                fileList = os.listdir(self.logDir)
                print("fileList:", fileList)
                self.logList.clear()
                for file in fileList:
                    if re.match(regstr, file):
                        self.logList.append(self.logDir + '/' + file)
                print("logList :", self.logList)
                self.email.setConfig(self.config)
                self.email.send_mail(self.config.getAppName()+"-错误日志", self.config.getAppName()+"请看附件", self.logList)
                print('sleep ', self.loopTime)
            time.sleep(self.loopTime)

#ezhe-api-error.log.2015-01-11.log