import unittest
import LAB4


class testCaeserCypher(unittest.TestCase):
    def setUp(self):
        # Use this as a test message to test all edges of upper and lower case as well as middle
        # Include non alpha characters as well
        self.testMessage = 'ABCD LMNO WXYZ abcd lmno wxyz 1234 !.!('

    def test_Encrypt(self):
        self.assertEqual(LAB4.encrypt(self.testMessage, 0), self.testMessage)
        self.assertEqual(LAB4.encrypt(self.testMessage, 12), 'MNOP XYZA IJKL mnop xyza ijkl 1234 !.!(')
        self.assertEqual(LAB4.encrypt(self.testMessage, -3), 'XYZA IJKL TUVW xyza ijkl tuvw 1234 !.!(')
        self.assertEqual(LAB4.encrypt(self.testMessage, 3.5), 'error')
        self.assertEqual(LAB4.encrypt(5, 7), 'error')
        self.assertEqual(LAB4.encrypt(self.testMessage, 13), LAB4.decrypt(self.testMessage, 13))

    def test_Decrypt(self):
        for i in range(-100, 100):
            self.assertEqual(LAB4.decrypt(LAB4.encrypt(self.testMessage, i), i), self.testMessage)
        self.assertEqual(LAB4.decrypt(LAB4.encrypt(self.testMessage, 3), 3), self.testMessage)
        self.assertEqual(LAB4.decrypt(LAB4.encrypt(self.testMessage, -3), -3), self.testMessage)
        self.assertEqual(LAB4.decrypt('message', -3.6), 'error')
        self.assertEqual(LAB4.decrypt(45, 12), 'error')


if __name__ == '__main__':
    unittest.main()