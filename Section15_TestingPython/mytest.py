import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print('About to run the test!!')

    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'gretfsdfsf'
        result = main.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter number')

    def test_do_stuff4(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter number')

    def tearDown(self):
        print('Time to tear down')


if __name__ == '__main__':
    unittest.main()