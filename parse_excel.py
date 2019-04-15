# Created by mqgao at 2019/2/18

"""
Feature: #Enter feature name here
# Enter feature description here

Scenario: #Enter scenario name here
# Enter steps here

Test File Location: # Enter
"""

import pandas as pd


def get_records(filename):
    content = pd.read_excel(filename)
    content = content.fillna('')

    content_dict = content.to_dict()

    return content_dict


if __name__ == '__main__':
    filename = '/Users/mqgao/Downloads/【拿不到 offer全额退款】人工智能与 NLP _ CV 课程(第三期)招生 (6).xls'
    get_records(filename)
