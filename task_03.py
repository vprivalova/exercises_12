class Date:
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = [0, 'янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']

    def __init__(self, date):
        if len(date) == 10:
            if (0 < int(date[3:5]) < 13 and int(date[0:2]) != 2 and 0 < int(date[0:2]) <= Date.days[int(date[3:5])]
                    and 0 < int(date[6:]) < 2024):
                self.date = date

            elif (int(date[3:5]) == 2 and int(date[6:]) % 4 == 0 and 0 < int(date[0:2]) <= Date.days[int(date[3:5])] + 1
                  and 0 < int(date[6:]) < 2024):
                self.date = date

            else:
                print('ошибка')
                self.date = None
        else:
            print('ошибка')
            self.date = None

    def __repr__(self):
        return f'{int(self.date[0:2])} {Date.months[int(self.date[3:5])]} {self.date[6:]} г.'

    def to_timestamp(self):
        seconds = 0
        year = int(self.date[6:])
        month = int(self.date[3:5])
        day = int(self.date[0:2])
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


class Meeting:
    lst_meeting = []

    def __init__(self, id, dates, title):
        self.id = id
        self.dates = Date(dates)
        self.title = title
        self.employees = []

    def __repr__(self):
        visitors = '\n'.join(self.employees)

        return f"""Рабочая встреча {self.id} 
{self.dates} {self.title} 
{visitors}\n"""

    def add_person(self, person):
        self.employees.append(str(User.users[int(person) - 1]))

    @classmethod
    def total(cls):
        number = 0
        for elem in cls.lst_meeting:
            number += len(elem.employees)
        return number

    @classmethod
    def count_meeting(cls, date):
        meetings_per_day = 0
        for elem in cls.lst_meeting:
            if elem.dates == date:
                meetings_per_day += 1
        return meetings_per_day


class User:
    users = []

    def __init__(self, id, nick_name, first_name, last_name=None, middle_name=None, gender=None):
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender
        User.users.append(self)

    def __repr__(self):
        result = (f"ID: {self.id} LOGIN: {self.nick_name} NAME: {self.first_name} {self.middle_name} {self.last_name} "
                  f"{'GENDER: ' * len(self.gender)}{self.gender}")
        return ' '.join(result.split())


class Load:
    @staticmethod
    def write(meeting_file, pers_file, attendance_file):

        with open(pers_file, 'r', encoding='utf-8') as pf:
            line1_p = pf.readline()
            for elem in pf:
                p_option = User(*(elem.split(';')[:-1]))

        with open(meeting_file, 'r', encoding='utf-8') as mf, open(attendance_file, 'r', encoding='utf-8') as af:
            line1_m = mf.readline()
            attendance = af.readlines()[1:]
            for elem in mf:
                m_option = Meeting(*(elem.split(';')[:-1]))
                Meeting.lst_meeting.append(m_option)
                for pers in attendance:
                    if pers[0] == m_option.id:
                        m_option.add_person(pers[2])


Load.write('meetings.txt', 'persons.txt', 'pers_meetings.txt')
print()
for item in Meeting.lst_meeting:
    print(item)
print(Meeting.total())
print(Meeting.count_meeting(Date('21.04.2020')))
