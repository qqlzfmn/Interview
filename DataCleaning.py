file = open('Data.txt', 'r')
lines = file.readlines()
file.close()

dic_num = {}
dic_str = {}
dic_null = {}

for line in lines:
    key = line.split(':')[0]
    value = line.split(':')[1]
    try:
        value = int(value)
        dic_num[int(key)] = value
    except ValueError:
        try:
            value = str(value.split("'")[1])
            dic_str[int(key)] = value
        except IndexError:
            dic_null[int(key)] = value

sorted_num = sorted(dic_num.items(), key=lambda x: x[1])
file_num = open('Num.txt', 'w')
for num in sorted_num:
    file_num.write('%s:%s\n' % (num[0], num[1]))
file_num.close()

sorted_str = sorted(dic_str.items(), key=lambda x: x[1])
file_str = open('String.txt', 'w')
for string in sorted_str:
    file_str.write('%s:%s\n' % (string[0], string[1]))
file_str.close()

sorted_null = sorted(dic_null.items(), key=lambda x: x[1])
file_null = open('Null.txt', 'w')
for null in sorted_null:
    file_null.write('%s:%s' % (null[0], null[1]))
file_null.close()
