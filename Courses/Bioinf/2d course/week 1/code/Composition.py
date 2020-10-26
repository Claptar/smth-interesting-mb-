def composition(k, text):
    'turning text in list of reads in lexicografic order'
    comp = []
    for i in range(len(text) - k + 1):
        comp.append(text[i:i + k])
    return sorted(comp)


def main():
    k = int(input())
    text = input()
    print('\n'.join(composition(k, text)))


main()
