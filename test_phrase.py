class TestPhrase:
    def test_phrase(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, f"Phrase {phrase} contains more than 14 symbols"
