from utestex1 import *
from utestex2 import *
import unittest
def suite():
    suite = unittest.TestSuite()
    suite.addTest(MyTestcaseClass1('mytestcase1'))
    suite.addTest(MyTestcaseClass2('mytestcase2'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
