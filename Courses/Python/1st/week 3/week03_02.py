import os


def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


class CarBase:
    def __init__(self, photo_file_name, brand, carrying):
        self.car_type = None
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Truck(CarBase):
    def __init__(self, brand, photo_file_name,  carrying, body_whl):
        super().__init__(photo_file_name, brand, carrying)
        self.car_type = 'truck'
        body_whl = body_whl.split('x')
        if all(is_digit(x) for x in body_whl) and all(float(x) > 0 for x in body_whl):
            self.body_length, self.body_width, self.body_height = map(float, body_whl)
        else:
            self.body_length, self.body_width, self.body_height = 0, 0, 0

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(photo_file_name, brand, carrying)
        self.passenger_seats_count = passenger_seats_count
        self.car_type = 'car'


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(photo_file_name, brand, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines[1:]:
        line = line.strip().split(';')
        if len(line) < 7 or os.path.splitext(line[3])[1] == '':
            continue
        elif line[0] == 'car':
            del line[6], line[4], line[0]
            if '' not in line and all(is_digit(x) for x in [line[1], line[3]]):
                car_list.append(Car(line[0], line[2], line[1], line[3]))
            else:
                continue
        elif line[0] == 'truck':
            del line[6], line[2], line[0]
            if '' not in line[:2] and is_digit(line[3]):
                car_list.append(Truck(line[0], line[1], line[3], line[2]))
        elif line[0] == 'spec_machine':
            del line[4], line[2], line[0]
            if all(x != '' for x in line[0:2] + [line[3]]) and is_digit(line[2]):
                car_list.append(SpecMachine(line[0], line[1], line[2], line[3]))
    return car_list


for x in get_car_list('coursera_week3_cars.csv'):
    print(f'car_type = {x.car_type}, brand = {x.brand}')
