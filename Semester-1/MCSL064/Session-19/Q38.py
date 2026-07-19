class KMPAlgorithm:

    def __pre_process_pattern(self, pattern: str) -> list:
        """
        Compute LPS - Longest Prefix Suffix
        """
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1
        print(f'Computing LPS - Longest Prefix Suffix for patten {pattern}')
        print(f'Initial LPS: {lps}')

        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                print(f'Match at {i}: pattern[{i}] = pattern[{length-1}], LPS[{i}] = {length}')
                i += 1
            else:
                if length != 0:
                    length = lps[length-1]
                    print(f'Mismatch at {i}: backtrack length to {length}')
                else:
                    lps[i] = 0
                    print(f'No prefix match at {i}: LPS[{i}] = 0')
                    i += 1
        print(f'Final LPS array: {lps}')
        return lps

    def kmp_search(self, text: str, pattern: str) -> list:
        n, m = len(text), len(pattern)
        if m == 0:
            return []

        lps = self.__pre_process_pattern(pattern)
        matches = []
        i,j,comparisons = 0,0,0
        print('Searching using KMP algorithm:')
        print(f'Text: {text}')
        print(f'Pattern: {pattern}')

        while i < n:
            comparisons += 1
            print(f'Comparing text[{i}]={text[i]} with pattern[{j}]={pattern[j]}')
            if text[i] == pattern[j]:
                print(f'Match at {i}: pattern[{i}] = {pattern[j]}')
                i, j = i + 1, j + 1
                if j == m:
                    match_pos = i-j
                    matches.append(match_pos)
                    print(f'Pattern found at position {match_pos}: {text[match_pos]}')
                    j = lps[j-1]
                    print(f'Using LPS: next j ={j}')
            elif i<n and text[i] != pattern[j]:
                if j !=0:
                    j = lps[j-1]
                    print(f'Mismatch Using LPS: j = lps[{j}] = {lps[j-1]}')
                else:
                    print(f" Mismatch at start of pattern, advance text pointer")
                    i += 1

        print(f"Total comparisons: {comparisons}")
        print(f"Matches found at positions: {matches}")
        return matches



if __name__ == '__main__':
    text = "ABABCABABA"
    pattern = "ABABA"

    kmp_algorithm = KMPAlgorithm()
    matches = kmp_algorithm.kmp_search(text, pattern)
    print(matches)
