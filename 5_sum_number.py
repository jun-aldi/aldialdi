def sum_numbers(num):
    hasil=1
    for i in range(2, num+1):
        hasil += i
    return hasil

print(sum_numbers(12))