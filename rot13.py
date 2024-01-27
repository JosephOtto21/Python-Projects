a = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'],['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']]

def translator():
    text = input("Enter word: ")

    rot_text = []

    rot_13 = ''

    for l in text:
        rot_text.append(l)

    for po, wo in enumerate(rot_text):
        for i in range(13):
            if a[0][i] == wo:
                rot_text[po] = a[1][i]
            elif a[1][i] == wo:
                rot_text[po] = a[0][i]
            elif a[0][i].upper() == wo.upper():
                rot_text[po] = a[1][i].upper()
            elif a[1][i].upper() == wo.upper():
                rot_text[po] = a[0][i].upper()
            else:
                continue

    for i in rot_text:
        rot_13 += i

    print(rot_13)
    return

if __name__ == '__main__':
    translator()
