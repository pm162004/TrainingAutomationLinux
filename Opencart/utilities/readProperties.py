import configparser
import os

config = configparser.RawConfigParser()
# config.read(os.path.abspath(os.curdir)+'\\configurations\\config.ini')
config.read("/home/web-h-028/PycharmProjects/TrainingAutomation/Opencart/configurations/config.ini")
class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url=(config.get('commonInfo', 'baseURL'))
        return url

    @staticmethod
    def getUseremail():
        username=(config.get('commonInfo', 'email'))
        return username

    @staticmethod
    def getPassword():
        password=(config.get('commonInfo', 'password'))
        return password

    @staticmethod
    def getUseremail1():
        username = (config.get('commonInfo', 'email1'))
        return username

    @staticmethod
    def getPassword1():
        password = (config.get('commonInfo', 'password1'))
        return password

    @staticmethod
    def getUseremail2():
        username = (config.get('commonInfo', 'email2'))
        return username

    @staticmethod
    def getPassword2():
        password = (config.get('commonInfo', 'password2'))
        return password


    @staticmethod
    def getUseremail3():
        username = (config.get('commonInfo', 'email3'))
        return username

    @staticmethod
    def getPassword3():
        password = (config.get('commonInfo', 'password3'))
        return password

# # Testing above methods - optional Code
# print(ReadConfig.getApplicationURL())
# print(ReadConfig.getUseremail())

