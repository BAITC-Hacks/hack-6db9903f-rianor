import unittest
from main import check_image

class TestDefectDetection(unittest.TestCase):
    def test_ok_image(self):
        self.assertEqual(check_image("ok.png"), "OK")

    def test_defect_image(self):
        self.assertEqual(check_image("defect.png"), "DEFECT")

if __name__ == "__main__":
    unittest.main()
