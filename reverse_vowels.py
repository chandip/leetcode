"""
write a function that takes a string as input and reverse only the vowels of a string
"""


class ReverseVowel:
    def __init__(self, word):
        self.word = word

    def reverse_vowels(self):
        string_list = list(self.word)
        left_pointer = 0
        right_pointer = len(self.word) - 1
        while left_pointer < right_pointer:
            left_is_vowel = self.is_vowel(self.word[left_pointer])
            right_is_vowel = self.is_vowel(self.word[right_pointer])
            if left_is_vowel and right_is_vowel:
                string_list[left_pointer], string_list[right_pointer] = string_list[right_pointer], string_list[
                    left_pointer]
                left_pointer += 1
                right_pointer -= 1
            if not left_is_vowel:
                left_pointer += 1
            if not right_is_vowel:
                right_is_vowel -= 1
        return ''.join(string_list)

    @staticmethod
    def is_vowel(char):
        vowels_char = ['a', 'e', 'i', 'o', 'u']
        return char.lower() in vowels_char


test_word = "Testa"
print(ReverseVowel(test_word).reverse_vowels())
