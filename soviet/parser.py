def block():
    output = ""
    with open('book.txt', 'r', encoding="utf8") as f:
        lines = f.readlines()
        for l in lines:
            l = l.strip()
            if l.isnumeric() or not l:
                continue
            if 'г.р' in l:
                output += '\n\n'
            output += ' ' + l

    with open('blocks.txt', 'w', encoding="utf8") as f:
        f.write(output)


def split():
    with open('blocks.txt', 'r', encoding="utf8") as f:
        blocks = f.read().split('\n\n')
        print(blocks[1])


split()
