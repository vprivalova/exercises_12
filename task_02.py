class AirTicket:
    def __init__(self, passenger_name, _from, to, date_time, flight, seat, _class, gate):
        self.passenger_name = passenger_name
        self._from = _from
        self.to = to
        self.date_time = date_time
        self.flight = flight
        self.seat = seat
        self._class = _class
        self.gate = gate

    def __repr__(self):
        return (f'|{self.passenger_name}{" " * (16-len(self.passenger_name))}|{self._from} |{self.to}|{self.date_time}'
                f'|{self.flight}{" " * (20-len(self.flight))}|{self.seat}{" " * (4-len(self.seat))}|{self._class}  '
                f'|{self.gate}{" " * (4-len(self.gate))}|')


class Load:
    data = []

    @classmethod
    def write(cls, file):
        with open(file, 'r') as f:
            line1 = f.readline()
            for elem in f:
                ticket = AirTicket(*(elem.split(';')[:-1]))
                cls.data.append(ticket)


tickets = Load.write('tickets.txt')
print('-' * 79)
print('|     NAME       |FROM|TO |   DATE/TIME    |       FLIGHT       |SEAT|CLS|GATE|')
print('=' * 79)
for item in Load.data:
    print(item)
print('-' * 79)
