def lexicographically_largest_string(s):
    s_list = list(map(int, list(s)))

    i = 0
    while i < len(s_list) - 1:
        if s_list[i] < s_list[i + 1]:
            s_list[i] = s_list[i + 1]
            del s_list[i + 1]
            i = max(0, i - 1)
        else:
            i += 1

    result = ''.join(map(str, s_list))
    return result

# Test cases
print(lexicographically_largest_string("1119812"))  # Output: "3992"
print(lexicographically_largest_string("226228"))   # Output: "8828"
