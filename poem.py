# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
rawdata = '''我
我的
眼睛
妳
妳的
心
溫柔
日子
雨
風
天空
雲
等待
哭泣
戀愛
相遇
分離
忘記
心醉
驀然
吹過
思念
靈魂
停止'''
words = rawdata.split('\n')
def poem():
    n = np.random.randint(2, 8) # 2-8句, 決定有幾句

    for i in range(n):
        m = np.random.randint(1, 6) # 決定每句的長度
        sentence = np.random.choice(words, m, replace=False)
        print(" ".join(sentence))
poem()
