# Created by mqgao at 2019/2/18

"""
Feature: #Enter feature name here
# Enter feature description here

Scenario: #Enter scenario name here
# Enter steps here

Test File Location: # Enter
"""


import itchat
from itchat.content import FRIENDS, TEXT


itchat.auto_login()


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    pass
