p_input = []
string = '[3,5,7,9] [1,2,3,4,5]'
input = string.split(' ')
for i in input:
    tmp = i[1:len(i)-1]
    p_input.append(tmp.split(','))
for l in p_input:
    for i in range(0, len(l)):
        l[i] = int(l[i])
print(p_input)
