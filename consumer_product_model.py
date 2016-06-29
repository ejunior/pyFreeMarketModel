import functools
import math
import random
import csv

__author__ = 'ur5f'


SIMULATION_DURATION = 150
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
            if self.price >= COST:
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
                    cheapest_producer.supply = 0
                else:
                    cheapest_producer.supply -= self.demands
                    self.demands = 0


producers = []
for i in range(NUM_OF_PRODUCERS):
    producer = Producer()
    producer.price = COST + random.choice(range(MAX_STARTING_PROFIT))  # rand(MAX_STARTING_PROFIT)
    producer.supply = random.choice(range(MAX_STARTING_SUPPLY))  # rand(MAX_STARTING_SUPPLY)
    producers.append(producer)


consumers = []
# NUM_OF_CONSUMERS.times do
for i in range(NUM_OF_CONSUMERS):
    consumers.append(Consumer())

generated_demand = []
# SIMULATION_DURATION.times {|n| $generated_demand << ((Math.sin(n)+2)*20).round }
for n in range(SIMULATION_DURATION):
    generated_demand.append(round((math.sin(n)+2)*20))


class Market:
    @staticmethod
    def average_price():
        # ($producers.inject(0.0) { |memo, producer| memo + producer.price}/ $producers.size).round(2)
        return round(functools.reduce(lambda x, y: x+y.price, producers, 0)/producers.__len__(), 2)

    @staticmethod
    def supply():
        # $producers.inject(0) { |memo, producer| memo + producer.supply }
        return functools.reduce(lambda x, y: x+y.supply, producers, 0)

    @staticmethod
    def demand():
        # $consumers.inject(0) { |memo, consumer| memo + consumer.demands }
        return functools.reduce(lambda x, y: x+y.demands, consumers, 0)

    @staticmethod
    def cheapest_producer():
        # producers = $producers.find_all {|f| f.supply > 0}
        # producers.min_by{|f| f.price}
        prds = []
        for p in producers:
            if p.supply > 0:
                prds.append(p)
        prds.sort(key=lambda f: f.price, reverse=True)
        if prds:
            return prds.pop()
        else:
            return None


demand_supply = []
price_demand = []

# SIMULATION_DURATION.times do |t|
for t in range(SIMULATION_DURATION):
    print(t)
    # consumers.each do |consumer|
    for consumer in consumers:
        consumer.demands = generated_demand[t]

    demand_supply.append([t, Market.demand(), Market.supply()])
    # demand_supply << [t, Market.demand, Market.supply]
    # $producers.each do |producer|
    for producer in producers:
        producer.produce()

    price_demand.append([t, Market.average_price(), Market.demand()])

    while Market.demand() > 0 and Market.supply() > 0:
        # $consumers.each do |consumer|
        for consumer in consumers:
            consumer.buy()

outputFile = open('price_demand.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
for r in price_demand:
    print(r)
    outputWriter.writerow(r)
outputFile.close()

outputFile = open('demand_supply.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
for r in demand_supply:
    print(r)
    outputWriter.writerow(r)
outputFile.close()
