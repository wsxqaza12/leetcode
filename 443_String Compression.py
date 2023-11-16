class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        letter = []
        L = 0

        if len(chars) == 1:
            return len(chars)

        while L < len(chars):
            letter.append(chars[L])
            R = L + 1
            count = 1
            while R < len(chars) and chars[L] == chars[R]:
                count += 1
                R += 1

            letter.append(count)
            L = R

        curr = 0
        i = 0
        while i < len(letter):
            if str(letter[i]).isalpha():
                chars[curr] = letter[i]
            if letter[i] > 1:
                for item in str(letter[i]):
                    chars[curr] = str(item)
                    curr += 1
            i += 1

        return curr
