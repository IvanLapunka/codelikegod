import math

class Solution:
    def compress(self, chars):
        count = 0
        curr = chars[0]
        first = 0
        start = 0
        for i in range(len(chars)):
            if chars[i] == curr:
                count += 1
            elif count > 1:
                buf = count
                chars[start] = chars[first]
                while count > 0:
                    order = 1 + start + math.floor(math.log10(count))
                    chars[order] = str(count % 10)
                    count //= 10
                start += 2 + math.floor(math.log10(buf))
                curr = chars[i]
                count = 1
                first = i
            else:
                chars[start] = chars[first]
                start += 1
                curr = chars[i]
                count = 1
                first = i
        else:
            if count > 1:
                buf = count
                chars[start] = chars[first]
                while count > 0:
                    order = 1 + start + math.floor(math.log10(count))
                    chars[order] = str(count % 10)
                    count //= 10
                start += 2 + math.floor(math.log10(buf))
            else:
                chars[start] = chars[first]
                start += 1
        return start