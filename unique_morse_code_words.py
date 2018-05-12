class Solution(object):
    def description(self):
        return "Solution to the unique morse code words problem"

    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        morse_dict = {}
        for i, char in enumerate(alphabet):
            morse_dict[char] = morse[i]

        morse_transformations = {}
        for w in words:
            morse_w = [""]*len(w)
            for i, char in enumerate(w):
                morse_w[i] = morse_dict.get(char)
            morse_w = "".join(morse_w)
            if morse_transformations.get(morse_w) is None:
                morse_transformations[morse_w] = 1

        return len(morse_transformations.keys())



