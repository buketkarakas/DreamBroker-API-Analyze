import unittest
import analyzeText

class TestAnalyzeText(unittest.TestCase):
    def test_count_chars_with_lowerEnglishAlphabet(self):
        actual = analyzeText.count_characters("Hello my friend")
        expected = [{"d":1},{"e":2},{"f":1},{"h":1},{"i":1},{"l":2},{"m":1},{"n":1},{"o":1},{"r":1},{"y":1}]
        self.assertEqual(actual, expected)
    
    def test_count_chars_with_UpperEnglishAlphabet(self):
        actual = analyzeText.count_characters("HELLO MY FRIEND")
        expected = [{"d":1},{"e":2},{"f":1},{"h":1},{"i":1},{"l":2},{"m":1},{"n":1},{"o":1},{"r":1},{"y":1}]
        self.assertEqual(actual, expected)
    
    def test_count_chars_with_EnglishAlphabetAndSpecialChar(self):
        actual = analyzeText.count_characters("Hello my friend!!!!!!")
        expected = [{"d":1},{"e":2},{"f":1},{"h":1},{"i":1},{"l":2},{"m":1},{"n":1},{"o":1},{"r":1},{"y":1}]
        self.assertEqual(actual, expected)
    
    def test_count_chars_with_EmptyText(self):
        actual = analyzeText.count_characters("")
        expected = []
        self.assertEqual(actual, expected)
    
    def test_count_words(self):
        actual = analyzeText.count_words("Hello I am Buket and this is test           test")
        expected = 9
        self.assertEqual(actual, expected)
    
    def test_count_words_empty(self):
        actual = analyzeText.count_words("")
        expected = 0
        self.assertEqual(actual, expected)
    
    def test_analyze_text_length_withoutanyspace(self):
        actual = analyzeText.analyze_text_length("ThisIsMeTesting")
        expected = {
            "withSpaces": 15,
            "withoutSpaces": 15
            }
        self.assertEqual(actual, expected)
    
    def test_analyze_text_length_withspace(self):
        actual = analyzeText.analyze_text_length("This Is Me Testing   ")
        expected = {
            "withSpaces": 21,
            "withoutSpaces": 15
            }
        self.assertEqual(actual, expected)
    
    def test_analyze_text_length_withspace(self):
        actual = analyzeText.analyze_text_length("")
        expected = {
            "withSpaces": 0,
            "withoutSpaces": 0
            }
        self.assertEqual(actual, expected)