class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Create a dict to store arrays of anagrams
        anagramGroups = {}

        # Loop over the anagrams
        for i in range(len(strs)):
            currWord = strs[i]
            # Sort the word alphabetically
            sortedWord = ''.join(sorted(currWord))

            # If the word is not in the dict, make its own key
            if sortedWord not in anagramGroups:
                anagramGroups[sortedWord] = [currWord]

            # Else append to the current
            else:
                anagramGroups[sortedWord].append(currWord)

        # Loop over dict key arrays and append to anagrams array
        anagrams = []
        for key in anagramGroups:
            anagrams.append(anagramGroups[key])

        return anagrams
