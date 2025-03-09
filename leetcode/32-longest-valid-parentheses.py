def longest_valid_parentheses(s: str) -> int:
    def helper(s, start, count, max_length):
        if start >= len(s):
            return max_length
        
        if s[start] == '(':
            return max(helper(s, start + 1, count + 1, max_length), max_length)
        elif s[start] == ')' and count > 0:
            if start == len(s)-1:
                return 0
            return max(helper(s, start + 1, count - 1, max_length + 2), max_length)
        else:
            return helper(s, start + 1, 0, max_length)  # Reset on invalid ')'

    return helper(s, 0, 0, 0)

print(longest_valid_parentheses("()(()"))