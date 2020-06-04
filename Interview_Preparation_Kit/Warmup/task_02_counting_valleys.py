def countingValleys(n, s):
    sea_level = 0
    current_level = 0
    valley_count = 0
    for letter in s:
        if letter == 'U':
            current_level += 1
        if letter == 'D':
            current_level -= 1
        
        if current_level == sea_level and letter == 'U':
            valley_count += 1
    return valley_count
