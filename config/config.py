import os
import pickle
import argparse

class Configure(object):
    def __init__(self, config: str, cookie: str = None):
        if not os.path.exists(config):
            os.makedirs(config)
        
        self.__config = os.path.join(config, "config.bin")

        # 如果配置文件不存在，初始化配置
        if not os.path.exists(self.__config):
            if cookie:
                # 如果命令行传入了 cookie，则直接使用
                __mediaUserToken = cookie
                print("传入了 cookie ",cookie)
            else:
                # 否则提示用户输入
                __mediaUserToken = input("\n\tmedia-user-token: ")
                print()

            __config = {
                "content-type": "configuration",
                "mediaUserToken": __mediaUserToken
            }

            with open(self.__config, 'wb') as c:
                pickle.dump(__config, c)

    def get(self):
        with open(self.__config, 'rb') as c:
            __config = pickle.load(c)

        return __config.get("mediaUserToken")

    def set(self):
        __mediaUserToken = input("\n\tmedia-user-token: ")
        print()

        with open(self.__config, 'rb') as c:
            __config = pickle.load(c)

        __config["mediaUserToken"] = __mediaUserToken

        with open(self.__config, 'wb') as c:
            pickle.dump(__config, c)

    def delete(self):
        with open(self.__config, 'rb') as c:
            __config = pickle.load(c)

        if "mediaUserToken" in __config:
            del __config["mediaUserToken"]

        with open(self.__config, 'wb') as c:
            pickle.dump(__config, c)