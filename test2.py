from __future__ import division

def choose_iter(elements, length):
    for i in xrange(len(elements)):
        if length == 1:
            yield (elements[i],)
        else:
            for next in choose_iter(elements[i+1:len(elements)], length-1):
                yield (elements[i],) + next
def choose(l, k):
    return list(choose_iter(l, k))

def main():
    N = input()
    s = raw_input()
    K = input()

    char_list = [s[i] for i in range(0,2*N-1,2)]

    tuples_list = choose(range(1,N+1), K)

    number_with_a = 0
    number_items=0

    for item_tuple in tuples_list:
        number_items += 1

        for ind in item_tuple:
            if char_list[ind-1]=='a':
                number_with_a += 1
                break

    print number_with_a/number_items

if __name__ == "__main__":
    main()
