a = {6, 7, 8, 9, 10}
b = {5, 6, 7, 8, 9}
a.add(4)
print(a)
b.add(3)
print(b)
lst = [11, 100, 99, 1000, 999, 99]
lst.insert(0,-1)
print(lst)
print(lst[1])
print(lst[6])
print(lst.count(99))
y=0
for num in lst:
      y+=num
print(y)
print(min(lst))
p=range(2020,2070)
for year in p:
      if year%4==0:
        print(year)
nums=range(1000,2000)
for num in nums:
      if num%7==0 & num%5 !=0:
          print(num)
numbers=range(1,11)
for num in numbers:
    print(num)
numbers=range(30,50)
for num in numbers:
    if num%2!=0:
         print(num)
x=[]
nums=range(100,200)
for num in nums:
    if num%7==0:
        x.append(num)
print(x)
numbers=range(1,50)
for num in numbers:
    if num%3==0 & num%5==0:
        print("purpleWhite")
    elif num%3==0:
         print("Purple")
    elif num %5==0:
          print("white")