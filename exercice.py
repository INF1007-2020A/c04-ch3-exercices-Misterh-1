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
    #degs_rad = (angle_degs * math.pi) / 180
    #mins_rad = (angle_mins * math.pi) / (60*180)
    #secs_rad = (angle_secs * math.pi) / (3600*180)
    #result_rad = degs_rad + mins_rad + secs_rad
    return math.radians (angle_degs + (angle_mins + (angle_secs /60))/60)


def to_degrees(angle_rads: float) -> tuple:
    rad_deg = math.degrees(angle_rads)
    rad_mins = ()
    return rad_deg, 0.0, 0.0


def to_celsius(temperature: float) -> float:
    cels_temp = (temperature -32)/1.8
    return cels_temp


def to_farenheit(temperature: float) -> float:
    fahr_temp = (temperature*1.8) + 32
    return fahr_temp


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 180 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
