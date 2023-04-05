months = ('January','February','March','April','May','June','July','August','September',
          'October','November','December')

profits = (125874,245879,356987,456975,523169,659743,784259,812549,945213,102365,112458,125884)
print(len(profits))

max_profits = max(profits)
print(max_profits)

min_profits = min(profits)
print(min_profits)


index1 = profits.index(max_profits)
print(months[index1])

index2 = profits.index(min_profits)
print(months[index2])