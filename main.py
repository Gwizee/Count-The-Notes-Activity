amount = int(input("Enter a Amount : "))

amount_500 = amount // 500
amount %= 500

amount_100 = amount // 100
amount %= 100

amount_50 = amount // 50
amount %= 50

amount_10 = amount // 10
amount %= 10
5
print("Notes of 500 is : ",amount_500)
print("Notes of 100 is : ",amount_100)
print("Notes of 50 is : ",amount_50)
print("Notes of 10 is : ",amount_10)