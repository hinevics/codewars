import re


def travel(r: str, zipcode: str):
    # findall = {i.group('index') for i in map(lambda x: re.match(pattern=r'(?P<number>\d+) (?P<text>[A-Za-z\.\,\s]+?) (?P<index>[A-Z]{2} \d{5})',string=x), r.split(','))}
    match_dict = dict()
    for i in r.split(','):
        match = re.match(pattern=r'(?P<number>\d+) (?P<text>[A-Za-z\.\,\s]+?) (?P<index>[A-Z]{2} \d{5})',
        string=i)
        if match.group('index') in match_dict:
            match_dict[match.group('index')].append(((match.group('number'), match.group('text'))))
        else:
            match_dict[match.group('index')] = [(match.group('number'), match.group('text'))]
    numbers = ','.join([i[0] for i in match_dict[zipcode]]) if zipcode in match_dict.keys() else ''
    texts = ','.join([i[1] for i in match_dict[zipcode]]) if zipcode in match_dict.keys() else ''
    return '{zipcode}:{text}/{number}'.format(zipcode=zipcode, text=texts, number=numbers)