import os


class CarBase:
    def __init__(self, car_type, photo_file_name, brand, carrying):
        self.car_type = car_type
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)


class Truck(CarBase):
    def __init__(self, car_type, photo_file_name, brand, carrying, body_whl):
        super().__init__(car_type, photo_file_name, brand, carrying)
        body_whl = body_whl.split('x')
        if all(x.isdigit() for x in body_whl) and all(float(x) > 0 for x in body_whl):
            self.body_length, self.body_width, self.body_height = map(float, body_whl)
        else:
            self.body_length, self.body_width, self.body_height = 0, 0, 0

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class Car(CarBase):
    def __init__(self, car_type, photo_file_name, brand, carrying, passenger_seats_count):
        super().__init__(car_type, photo_file_name, brand, carrying)
        self.passenger_seats_count = passenger_seats_count


class SpecMachine(CarBase):
    def __init__(self, car_type, photo_file_name, brand, carrying, extra):
        super().__init__(car_type, photo_file_name, brand, carrying)
        self.extra = extra
