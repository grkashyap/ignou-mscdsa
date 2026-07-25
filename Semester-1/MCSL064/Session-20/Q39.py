class BoyerMooreAlgorithm:
    def create_bad_character_table(self, pattern):
        """Store the last position of every character in the pattern."""
        bad_character = {}

        for index, character in enumerate(pattern):
            bad_character[character] = index

        return bad_character

    def search(self, text, pattern):
        """Return all positions where pattern occurs in text."""
        if not pattern or len(pattern) > len(text):
            return []

        bad_character = self.create_bad_character_table(pattern)
        text_length = len(text)
        pattern_length = len(pattern)
        matches = []
        shift = 0

        while shift <= text_length - pattern_length:
            pattern_index = pattern_length - 1

            # Compare characters from right to left.
            while (pattern_index >= 0 and
                   pattern[pattern_index] == text[shift + pattern_index]):
                pattern_index -= 1

            if pattern_index < 0:
                matches.append(shift)

                # Shift to check for another (possibly overlapping) match.
                if shift + pattern_length < text_length:
                    next_character = text[shift + pattern_length]
                    shift += pattern_length - bad_character.get(next_character, -1)
                else:
                    shift += 1
            else:
                # Use the bad-character rule to skip comparisons.
                mismatched_character = text[shift + pattern_index]
                last_position = bad_character.get(mismatched_character, -1)
                shift += max(1, pattern_index - last_position)

        return matches


if __name__ == "__main__":
    text = "ABAAABCDABCABC"
    pattern = "ABC"

    boyer_moore = BoyerMooreAlgorithm()
    matches = boyer_moore.search(text, pattern)

    print("Text:", text)
    print("Pattern:", pattern)
    print("Pattern found at positions:", matches)
