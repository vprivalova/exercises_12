class Date:
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = [0, 'янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']

    def __init__(self, date):
        if len(date) == 10:
            if (int(date[6:]) % 4 != 0 and 0 < int(date[3:5]) < 13 and 0 < int(date[0:2]) <= Date.days[int(date[3:5])] and
                    0 < int(date[6:]) < 2024):
                self._date = date

            elif (int(date[3:5]) == 2 and int(date[6:]) % 4 == 0 and
                  0 < int(date[0:2]) <= Date.days[int(date[3:5])] + 1 and 0 < int(date[6:]) < 2024):
                self._date = date

            else:
                print('ошибка')
                self._date = None

    def __repr__(self):
        return str(self._date)

    @property
    def date(self):
        if self._date is not None:
            return f'{int(self._date[0:2])} {Date.months[int(self._date[3:5])]} {self._date[6:]} г.'
        else:
            return self._date

    @date.setter
    def date(self, date):
        if len(date) == 10:
            if (int(date[6:]) % 4 != 0 and 0 < int(date[3:5]) < 13 and 0 < int(date[0:2]) <= Date.days[
                int(date[3:5])] and
                    0 < int(date[6:]) < 2024):
                self._date = date

            elif (int(date[3:5]) == 2 and int(date[6:]) % 4 == 0 and
                  0 < int(date[0:2]) <= Date.days[int(date[3:5])] + 1 and 0 < int(date[6:]) < 2024):
                self._date = date

            else:
                print('ошибка')
                self._date = None

    def to_timestamp(self):
        seconds = 0
        year = int(self._date[6:])
        month = int(self._date[3:5])
        day = int(self._date[0:2])
        seconds += (year - 1970) * 365 * 24 * 60 * 60

        for y in range(1970, year + 1):
            if y % 4 == 0:
                seconds += (24 * 60 * 60)

        for m in range(1, month):
            seconds += Date.days[m] * 24 * 60 * 60

        seconds += (day - 1) * 24 * 60 * 60
        return seconds

    def __lt__(self, other):
        first = self.to_timestamp()
        second = other.to_timestamp()
        return first < second

    def __le__(self, other):
        first = self.to_timestamp()
        second = other.to_timestamp()
        return first <= second

    def __eq__(self, other):
        first = self.to_timestamp()
        second = other.to_timestamp()
        return first == second

    def __ne__(self, other):
        first = self.to_timestamp()
        second = other.to_timestamp()
        return first != second

    def __gt__(self, other):
        first = self.to_timestamp()
        second = other.to_timestamp()
        return first > second

    def __ge__(self, other):
        first = self.to_timestamp()
        second = other.to_timestamp()
        return first >= second


d1 = Date('07.12.2021')
print(d1.date)
d1.date = '14.02.2022'
print(d1.date)
print(d1.to_timestamp())
d2 = Date('32.14.2020')
print(d2.date)
d2.date = '29.02.2021'
print(d2)
d2.date = '29.02.2020'
print(d2.date)
if d1 < d2:
    print('YES')
else:
    print('NO')
print(d1 >= d2)
print(d1 != Date('01.01.2023'))
print(d1 <= d2)
