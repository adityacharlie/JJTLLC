def compress(S):
    new_s = ""
    count = 1
    i = 0
    new_s += S[0]
    while(i < len(S) - 1):
        # Check current,next char in string and increment count
        if S[i] == S[i + 1]:
            count += 1
        else:
            # once repeating of char stops add str of count to new string
            if count > 1:
                new_s += str(count)
            new_s += S[i + 1]  # Adding the next non repeated char
            count = 1
        i += 1
    # Add the last count of last char seperately
    if count > 1:
        new_s += str(count)
    return new_s

    # Since we are iterating over the list of chars of length N only once
    # the time complexity will be O(n)
    # Assigment, increment statements are linear time
    # So total time complexity would be O(n)


if __name__ == '__main__':
    compress("aaaabbbccddddddee")
