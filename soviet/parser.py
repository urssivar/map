with open('book.txt', 'r', encoding="utf8") as f:
    items = f.read().split('\n\n')
    print(*items[:15], sep='\n\n')
