#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> exceptions
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/3/18 17:28
@Desc   ：
==================================================
"""


class TaskNotStartError(BaseException):
    """ Inappropriate argument value (of correct type). """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class TaskRunCompletedError(BaseException):
    """ Inappropriate argument value (of correct type). """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
