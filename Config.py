# coding=utf-8

import logging

class Config:
    #配置
    PROP_APP_NAME = "app.name"
    PROP_LOG_DIR = "log.dir"
    PROP_LOG_PATTERM = "log.file.patterm"
    ConfigFile = "dailyCheck.properties"
    prop = {}

    mailto_list = ["BlackShadowWalker@163.com","yangbing@gozap.com"]
    mail_host = "smtp.126.com"  # 设置服务器
    mail_user = "crash_client"  # 用户名
    nick_name = "错误日志清查" #发件人昵称
    mail_pass = "vqldobvhsssobpfb"  # 口令
    mail_postfix = "126.com"  # 发件箱的后缀
    mail_from = mail_user + "@" + mail_postfix;

    def setConfigFile(self, fileName):
        self.ConfigFile = fileName
        print('set conf file ', self.ConfigFile)

    def getLogDir(self):
        return self.prop[self.PROP_LOG_DIR]

    def getLogPatterm(self):
        return self.prop[self.PROP_LOG_PATTERM]

    def getAppName(self):
        return self.prop[self.PROP_APP_NAME]

    def display(self):

        print("init ", self.ConfigFile)
        try:
            propFile = open(self.ConfigFile, "r")
            for line in propFile:
                if line.find('=') > 0 and not line.startswith('#'):
                    str = line.replace('\n', '').split('=')
                    self.prop[str[0]] = str[1]
                # print(str[0], "=", str[1])
            propFile.close()
            if self.prop.get(self.PROP_LOG_DIR) == None:
                raise ValueError('please set '+self.PROP_LOG_DIR)
            if self.prop.get(self.PROP_LOG_PATTERM) == None:
                raise  ValueError('please set '+self.PROP_LOG_PATTERM)
        except Exception as e:
            logging.error(e)
        else:
            return True
