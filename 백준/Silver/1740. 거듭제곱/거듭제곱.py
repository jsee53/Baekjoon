N = int(input())

binN = bin(N)[2:N.bit_length()+3]

binN_list = list(map(int,str(binN)))

result = 0
i = 0
for bit in binN_list:
    result = result + bit * (3 ** (len(binN_list) - 1 - i))
    i = i + 1

print(result)