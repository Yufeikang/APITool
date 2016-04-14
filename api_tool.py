#!/usr/bin/env python3
# encoding: utf-8

"""
@version: ??
@author: kang
@license: Apache Licence 
@contact: kyf0722@gmail.com
@site: http://www.kangyufei.net
@software: PyCharm
@file: api_tool.py
@time: 4/14/2016 16:24
@description: ??
"""

from urllib import request
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem
from windows import Ui_Form
import json


class APITool(Ui_Form, QtWidgets.QWidget):
    def __init__(self):
        super(APITool, self).__init__()
        self.setupUi(self)
        self.lineEdit_Url.setText(
            'http://api.maiziedu.com/v2/getExcellentCourse/?orderBy=1&androidVersion=312&page=1&client=android&loadAd=0&pageSize=20')

        self.pushButton_go.clicked.connect(self.request)

    def request(self):
        data = request.urlopen(self.lineEdit_Url.text()).read()
        dict_data = json.loads(data.decode('utf-8'))
        if isinstance(dict_data, dict):
            text = self.display_text(dict_data)
            self.textBrowser.setText(text)

    def display_text(self, data={}, pre_str=''):
        str_data = ''
        if isinstance(data, dict):
            pre_str += '  '
            for k in data.keys():
                # print("%s : %s" % (k, data[k]))
                str_data += '\n' + pre_str + k + ':' + self.display_text(data[k], pre_str)
        elif isinstance(data, list):
            pre_str += '  '
            for index, item in enumerate(data):
                # print(d)
                str_data += '\n' + pre_str + str(index) + ':' + self.display_text(item, pre_str)
        else:
            str_data += str(data)
        return str_data


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_win = APITool()
    main_win.show()
    sys.exit(app.exec_())
