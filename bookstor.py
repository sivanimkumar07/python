header="""\t bookstore receipt
\t----"""

book1="python basics"
book2="data science intro"

price1=450
price2=600

value1="\t book:{} \t price:{}/-".format(book1,price1)
value2="\t book:{} \t price:{}/-".format(book2,price2)

total=price1+price2
total1="\t total amount:{}".format(total)

message="\n\t thank you visit again!"
receipt = header + "\n" + value1 + "\n" + value2 + "\n" + total1 + message
print(receipt.upper())
