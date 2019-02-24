"""
    Napisz funkcję, która wyświetli najkrótszy znakowo zakres czasu na podstawie dwóch danych stringów

"""
import re

begin = '2019-03-03 16:00'
end = '2019-02-03 16:45+03'

def dateRange(date1: str, date2: str):
    pattern = re.compile(r'\d{4}(-\d{2}){2} \d{2}:\d{2}')

    if pattern.match(begin) and pattern.match(end):

        cut_zero = lambda x: x[:13] + x[16:] if x[14:16] == '00' else x

        if date1 > date2:
            prep_date1 = cut_zero(date2)
            prep_date2 = cut_zero(date1)
        else:
            prep_date1 = cut_zero(date1)
            prep_date2 = cut_zero(date2)

        for item in [10, 7, 4]:
            if date1[:item] == date2[:item]:
                return prep_date1[:item] + ': ' + prep_date1[item+1:] + ', '+ prep_date2[item+1:]

        return prep_date1 + ', ' + prep_date2
    else:
        return 'Invalid input string'


print(dateRange(begin,end))

