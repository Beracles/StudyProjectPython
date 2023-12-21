#from name_function import get_formatted_name
#print("Enter 'quit' at any time to quit.")
#while True:
#    first=input("Please give me a first name:")
#    if first=='quit':
#        break
#    last=input("Please give me a last name:")
#    if last=='quit':
#        break
#    formatted_name=get_formatted_name(first,last)
#    print("Neatly formatted name: "+formatted_name+'.')

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name=get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')
    def test_first_middle_last_name(self):
        """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
        formatted_name=get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')

unittest.main()

