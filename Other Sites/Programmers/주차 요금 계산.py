from math import *


def solution(fees, records):
    base_time = fees[0]
    base_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]

    car = []
    temp_time = {}
    car_time = {}
    car_in = {}
    car_isOut = {}

    car_fee = {}
    car_fee_keys = []
    ans = []

    for i in records:
        car.append(i.split(" "))

    for i in car:
        car_time[i[1]] = 0
        car_in[i[1]] = 0
        car_isOut[i[1]] = False

    for i_car in car:
        if (i_car[2] == "IN"):
            temp_time[i_car[1]] = i_car[0].split(":")
            car_in[i_car[1]] = i_car[0]
            car_isOut[i_car[1]] = False
        if (i_car[2] == "OUT"):
            out_time = i_car[0].split(":")
            time_from = int(out_time[0]) * 60 + int(out_time[1])
            time_des = int(temp_time[i_car[1]][0]) * 60 + int(temp_time[i_car[1]][1])
            hour = int(time_from) - int(time_des)

            car_time[i_car[1]] += hour
            car_isOut[i_car[1]] = True
            del temp_time[i_car[1]]

    for i in car_time.keys():
        if car_isOut[i] == False:
            time_from = 23 * 60 + 59
            time_des = int(temp_time[i][0]) * 60 + int(temp_time[i][1])
            hour = int(time_from) - int(time_des)
            car_time[i] += hour

    for i in car_time.keys():
        if car_time[i] < base_time:
            car_fee[i] = base_fee
        else:
            car_fee[i] = base_fee + (ceil((car_time[i] - base_time) / unit_time)) * unit_fee

    for i in car_fee.keys():
        car_fee_keys.append(i)
    car_fee_keys.sort()

    for i in car_fee_keys:
        ans.append(car_fee[i])

    return ans