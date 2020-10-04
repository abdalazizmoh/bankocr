import unittest
import bankocr

class TestReadOCR(unittest.TestCase):

    def test_read_zeroes(self):
        input = " _  _  _  _  _  _  _  _  _ \n"\
                "| || || || || || || || || |\n"\
                "|_||_||_||_||_||_||_||_||_|"
        ocr = list(input.split("\n"))

        list_numbers = bankocr.readocr(ocr)
        self.assertTrue(list_numbers[0] == "000000000")

    def test_read_ones(self):
        input = "                           \n"\
                "  |  |  |  |  |  |  |  |  |\n"\
                "  |  |  |  |  |  |  |  |  |"
        ocr = list(input.split("\n"))

        list_numbers = bankocr.readocr(ocr)
        self.assertTrue(list_numbers[0] == "111111111")
    
    def test_invalide_number(self):
        input = "  |                        \n"\
                "  |  |  |  |  |  |  |  |  |\n"\
                "  |  |  |  |  |  |  |  |  |"
        ocr = list(input.split("\n"))

        list_numbers = bankocr.readocr(ocr)
        self.assertTrue(list_numbers[0] == "Error in data")

if __name__ == '__main__':
    unittest.main()