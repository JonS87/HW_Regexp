from pprint import pprint
import re
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)

## 1. Выполните пункты 1-3 задания.
contacts_list.sort()
contacts_list_new = []
index2 = 0
pattern = r'(\+7|8)?\s*\(?(\d\d\d)\)?\s*-?(\d\d\d)-?(\d\d)-?(\d\d)\s*\(?(доб\.)?\s*(\d+)?\)?'
replace = r'+7(\2)\3-\4-\5 \6\7'
for index, row in enumerate(contacts_list):
    if index == 0:
        contacts_list_new.append(row)
        index2 += 1
    else:
        fio = ' '.join(row[:3]).strip().split()
        if len(fio) == 2:
            row[:3] = [*fio, '']
        else:
            row[:3] = fio
        if row[0] == contacts_list_new[index2-1][0] and row[1] == contacts_list_new[index2-1][1]:
            if contacts_list_new[index2-1][2] == '':
                contacts_list_new[index2-1][2] = row[2]
            if contacts_list_new[index2-1][3] == '':
                contacts_list_new[index2-1][3] = row[3]
            if contacts_list_new[index2-1][4] == '':
                contacts_list_new[index2-1][4] = row[4]
            if contacts_list_new[index2-1][5] == '':
                contacts_list_new[index2-1][5] = re.sub(pattern, replace, row[5]).strip()

            if contacts_list_new[index2-1][6] == '':
                contacts_list_new[index2-1][6] = row[6]
        else:
            contacts_list_new.append(row)
            index2 += 1
            contacts_list_new[index2-1][5] = re.sub(pattern, replace, contacts_list_new[index2-1][5]).strip()
        #print(index, row)

## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  
## Вместо contacts_list подставьте свой список:
  datawriter.writerows(contacts_list_new)