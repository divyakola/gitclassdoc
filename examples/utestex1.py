import unittest
def add(x,y):
    return x+y
class MyTestcaseClass1(unittest.TestCase):       
    def test1(self):
        #Arrange
        a=5
        b=3
        #Act
        result=add(a,b)
        #Assert
        self.assertEqual(a+b,result)     
    
if __name__=='__main__':
    unittest.main()
