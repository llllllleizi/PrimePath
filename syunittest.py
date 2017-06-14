import unittest
import codecs as cs
import shiyu_path_unit


class sytest(unittest.TestCase):

    def setUp(self):
        print "test start"

    def test_prime(self):
        for i in range(16):
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

            # self.assertEqual(sy[0],hsh[0],msg='The answer\'s length not equal to testcase\'s.')

            # for j in range(int(sy[0])):
            #     self.assertEqual(
            #         sy[j + 1],
            #         hsh[j + 1],
            #         msg='ans%d\'s %d path not correct!' % (i, j + 1))
            # print "ans%d all path correct!" % i


    def tearDown(self):
        print "test end."
    
if __name__ == "__main__":
    unittest.main()