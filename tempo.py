from datetime import timedelta

_8_HORAS = timedelta(hours=8)

t1 = timedelta(hours=7, minutes=36)
t2 = timedelta(hours=11, minutes=32)
t3 = timedelta(hours=13, minutes=7)
t4 = timedelta(hours=21, minutes=0)

arrival = t2 - t1
lunch = (t3 - t2 - timedelta(hours=1))
departure = t4 - t3

print(arrival, lunch, departure)
print("total de horas", arrival + departure - lunch)
print("horas extras", (arrival + departure - lunch - timedelta(hours=8)))
print(timedelta(hours=30) / (arrival + departure - lunch - timedelta(hours=8)))


t1 = timedelta(hours=9, minutes=2)
t2 = timedelta(hours=11, minutes=44)
t3 = timedelta(hours=13, minutes=27)
t4 = timedelta(hours=19, minutes=00)

arrival = t2 - t1
lunch = t3 - t2 - timedelta(hours=1)
departure = t4 - t3
print()
print(arrival, lunch, departure)
print("total de horas", arrival + departure - lunch)
print("horas extras", (arrival + departure - lunch - _8_HORAS))
# print(timedelta(hours=30) / (arrival + departure - lunch - timedelta(hours=8)))


t1 = timedelta(hours=7, minutes=52)
t2 = timedelta(hours=11, minutes=46)
t3 = timedelta(hours=13, minutes=2)
t4 = timedelta(hours=20, minutes=50)

arrival = t2 - t1
lunch = t3 - t2 - timedelta(hours=1)
departure = t4 - t3
print()
print(arrival, lunch, departure)
print("total de horas", arrival + departure - lunch)
print("horas extras", (arrival + departure - lunch - _8_HORAS))
# print(timedelta(hours=30) / (arrival + departure - lunch - timedelta(hours=8)))

print(timedelta(hours=21, minutes=00) - timedelta(hours=9, minutes=0) - _8_HORAS)


# ta = timedelta(hours=9, minutes=27) - timedelta(hours=9, minutes=18)
ta = timedelta(hours=12, minutes=2) - timedelta(hours=9, minutes=18)
tb = timedelta(hours=12, minutes=2) - timedelta(hours=11, minutes=24)
tc = timedelta(hours=19, minutes=0) - timedelta(hours=12, minutes=53)

print("[dia 12: ", ta + tb + tc, "], [horas extras", ta + tb + tc - _8_HORAS, "]", sep="")


x = [(8, 10), {8, 10}]
print(x, type(x), type(x[0]), type(x[1]))

import sys
from PyQt5.QtWidgets import QApplication, QWidget


def main():

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
