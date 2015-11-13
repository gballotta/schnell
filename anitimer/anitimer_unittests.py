import anitimer
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.ani = anitimer.AniTimer()

    def test_passframes1(self):
        self.ani.passframes(30)
        self.assertEqual(self.ani.endframe, 29)

    def test_passframes_false(self):
        self.assertFalse(self.ani.passframes(30.1))

    def test_secstoframes_int(self):
        self.assertEqual(self.ani.secstoframes(2), 50)

    def test_secstoframes_float(self):
        self.assertEqual(self.ani.secstoframes(2.5), 62)

    def test_passseconds(self):
        self.ani.passseconds(5)
        self.assertEqual(self.ani.endframe, 124)

    def test_passseconds_float(self):
        self.ani.passseconds(3.12)
        self.assertEqual(self.ani.endframe, 77)

    def test_passseconds_false(self):
        self.assertFalse(self.ani.passseconds('tot'))

    def test_setbreak_true(self):
        self.ani.passseconds(1)
        self.ani.setbreakpoint('alpa')
        self.assertEqual(self.ani.breakpoints, {'alpa': 24})

    def test_setbreak_false(self):
        self.ani.passseconds(1)
        self.ani.setbreakpoint('alpa')
        self.assertFalse(self.ani.setbreakpoint('alpa'))

    def test_setbreaks(self):
        self.ani.passseconds(1)
        self.ani.setbreakpoint('alpa')
        self.ani.passseconds(1)
        self.ani.setbreakpoint('cino')
        uno = len(self.ani.breakpoints)
        due = self.ani.breakpoints['cino']
        conf = [uno, due]
        self.assertEqual(conf, [2, 48])


if __name__ == '__main__':
    unittest.main()
