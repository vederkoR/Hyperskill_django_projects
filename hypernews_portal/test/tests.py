# -*- coding: utf-8 -*-
from hstest import dynamic_test

from .base import HyperNewsTest


class HyperNewsTestRunner(HyperNewsTest):

    funcs = [
        # 1 task
        HyperNewsTest.check_coming_soon_page,
        # 2 task
        HyperNewsTest.check_news_page,
        HyperNewsTest.check_news_page_main_link,
    ]

    @dynamic_test(data=funcs)
    def test(self, func):
        return func(self)


if __name__ == '__main__':
    HyperNewsTestRunner().run_tests()
