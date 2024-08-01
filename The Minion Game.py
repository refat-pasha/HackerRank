


def minion_game(string):
    vowels = 'AEIOU'
    s_len = len(string)
    k = 0
    s = 0
    for i in range(s_len):
        if string[i] in vowels:
            k+=s_len-i
        else:
            s+=s_len-i
    if k>s:
        print(f"Kevin {k}")
    elif s>k:
        print(f"Stuart {s}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)