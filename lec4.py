import sys
print(sys.argv)
v1=sys.argv[1]
v2=sys.argv[2]
file_name = 'first_10.csv'
f = open(file_name)
lines = f.readlines()
for line in lines[1:]:
    columns = line.split(',')
    price = int(columns[9])
    if price >= int(v1) and price <= int(v2):
        print(line)
    testing

