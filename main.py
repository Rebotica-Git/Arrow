import math
import eel


@eel.expose
def get_file(file: str):
    car_list = file.split("\n")[1:]
    for num, car in enumerate(car_list):
        car_list[num] = car.split(";")
    return analyze(car_list)


def analyze(cars_list: list[list[str]]):
    text = ''
    for car in cars_list:
        text += f"Авто {car[3]} по адресу {round(float(car[0]), 5)},{round(float(car[1]), 5)}. " \
                f"Сигнал — {'✅' if car[2] == '' else car[2] + '❌'}\n"
    text += "\n\n"

    for num, car in enumerate(cars_list):
        for scar in cars_list[num+1:]:
            text += f"Между  {car[3]}  и  {scar[3]}   — {long(car, scar)} км\n"
    text += "\n"
    return text


def long(point_A, point_B):
    point_A = list(map(float, point_A[:2]))
    point_B = list(map(float, point_B[:2]))

    AD = abs(point_A[1] - point_B[1]) * 111.3 * math.cos(point_B[0])
    BC = abs(point_A[1] - point_B[1]) * 111.3 * math.cos(point_A[0])
    AB = abs(point_A[0] - point_B[0]) * 111.1
    AH = abs(AD - BC) / 2
    BH = math.sqrt(abs(AB ** 2 - AH ** 2))
    HD = abs(AD - AH)
    BD = math.sqrt(BH ** 2 + HD ** 2)
    return round(BD, 3)


if __name__ == "__main__":
    eel.init("web")
    eel.start("main.html", size=(800, 800), mode="chrome")



















