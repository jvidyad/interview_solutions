#!/usr/bin/env python


def compress(s):

    char_list = list(s)
    
    temp_char = char_list.pop(0)
    cs=""
    count=1
    for i in xrange(1, len(s)):
        ch_i = char_list.pop(0)

        if(ch_i == temp_char):
            count += 1

        else:
            cs += " (%d,%s)"%(count, temp_char)
            count = 1
            temp_char = ch_i

        if(i == len(s)-1):
            cs += " (%d,%s)"%(count, temp_char)

    return cs

        
        


def main():
    print compress("abbcccddddeeeeefassdd")

if __name__ == "__main__":
    main()
