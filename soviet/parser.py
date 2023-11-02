# book : г\.р -> \n$& // 8653
import re


def block():
    output = ""
    with open('book.txt', 'r', encoding="utf8") as f:
        lines = f.readlines()
        block = ''
        for l in lines:
            l = l.strip()
            if l.isnumeric() or not l:
                continue
            if 'г.р' in l:
                output += block.strip() + '\n\n'
                block = ''
            block += l + ' '

    with open('blocks.txt', 'w', encoding="utf8") as f:
        f.write(output)


def split():
    def sentence(x):
        for r, s in [('концлагерь', 'лагер'),
                     ('гулаг', 'ИТЛ'),
                     ('расстрел', 'расстрел'),
                     ('высылка', 'высылк'),
                     ('ссылка', 'ссылк'),
                     ('тюрьма', 'заключен'),
                     ('тюрьма', 'свобод')]:
            if s in x:
                return r

    with open('list.txt', 'w', encoding="utf8") as fw:
        with open('blocks.txt', 'r', encoding="utf8") as f:
            lines = f.readlines()
            for l in lines:

                try:
                    name, b_year = re.findall(
                        r'([а-яА-Я\s]*).*(\d{4}).*г\.р', l)[0]
                    # b_place = re.findall(
                    #     r'г\.р\.*,*\s*(?:уроженка|уроженец)?\s*(?:ст\.|с\.|г\.)?(.*?)\.', l)[0]
                    a_yr = re.findall(r'Арестован.*?([\.\d]+\d{4})', l)
                    s_yr = re.findall(r'Приговорен.*?([\.\d]+\d{4})', l)
                    r_yr = re.findall(r'Реабилитирован.*?([\.\d]+\d{4})', l)

                    row = [name,
                           b_year,
                           a_yr[0] if a_yr else '',
                           s_yr[0] if s_yr else '',
                           r_yr[0] if r_yr else 'ERR']

                    sent = sentence(
                        l.split('заменен')[1]
                        if 'заменен' in l
                        else l
                    )
                    row.append(sent if sent else 'ERR')

                except:
                    row = ['ERR']+['']*5

                row.append(l)
                fw.write('|'.join(row))


split()
