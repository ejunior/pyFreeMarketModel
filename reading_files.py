import csv

demand_price = []
with open('price_demand.csv', newline='') as csvfile:
    line = csv.reader(csvfile, delimiter=',')
    for r in line:
        demand_price.append([int(r[0]), float(r[1]), int(r[2])])
    print(demand_price)