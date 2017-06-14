#-*- coding=utf-8 -*-
from selenium import webdriver
import unittest, time
from HTMLTestRunner import HTMLTestRunner
import unittest
import codecs as cs
import shiyu_path_unit
import sys


class sytest(unittest.TestCase):

    def setUp(self):
        print "test start"

    def test_prime(self):
        for i in range(5):
            case='case/case'+str(i)+'.txt'
            edges = shiyu_path_unit.readGraph(case)
            nodelen = len(edges)
            nodes = list(range(nodelen))
            shiyu_path_unit.process(nodes,edges,i)

            answer = open('hshanswer/answer' + str(i) + '.txt','r')
            ans = open('ans/ans' + str(i) + '.txt','r')

            hsh = answer.readlines()
            sy = ans.readlines()

            if hsh == sy:
                print "ans"+ '%d'%i +" is correct!"
            else:
                print "ans"+ '%d'%i +" is incorrect!"

    def tearDown(self):
        print "test end."

if __name__ == "__main__":

    reload(sys)
    sys.setdefaultencoding('utf8')
    testunit = unittest.TestSuite()
    testunit.addTest(sytest("test_prime"))

    # 按照一定格式获取当前时间
    now = time.strftime("%Y-%m-%d %H-%M-%S")

    # 定义报告存放路径
    # filename = './report/result.html'
    filename = './report/shiyu-' + now + '-result.html'
    fp = open(filename, 'wb')

    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,                  # 指定测试报告文件
                        title='测试报告_施宇',        # 定义测试报告标题 
                        description='用例执行状况：')    # 定义测试报告副标题
    runner.run(testunit)    # 运行测试用例
    fp.close()  
    # 关闭报告文件