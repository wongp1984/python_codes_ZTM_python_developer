import unittest
import randomgame

class TestMain(unittest.TestCase):
    start = None
    end = None

    def setUp(self):
        print('About to run the test!!')
        self.start = 0
        self.end = 10
    def test_do_stuff(self):
        print('Test 1: Input correct integer.')
        result = randomgame.PromptUserInput(self.start, self.end)
        self.assertIn(result, range(self.start, self.end))

    def test_do_stuff2(self):
        print('Test 2: Input incorrect type.')
        result = randomgame.PromptUserInput(self.start, self.end)
        self.assertTrue(isinstance(result, ValueError))

    def test_do_stuff3(self):
        print('Test 3: Input not in range integer.')
        result = randomgame.PromptUserInput(self.start, self.end)
        self.assertEqual(result, 'Input is not in range.')

    # def test_do_stuff3(self):
    #     test_param = None
    #     result = main.do_stuff(test_param)
    #     self.assertEqual(result, 'Please enter number')

    # def test_do_stuff4(self):
    #     test_param = None
    #     result = main.do_stuff(test_param)
    #     self.assertEqual(result, 'Please enter number')

    def tearDown(self):
        print('Time to tear down')

if __name__ == '__main__':
    unittest.main()