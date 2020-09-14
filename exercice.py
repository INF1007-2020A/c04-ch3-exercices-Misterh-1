#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    a = math.sqrt(a)
    return a


def square(a: float) -> float:
    a = a**2
    return a


def average(a: float, b: float, c: float) -> float:
    result = (a + b + c)/3
    return result


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    degs_rad = (angle_degs * math.pi) / 180
    mins_rad = (angle_mins * math.pi) / (60*180)
    secs_rad = (angle_secs * math.pi) / (3600*180)
    result_rad = degs_rad + mins_rad + secs_rad
    return result_rad


def to_degrees(angle_rads: float) -> tuple:
    rad_deg = (60*180*angle_rads)
    return 0.0, 0.0, 0.0


def to_celsius(temperature: float) -> float:
    return 0.0


def to_farenheit(temperature: float) -> float:
    return 0.0


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(100, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
