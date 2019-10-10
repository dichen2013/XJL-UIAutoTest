# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 17:46
# @Author  : DannyDong
# @File    : login_case.py
# @describe: 登录测试用例

import unittest

from Utils.get_log import LogInfo
from Utils.read_ini import ReadIni
from Test.Case.base_case import LoginBaseCase


class LoginCase(LoginBaseCase, LogInfo):
    """ 登录测试用例 """

    @LogInfo.get_error
    def test_000(self):
        """ 登录成功 """
        self.log.info('TestCase000 Start Running')

        # 获取用户名和密码
        username = ReadIni('Sys_config.ini', 'Base').get_value('username')
        password = ReadIni('Sys_config.ini', 'Base').get_value('password')

        # 获取Org名称
        org_name = self.login.login_suc(username, password)
        self.assertEqual('重构测试Rock', org_name, '机构名称不一致 --- 测试用例不通过')


if __name__ == '__main__':
    unittest.main()
