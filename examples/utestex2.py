import unittest
def sub(x,y):
    return x-y     
class MyTestcaseClass2(unittest.TestCase):          
    def test2(self):
        #Arrange
        a=5
        b=3
        #Act
        result=sub(a,b)
        #Assert
        self.assertEqual(a-b,result)   
    
if __name__=='__main__':
    unittest.main()
