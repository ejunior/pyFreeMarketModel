import random
import csv
import matplotlib.pyplot as plt

__author__ = 'ur5f'


SIMULATION_DURATION = 800
NUM_OF_PRODUCERS = 10
NUM_OF_CONSUMERS = 10
MAX_STARTING_SUPPLY = 20
SUPPLY_INCREMENT = 80
COST = 5
MAX_ACCEPTABLE_PRICE = COST * 10
MAX_STARTING_PROFIT = 5
PRICE_INCREMENT = 1.1
PRICE_DECREMENT = 0.9


class Producer:

    supply = 0
    price = 0

    def __init__(self):
        self.supply = 0
        self.price = 0

    def generate_goods(self):
        if self.price > COST:
            self.supply += SUPPLY_INCREMENT

    def produce(self):
        if self.supply > 0:
            if self.price > COST:
                self.price *= PRICE_DECREMENT
        else:
            self.price *= PRICE_INCREMENT
            self.generate_goods()


class Consumer:
    demands = 0

    def initialize(self):
        self.demands = 0

    def buy(self):
        while self.demands > 0 and Market.supply() > 0:
            cheapest_producer = Market.cheapest_producer()

            if cheapest_producer:
                if cheapest_producer.price > MAX_ACCEPTABLE_PRICE:
                    self.demands *= 0.5
                cheapest_supply = Market.cheapest_producer().supply

                if self.demands > cheapest_supply:
                    self.demands -= cheapest_supply
                    Market.cheapest_producer().supply = 0
                else:
                    Market.cheapest_producer().supply -= self.demands
                    self.demands = 0


producers = []
for _z in range(NUM_OF_PRODUCERS):
    producer = Producer()
    producer.price = COST + random.choice(range(MAX_STARTING_PROFIT))  # rand(MAX_STARTING_PROFIT)
    producer.supply = random.choice(range(MAX_STARTING_SUPPLY))  # rand(MAX_STARTING_SUPPLY)
    producers.append(producer)

# NUM_OF_CONSUMERS.times do
consumers = [Consumer() for c in range(NUM_OF_CONSUMERS)]

# SIMULATION_DURATION.times {|n| $generated_demand << ((Math.sin(n)+2)*20).round }
#generated_demand = [round((math.sin(n)+2)*20) for n in range(SIMULATION_DURATION)]

# reading demand data
generated_demand = []
with open('foo.csv', newline='') as csvfile:
    line = csv.reader(csvfile, delimiter=',')
    for r in line:
        generated_demand.append(round(int(r[1])/10))

generated_demand += generated_demand
generated_demand += generated_demand
generated_demand += generated_demand
print(generated_demand)


class Market:
    @staticmethod
    def average_price():
        # ($producers.inject(0.0) { |memo, producer| memo + producer.price}/ $producers.size).round(2)
        return round(sum(p.price for p in producers)/producers.__len__(), 2)

    @staticmethod
    def supply():
        # $producers.inject(0) { |memo, producer| memo + producer.supply }
        return sum(p.supply for p in producers)

    @staticmethod
    def demand():
        # $consumers.inject(0) { |memo, consumer| memo + consumer.demands }
        return sum(c.demands for c in consumers)

    @staticmethod
    def cheapest_producer():
        # producers = $producers.find_all {|f| f.supply > 0}
        # producers.min_by{|f| f.price}
        return sorted([p for p in producers if p.supply > 0], key=lambda f: f.price, reverse=True).pop()

demand_supply = []
price_demand = []

price = []
supply = []
demand = []
newProducers = 0


# SIMULATION_DURATION.times do |t|
# for t in range(SIMULATION_DURATION):
for t in range(SIMULATION_DURATION):

    # progress = t/SIMULATION_DURATION
    # print("\rProgress: [{0:50s}] {1:.1f}%".format('#' * int(progress * 50), progress*100), end="", flush=True)

    # consumers.each do |consumer|
    for consumer in consumers:
        consumer.demands = generated_demand[t]

    demand_supply.append([t, Market.demand(), Market.supply()])
    supply.append(Market.supply())
    # demand_supply << [t, Market.demand, Market.supply]
    # $producers.each do |producer|
    [producer.produce() for producer in producers]

    price.append(Market.average_price())
    demand.append(Market.demand())
    price_demand.append([t, Market.average_price(), Market.demand()])

    if Market.average_price() > MAX_STARTING_PROFIT*2:
        newProducers += 1
        print("adding new producer %d " % newProducers)
        producers.append(Producer())

    while Market.demand() > 0 and Market.supply() > 0:
        # $consumers.each do |consumer|
        [consumer.buy() for consumer in consumers]


# price demand
fig, ax1 = plt.subplots(nrows=2, ncols=1)
t = range(SIMULATION_DURATION)

ax1[0].plot(t, price, 'b-')
ax1[0].set_xlabel('time (months)')
# Make the y-axis label and tick labels match the line color.
ax1[0].set_ylabel('price', color='b')
ax1[0].yaxis.grid(True)
ax1[0].xaxis.grid(True)

for tl in ax1[0].get_yticklabels():
    tl.set_color('b')

ax2 = ax1[0].twinx()
ax2.plot(t, demand, 'r-')
ax2.set_ylabel('demand', color='r')
ax2.yaxis.grid(True)

for tl in ax2.get_yticklabels():
    tl.set_color('r')

# demand supply
ax1[1].plot(t, demand, 'b-')
ax1[1].set_xlabel('time (months)')

ax1[1].set_ylabel('demand', color='b')
ax1[1].yaxis.grid(True)
for tl in ax1[1].get_yticklabels():
    tl.set_color('b')

ax3 = ax1[1].twinx()
ax3.plot(t, supply, 'r-')
ax3.set_ylabel('supply', color='r')
ax3.yaxis.grid(True)

for tl in ax3.get_yticklabels():
    tl.set_color('r')

plt.show()

#
# outputFile = open('price_demand.csv', 'w', newline='')
# outputWriter = csv.writer(outputFile)
# for r in price_demand:
#     print(r)
#     outputWriter.writerow(r)
# outputFile.close()
#
# outputFile = open('demand_supply.csv', 'w', newline='')
# outputWriter = csv.writer(outputFile)
# for r in demand_supply:
#     print(r)
#     outputWriter.writerow(r)
# outputFile.close()
