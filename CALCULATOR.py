import sqlite3
import time
import os
import math

#terminal func
def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def loading(str):
    print(f"{str}", end='')
    time.sleep(0.3)
    print(".", end="")
    time.sleep(0.3)
    print(".", end="")
    time.sleep(0.3)
    print(".", end='\r')
    print(f"{str}", end="")
    time.sleep(0.3)
    print(".", end="")
    time.sleep(0.3)
    print(".", end="")
    time.sleep(0.3)
    print(".", end="\r")
    time.sleep(0.5)
    clear_terminal()


#================================================================

# calculator part
def redable_number(last_result):
    if isinstance(last_result, float):
        int_part, dec_part = str(last_result).split('.')
        int_part_with_commas = "{:,}".format(int(int_part))
        formatted = f"{int_part_with_commas}.{dec_part}"
        return (formatted)


def delete_zero1(entered_number):
    if "." in entered_number:
        changed_list = entered_number.split(".")
        if changed_list[1] == "0":
            return changed_list[0]
        else:
            return entered_number


def delete_zero2(entered_number):
    changed_list = str(entered_number).split(".")
    if changed_list[1] == "0":
        return changed_list[0]
    else:
        return entered_number


def entery():
    bool_value_1 = 1
    bool_value_2 = 1
    while bool_value_1:
        try:
            num_1 = float(input("enter your first number: "))
            bool_value_1 = 0
        except Exception as err:
            print(err)
            print("\nyour entery is incorrect enter again")
    while bool_value_2:
        try:
            num_2 = float(input("enter your second number: "))
            bool_value_2 = 0
        except Exception as err:
            print(err)
            print("\nyour entery is incorrect enter again")
    return [num_1, num_2]


def sum():
    clear_terminal()
    entery_list = entery()
    result = (
        f'{delete_zero2(entery_list[0])} + {delete_zero2(entery_list[1])} ='
        f' {delete_zero1(redable_number((entery_list[0]) + (entery_list[1])))}')
    add_operation_to_history(result)
    print(f"\033[1m   {result} \033[0m")


def sub():
    clear_terminal()
    entery_list = entery()
    result = (
        f'{delete_zero2(entery_list[0])} - {delete_zero2(entery_list[1])} = {delete_zero1(redable_number((entery_list[0]) - (entery_list[1])))}')
    add_operation_to_history(result)
    print(f"\033[1m   {result} \033[0m")


def multiply():
    clear_terminal()
    entery_list = entery()
    result = (
        f'{delete_zero2(entery_list[0])} x {delete_zero2(entery_list[1])} = {delete_zero1(redable_number((entery_list[0]) * (entery_list[1])))}')
    add_operation_to_history(result)
    print(f"\033[1m   {result} \033[0m")


def devide():
    clear_terminal()
    entery_list = entery()
    result = (
        f'{delete_zero2(entery_list[0])} / {delete_zero2(entery_list[1])} = {delete_zero1(redable_number((entery_list[0]) / (entery_list[1])))}')
    add_operation_to_history(result)
    print(f"\033[1m   {result} \033[0m")


def pow():
    clear_terminal()
    entery_list = entery()
    result = (
        f'{delete_zero2(entery_list[0])} ** {delete_zero2(entery_list[1])} = {delete_zero1(redable_number(((entery_list[0]) ** (entery_list[1]))))}')
    add_operation_to_history(result)
    print(f"\033[1m   {result} \033[0m")


def radical():
    clear_terminal()
    num_1 = float(input("enter your number: "))
    result = (
        f'radical {delete_zero2(num_1)} = {delete_zero1(redable_number(num_1 ** 0.5))}')
    add_operation_to_history(result)
    print(f"\033[1m   {result} \033[0m")


#===================================================================

#length
def length(given_parameter, value):
    if given_parameter == "cm":
        m = value /100
        mm = value * 10
        km = value / 100000
        print(f"convert to meter: {m}\nconvert to millimeter: {mm}\nconvert to kilometer: {km}")
    elif given_parameter == "m":
        cm = value * 100
        mm = value * 1000
        km = value / 1000
        print(f"convert to centimeter: {cm}\nconvert to millimeter: {mm}\nconvert to kilometer: {km}")
    elif given_parameter == "mm":
        m = value / 1000
        cm = value / 10
        km = value / 1000000
        print(f"convert to centimeter: {cm}\nconvert to meter: {m}\nconvert to kilometer: {km}")
    elif given_parameter == "km":
        m = value*1000
        cm = value*100000
        mm = value*1000000
        mile = value / 1.60934
        print(f"convert to centimeter: {cm}\nconvert to meter: {m}\nconvert to millimeter: {mm}\nconvert to mile: {mile}")
    elif given_parameter == "mile":
        km = value * 1.60934
        print(f"convert to kilometer: {km}")


#===================================================================

#bmi
def height_chek(given_height):
    string = str(given_height)
    if string.split(".")[1] == "0":
        return 1
    elif string.split(".")[1] != "0":
        return 2


def calculate_bmi() :
    value = 1
    while value:
        try:
            weight = float(input("enter your weight: "))
            if weight < 20:
                print("your entry is not regular")
            else:
                value = 0
        except Exception as e:
            print("your entry is wrong")
    value2 = 1
    while value2:
        try:
            toocken_height = float(input("enter your height: "))
            result_1 = height_chek(toocken_height)
            if result_1 == 1:
                if toocken_height < 80:
                    print("your entry is not regular")
                else:
                    height = toocken_height / 100
                    value2 = 0
            elif result_1 == 2:
                if toocken_height < 0.8:
                    print("your entry is not regular")
                else:
                    height = toocken_height
                    value2 = 0
        except Exception as e:
            print("your entry is wrong")
    bmi = weight / (height ** 2)
    rounded = round(bmi, 2)
    print(rounded)
    if bmi < 18.5:
        print("underweight")

    elif 18.5 <= bmi < 25:
        print("normal")

    elif 25 <= bmi < 30:
        print("overweight")

    elif 30 <= bmi < 35:
        print("large")

    elif 35 <= bmi < 40:
        print("fat")

    elif 40 <= bmi < 45:
        print("fat")

    elif 45 <= bmi < 50:
       print("pot bellied")

    elif 50 <= bmi < 100:
        print("obese")


# ===================================================================

# area functions
def area_of_square():
    while 1:
        try:
            side = float(input("Please enter the size of the square: "))
            if side <= 0:
                print("Please enter a positive number :)")
                continue
            break
        except ValueError:
            print("Please enter a valid number :)")

    area = side * side
    print(f"The area of the square is: {area}")
    area_to_add = f"Area:{area}"
    data_to_add = f"Side:{side}"
    add_to_a_history("Square", area_to_add, data_to_add)


def area_of_rectangle():
    while 1:
        try:
            length = float(input("Please enter the length of the rectangle: "))
            if length <= 0:
                print("Please enter a positive number :)")
                continue
            break
        except ValueError:
            print("Please enter a valid number :)")

    while 1:
        try:
            width = float(input("Please enter the width of the rectangle: "))
            if width <= 0:
                print("Please enter a positive number :)")
                continue
            break
        except ValueError:
            print("Please enter a valid number :)")

    area = length * width
    print(f"The area of the rectangle is: {area}")
    area_to_add = f"Area: {area}"
    data_to_add = (f"Length:{length}\nWidth:{width}")
    add_to_a_history("Rectangle", area_to_add, data_to_add)


def area_of_triangle():
    while 1:
        try:
            height = float(input("Please enter the height of the triangle: "))
            if height <= 0:
                print("Please enter a positive number :)")
                continue
            break
        except ValueError:
            print("Please enter a valid number :)")

    while 1:
        try:
            base = float(input("Please enter the base of the triangle: "))
            if base <= 0:
                print("Please enter a number value :)")
                continue
            break
        except ValueError:
            print("Please enter a valid number :)")

    area = (base * height) / 2
    print(f"The area of your triangle is {area}")
    area_to_add = f"Area:{area}"
    data_to_add = (f"Base:{base}\nHeight:{height}")
    add_to_a_history("Triangle", area_to_add, data_to_add)


def area_of_rhomboid():
    while 1:
        try:
            large_diameter = float(input("Please enter the large diameter of the rhomboid: "))
            if large_diameter <= 0:
                print("Please enter a positive value :)")
                continue
            break
        except ValueError:
            print("Please enter a valid value :)")

    while 1:
        try:
            small_diameter = float(input("Please enter the small diameter of the rhomboid: "))
            if small_diameter <= 0:
                print("Please enter a positive value :)")
                continue
            break
        except ValueError:
            print("Please enter a valid value :)")

    area = (large_diameter * small_diameter) / 2
    print(f"The area of your rhomboid is {area}")
    area_to_add = f"Area:{area}"
    data_to_add = (f"Large diameter:{large_diameter}\nSmall diameter:{small_diameter}")
    add_to_a_history("Rhomboid", area_to_add, data_to_add)


def area_of_parallelogram():
    while 1:
        try:
            height = float(input("Please enter the height of the parallelogram: "))
            if height <= 0:
                print("Please enter a positive value :)")
                continue
            break
        except ValueError:
            print("Please enter a valid value :)")

    while 1:
        try:
            base = float(input("Please enter the base of the parallelogram: "))
            if base <= 0:
                print("Please enter a positive value :)")
                continue
            break
        except ValueError:
            print("Please enter a valid value :)")

    area = height * base
    print(f"The area of your parallelogram is {area}")
    area_to_add = f"Area: {area}"
    data_to_add = (f"Height:{height}\nBase:{base}")
    add_to_a_history("Parallelogram", area_to_add, data_to_add)


def area_of_trapezium():
    while 1:
        try:
            large_base = float(input("Please enter the large base of the trapezium: "))
            if large_base <= 0:
                print("Please enter a positive value :)")
                continue
            break
        except ValueError:
            print("Please enter a valid value :)")

    while 1:
        try:
            small_base = float(input("Please enter the small base of the trapezium: "))
            if small_base <= 0:
                print("Please enter a positive value :)")
                continue
            break
        except ValueError:
            print("Please enter a valid value :)")

    while 1:
        try:
            height = float(input("Please enter the height of the trapezium: "))
            if height <= 0:
                print("Please enter a positive value :)")
                continue
            break
        except ValueError:
            print("Please enter a valid value :)")

    area = (large_base + small_base) * height / 2
    print(f"The area of your trapezium is {area}")
    area_to_add = f"Area:{area}"
    data_to_add = (f"Large base:{large_base}\nSmall base:{small_base}\nHeight:{height}")
    add_to_a_history("Trapezium", area_to_add, data_to_add)


def area_of_circle():
    while 1:
        try:
            radius = float(input("Please enter the radius of the circle: "))
            if radius <= 0:
                print("Please enter a positive value :)")
                continue
            break
        except ValueError:
            print("Please enter a valid value :)")

    area = radius * radius * 3.14
    print(f"The area of your circle is {area}")
    area_to_add = f"Area:{area}"
    data_to_add = f"Radius:{radius}"
    add_to_a_history("Circle", area_to_add, data_to_add)


#====================================================================

# perimeter functions
def perimeter_of_square():
    while 1:
        try:
            side = float(input("Please enter the size of the square: "))
            if side <= 0:
                print("Please enter a positive number :)")
                continue
            break
        except ValueError:
            print("Please enter a valid number :)")

    perimeter = side * 4
    print(f"The perimeter of the square is: {perimeter}")
    data_to_add = f"Side:{side}"
    perimeter_to_add = f"Perimeter:{perimeter}"
    add_to_p_history("Square", perimeter_to_add, data_to_add)


def perimeter_of_rectangle():
    while 1:
        try:
            length = float(input("Please enter the length of the rectangle: "))
            if length <= 0:
                print("Please enter a positive number :)")
                continue
            break
        except ValueError:
            print("Please enter a valid number :)")

    while 1:
        try:
            width = float(input("Please enter the width of the rectangle: "))
            if width <= 0:
                print("Please enter a positive number :)")
                continue
            break
        except ValueError:
            print("Please enter a valid number :)")

    perimeter = 2 * (length + width)
    print(f"The perimeter of the rectangle is: {perimeter}")
    perimeter_to_add = f"Perimeter:{perimeter}"
    data_to_add = (f"Length:{length}\nWidth:{width}")
    add_to_p_history("Rectangle", perimeter_to_add, data_to_add)


def perimeter_of_triangle():
    while 1:
        try:
            side_1 = float(input("Please enter the first side of the triangle: "))
            if side_1 <= 0:
                print("Please enter a positive number :)")
                continue
            break
        except ValueError:
            print("Please enter a valid number :)")
    while 1:
        try:
            side_2 = float(input("Please enter the second side of the triangle: "))
            if side_2 <= 0:
                print("Please enter a positive number :)")
                continue
            break
        except ValueError:
            print("Please enter a valid number :)")

    while 1:
        try:
            side_3 = float(input("Please enter the third side of the triangle (base): "))
            if side_3 <= 0:
                print("Please enter a positive number :)")
                continue
            break
        except ValueError:
            print("Please enter a valid number :)")

    perimeter = side_1 + side_2 + side_3
    print(f"The perimeter of your triangle is {perimeter}")
    perimeter_to_add = f"Perimeter:{perimeter}"
    data_to_add = (f"Side_1:{side_1}\nSide_2:{side_2}\nSide_3:{side_3} ")
    add_to_p_history("Triangle", perimeter_to_add, data_to_add)


def perimeter_of_rhomboid():
    while 1:
        try:
            sides = float(input("Please enter the size of the sides of the rhomboid: "))
            if sides <= 0:
                print("Please enter a positive value :)")
                continue
            break
        except ValueError:
            print("Please enter a valid value :)")

    perimeter = sides * 4
    print(f"The perimeter of your rhomboid is {perimeter}")
    perimeter_to_add = f"Perimeter:{perimeter}"
    data_to_add = (f"Sides:{sides}")
    add_to_p_history("Rhomboid", perimeter_to_add, data_to_add)


def perimeter_of_parallelogram():
    while 1:
        try:
            side_1 = float(input("Please enter the first side of the parallelogram: "))
            if side_1 <= 0:
                print("Please enter a positive value :)")
                continue
            break
        except ValueError:
            print("Please enter a valid value :)")

    while 1:
        try:
            side_2 = float(input("Please enter the second side of the parallelogram: "))
            if side_2 <= 0:
                print("Please enter a positive value :)")
                continue
            break
        except ValueError:
            print("Please enter a valid value :)")

    while 1:
        try:
            side_3 = float(input("Please enter the third side of the parallelogram: "))
            if side_3 <= 0:
                print("Please enter a positive value :)")
                continue
            break
        except ValueError:
            print("Please enter a valid value :)")

    while 1:
        try:
            side_4 = base = float(input("Please enter the base of the parallelogram: "))
            if side_4 <= 0:
                print("Please enter a positive value :)")
                continue
            break
        except ValueError:
            print("Please enter a valid value :)")

    perimeter = side_1 + side_2 + side_3 + side_4
    print(f"The perimeter of your parallelogram is {perimeter}")
    perimeter_to_add = f"Perimeter:{perimeter}"
    data_to_add = (f"Side-1:{side_1}\nSide-2:{side_2}\nSide-3:{side_3}\nSide-4:{side_4} ")
    add_to_p_history("Parallelogram", perimeter_to_add, data_to_add)


def perimeter_of_trapezium():
    while 1:
        try:
            side_1 = float(input("Please enter the first side of the trapezium: "))
            if side_1 <= 0:
                print("Please enter a positive value :)")
                continue
            break
        except ValueError:
            print("Please enter a valid value :)")

    while 1:
        try:
            side_2 = float(input("Please enter the second side of the trapezium: "))
            if side_2 <= 0:
                print("Please enter a positive value :)")
                continue
            break
        except ValueError:
            print("Please enter a valid value :)")

    while 1:
        try:
            side_3 = float(input("Please enter the third side of the trapezium: "))
            if side_3 <= 0:
                print("Please enter a positive value :)")
                continue
            break
        except ValueError:
            print("Please enter a valid value :)")

    while 1:
        try:
            side_4 = float(input("Please enter the base of the trapezium: "))
            if side_4 <= 0:
                print("Please enter a positive value :)")
                continue
            break
        except ValueError:
            print("Please enter a valid value :)")

    perimeter = side_1 + side_2 + side_3 + side_4
    print(f"The perimeter of your trapezium is {perimeter}")
    perimeter_to_add = f"Perimeter:{perimeter}"
    data_to_add = (f"Side-1:{side_1}\nSide-2:{side_2}\nSide-3:{side_3}\nSide-4:{side_4}")
    add_to_p_history("Trapezium", perimeter_to_add, data_to_add)


def perimeter_of_circle():
    while 1:
        try:
            radius = float(input("Please enter the radius of the circle: "))
            if radius <= 0:
                print("Please enter a positive value :)")
                continue
            break
        except ValueError:
            print("Please enter a valid value :)")
    diameter = radius + radius
    perimeter = diameter * 3.14
    print(f"The perimeter of your circle is {perimeter}")
    perimeter_to_add = f"Perimeter:{perimeter}"
    data_to_add = f"Diameter:{diameter}"
    add_to_p_history("Circle", perimeter_to_add, data_to_add)


#====================================================================

# volume menu
def volume_of_cube():  # مکعب
    while 1:
        try:
            side = float(input("Enter the side of the cube: "))
            if side <= 0:
                print("Please enter a positive number :)")
                continue
            break
        except ValueError:
            print("Please enter a valid number :)")

    volume = side ** 3
    print(f"The volume of the cube is {volume}")
    volume_to_add = f"Volume:{volume}"
    data_to_add = f"Side:{side}"
    add_to_volume_history("Cube", volume_to_add, data_to_add)


def volume_of_sphere():  # کره
    while 1:
        try:
            radius = float(input("Enter the radius of the sphere: "))
            if radius <= 0:
                print("Please enter a positive number :)")
                continue
            break
        except ValueError:
            print("Please enter a valid number :)")

    volume = (4 / 3) * math.pi * (radius ** 3)
    print(f"The volume of the sphere is {volume}")
    volume_to_add = f"Volume:{volume}"
    data_to_add = f"Radius:{radius}"
    add_to_volume_history("Sphere", volume_to_add, data_to_add)


def volume_of_hemisphere():  # نیم کره
    while 1:
        try:
            radius = float(input("Enter the radius of the hemisphere: "))
            if radius <= 0:
                print("Please enter a positive number :)")
                continue
            break
        except ValueError:
            print("Please enter a valid number :)")

    volume = (2 / 3) * math.pi * (radius ** 3)
    print(f"The volume of the hemisphere is {volume}")
    volume_to_add = f"Volume:{volume}"
    data_to_add = f"Radius:{radius}"
    add_to_volume_history("Hemisphere", volume_to_add, data_to_add)


def volume_of_cylinder():  # استوانه
    while 1:
        try:
            radius = float(input("Enter the radius of the cylinder: "))
            if radius <= 0:
                print("Please enter a positive number :)")
                continue
            break
        except ValueError:
            print("Please enter a valid number :)")
    while 1:
        try:
            height = float(input("Enter the height of the cylinder: "))
            if height <= 0:
                print("Please enter a positive number :)")
                continue
            break
        except ValueError:
            print("Please enter a valid number :)")

    volume = math.pi * (radius ** 2) * height
    print(f"The volume of the cylinder is {volume}")
    volume_to_add = f"Volume:{volume}"
    data_to_add = f"Radius:{radius}\nHeight:{height}"
    add_to_volume_history("Cylinder", volume_to_add, data_to_add)


def volume_of_cone():  # مخروط
    while 1:
        try:
            radius = float(input("Enter the radius of the cone: "))
            if radius <= 0:
                print("Please enter a positive number :)")
                continue
            break
        except ValueError:
            print("Please enter a valid number :)")

    while 1:
        try:
            height = float(input("Enter the height of the cone: "))
            if height <= 0:
                print("Please enter a positive number :)")
                continue
            break
        except ValueError:
            print("Please enter a valid number :)")

    volume = (1 / 3) * math.pi * (radius ** 2) * height
    print(f"The volume of the cone is {volume}")
    volume_to_add = f"volume:{volume}"
    data_to_add = f"Radius:{radius}\nHeight:{height}"
    add_to_volume_history("Cone", volume_to_add, data_to_add)


# ===================================================================

# history and database
def create_history():
    connection_1 = sqlite3.connect('history.db')
    cursor = connection_1.cursor()
    cmd_to_create = """ CREATE TABLE IF NOT EXISTS operation_history(
            operations VARCHAR(100));
    """
    cmd = """
        CREATE TABLE IF NOT EXISTS a_history (
        shape VARCHAR(100),
        sizes VARCHAR(100),
        area VARCHAR(100));
        """
    cmd_2 = """
        CREATE TABLE IF NOT EXISTS p_history (
        shape VARCHAR(100),
        sizes VARCHAR(100),
        perimeter VARCHAR(100));
        """
    cmd_3 = """
        CREATE TABLE IF NOT EXISTS volume_history (
        shape VARCHAR(100),
        sizes VARCHAR(100),
        volume VARCHAR(100));
        """
    cursor.execute(cmd)
    cursor.execute(cmd_2)
    cursor.execute(cmd_3)
    cursor.execute(cmd_to_create)
    connection_1.commit()
    connection_1.close()


def add_operation_to_history(operation_to_add):
    connection_1 = sqlite3.connect('history.db')
    cursor = connection_1.cursor()
    cmd_to_add = f"INSERT INTO operation_history (operations) VALUES ('{operation_to_add}');"
    cursor.execute(cmd_to_add)
    connection_1.commit()
    connection_1.close()


def add_to_a_history(shape_to_add, size_to_add, a_to_add):
    connection = sqlite3.connect("history.db")
    cursor = connection.cursor()
    cmd = f"INSERT INTO a_history (shape, sizes, area) VALUES ('{shape_to_add}', '{size_to_add}', '{a_to_add}');"
    cursor.execute(cmd)
    connection.commit()
    connection.close()


def add_to_p_history(shape_to_add, size_to_add, p_to_add):
    connection = sqlite3.connect("history.db")
    cursor = connection.cursor()
    cmd = f"INSERT INTO p_history (shape, sizes, perimeter) VALUES ('{shape_to_add}', '{size_to_add}', '{p_to_add}');"
    cursor.execute(cmd)
    connection.commit()
    connection.close()


def add_to_volume_history(shape_to_add, size_to_add, volume_to_add):
    connection = sqlite3.connect("history.db")
    cursor = connection.cursor()
    cmd = f"INSERT INTO volume_history (shape, sizes, volume) VALUES ('{shape_to_add}', '{size_to_add}', '{volume_to_add}');"
    cursor.execute(cmd)
    connection.commit()
    connection.close()


def show_the_operation_history():
    loading("accessing history")
    connection_1 = sqlite3.connect('history.db')
    cursor = connection_1.cursor()
    cmd_to_show = """SELECT * FROM operation_history;"""
    cursor.execute(cmd_to_show)
    print(f"here is your operation history:\n{70 * "="}")
    for operation in cursor:
        print(operation[0])
    connection_1.commit()
    connection_1.close()


def show_a_history():
    connection = sqlite3.connect("history.db")
    cursor = connection.cursor()
    cmd = f"SELECT * FROM a_history;"
    cursor.execute(cmd)
    print(f"Here is your area history:\n{70 * "="}")
    for operation in cursor:
        print(f"Shape: {operation[0]}\n{operation[1]}\n{operation[2]}\n{"_" * 40}\n\n")
    connection.commit()
    connection.close()


def show_p_history():
    connection = sqlite3.connect("history.db")
    cursor = connection.cursor()
    cmd = f"SELECT * FROM p_history;"
    cursor.execute(cmd)
    print(f"Here is your perimeter history:\n{70 * "="}")
    for operation in cursor:
        print(f"Shape:{operation[0]}\n{operation[1]}\nData:{operation[2]}\n{"_" * 40}\n\n")
    connection.commit()
    connection.close()


def show_volume_history():
    connection = sqlite3.connect("history.db")
    cursor = connection.cursor()
    cmd = f"SELECT * FROM volume_history;"
    cursor.execute(cmd)
    print(f"Here is your volume history:\n{70 * "="}")
    for operation in cursor:
        print(f"Shape:{operation[0]}\n{operation[1]}\nData:{operation[2]}\n{"_" * 40}\n\n")
    connection.commit()
    connection.close()


def delete_the_operation_history():
    connection_1 = sqlite3.connect('history.db')
    cursor = connection_1.cursor()
    cmd_to_delete = """DROP TABLE operation_history;"""
    cursor.execute(cmd_to_delete)
    connection_1.commit()
    connection_1.close()


def delete_a_history():
    connection = sqlite3.connect("history.db")
    cursor = connection.cursor()
    cmd = """DROP TABLE IF EXISTS a_history;"""
    cursor.execute(cmd)
    print(f"Your history deleted successfully\n{"_" * 40}\n\n")
    connection.commit()
    connection.close()


def delete_p_history():
    connection = sqlite3.connect("history.db")
    cursor = connection.cursor()
    cmd = """DROP TABLE IF EXISTS p_history;"""
    cursor.execute(cmd)
    print(f"Your history deleted successfully\n{"_" * 40}\n\n")
    connection.commit()
    connection.close()


def delete_volume_history():
    connection = sqlite3.connect("history.db")
    cursor = connection.cursor()
    cmd = """DROP TABLE IF EXISTS volume_history;"""
    cursor.execute(cmd)
    print(f"Your history deleted successfully\n{"_" * 40}\n\n")
    connection.commit()
    connection.close()


# ===================================================================

# menus
def operation_menu():
    loading("operation menu")
    print("welcome to operation menu!")
    print("what kind of operation do you want?")
    while 1:
        print("\n\n1-sum operation")
        print("2-subtraction operation")
        print("3-multiplication operation")
        print("4_division operation")
        print("5-power operation")
        print("6-radical operation")
        print("0-back to home menu")
        while 1:
            try:
                operation_to_do = int(input("your operation: "))
                break
            except Exception as err:
                print(err)
                print("\nyou should enter the number of you request")
        if operation_to_do == 0:
            loading("backing to home menu")
            break
        elif operation_to_do == 1:
            sum()
        elif operation_to_do == 2:
            sub()
        elif operation_to_do == 3:
            multiply()
        elif operation_to_do == 4:
            devide()
        elif operation_to_do == 5:
            pow()
        elif operation_to_do == 6:
            radical()
        else:
            print("\nyou should enter the number of you operation")


def bmi_menu():
    loading("bmi menu")
    print("Welcome to bmi calculator!")
    print("what is your request?")
    while 1:
        print("\n\n1-bmi operation")
        print("0-back to home menu")
        while 1:
            try:
                request = int(input("your operation: "))
                break
            except Exception as err:
                print(err)
                print("\nyou should enter the number of you request")
        if request == 0:
            loading("backing to home menu")
            break
        elif request == 1:
            calculate_bmi()
        else:
            print("\nyou should enter the number of you request")


def area_menu():
    loading("area menu")
    print("Welcome to Area menu.")
    print("In this section you can calculate the area of different shapes.")
    while 1:
        print("1-Square")
        print("2-Rectangle")
        print("3-Triangle")
        print("4-Rhomboid")
        print("5-Parallelogram")
        print("6-Trapezium")
        print("7-Circle")
        print("0-Back to APV menu")
        while 1:
            try:
                choice = int(input("Enter your choice: "))
                break
            except ValueError:
                print("Please enter a valid number :)")

        if choice == 1:
            area_of_square()
        elif choice == 2:
            area_of_rectangle()
        elif choice == 3:
            area_of_triangle()
        elif choice == 4:
            area_of_rhomboid()
        elif choice == 5:
            area_of_parallelogram()
        elif choice == 6:
            area_of_trapezium()
        elif choice == 7:
            area_of_circle()
        elif choice == 0:
            loading("backing to apv menu")
            break
        else:
            print("Please enter a valid choice")


def perimeter_menu():
    loading("perimeter menu")
    print("Welcome to Perimeter menu.")
    print("In this section you can calculate the perimeter of different shapes.")
    while 1:
        print("1-Square")
        print("2-Rectangle")
        print("3-Triangle")
        print("4-Rhomboid")
        print("5-Parallelogram")
        print("6-Trapezium")
        print("7-Circle")
        print("0-Back to APV menu")
        while 1:
            try:
                choice = int(input("Enter your choice: "))
                break
            except ValueError:
                print("Please enter a valid number :)")

        if choice == 1:
            perimeter_of_square()
        elif choice == 2:
            perimeter_of_rectangle()
        elif choice == 3:
            perimeter_of_triangle()
        elif choice == 4:
            perimeter_of_rhomboid()
        elif choice == 5:
            perimeter_of_parallelogram()
        elif choice == 6:
            perimeter_of_trapezium()
        elif choice == 7:
            perimeter_of_circle()
        elif choice == 0:
            loading("backing to apv menu")
            break
        else:
            print("Please enter a valid choice")


def volume_menu():
    loading("volume menu")
    print("Welcome to volume menu.")
    print("In this section you can calculate the volume of different shapes.")
    while 1:
        print("1-Cube")
        print("2-Sphere")
        print("3-Hemisphere")
        print("4-Cylinder")
        print("5-Cone")
        print("0-Back to APV menu")
        while 1:
            try:
                choice = int(input("Enter your choice: "))
                break
            except ValueError:
                print("Please enter a valid number :)")
        if choice == 1:
            volume_of_cube()
        elif choice == 2:
            volume_of_sphere()
        elif choice == 3:
            volume_of_hemisphere()
        elif choice == 4:
            volume_of_cylinder()
        elif choice == 5:
            volume_of_cone()
        elif choice == 0:
            loading("backing to apv menu")
            break
        else:
            print("Please enter a valid choice")


def apv_menu():
    loading("apv menu")
    print("Welcome to APV (Area, Perimeter, Volume) menu.")
    print("You can calculate area, perimeter and volume of different shapes.")
    while 1:
        print("1-Area menu")
        print("2-Perimeter menu")
        print("3-Volume menu")
        print("0-Back to home menu")
        while 1:
            try:
                choice = int(input("Enter your choice: "))
                break
            except ValueError:
                print("Please enter a valid number :)")

        if choice == 1:
            area_menu()
        elif choice == 2:
            perimeter_menu()
        elif choice == 3:
            volume_menu()
        elif choice == 0:
            loading("backing to home menu")
            break
        else:
            print("Please enter a valid number :)")


def history_menu():
    loading("history menu")
    print("welcome to history menu!\n\n")
    while 1:
        print("\nwhat do you want?")
        print("1-operation history")
        print("2-Area history")
        print("3-Perimeter history")
        print("4-Volume history")
        print("5-delete operation history")
        print("6-Delete area history")
        print("7-Delete perimeter history")
        print("8-Delete volume history")
        print("0-back to home menu")
        while 1:
            try:
                request_to_do_2 = int(input("your request: "))
                break
            except ValueError:
                print("\nyou should enter the number of you request")
        if request_to_do_2 == 0:
            print(f"\n")
            loading("backing to home menu")
            break
        elif request_to_do_2 == 1:
            show_the_operation_history()
        elif request_to_do_2 == 2:
            show_a_history()
        elif request_to_do_2 == 3:
            show_p_history()
        elif request_to_do_2 == 4:
            show_volume_history()
        elif request_to_do_2 == 5:
            delete_the_operation_history()
            print("your history has been deleted\n\n")
            create_history()
        elif request_to_do_2 == 6:
            delete_a_history()
            print("your history has been deleted\n\n")
            create_history()
        elif request_to_do_2 == 7:
            delete_p_history()
            print("your history has been deleted\n\n")
            create_history()
        elif request_to_do_2 == 8:
            delete_volume_history()
            print("your history has been deleted\n\n")
            create_history()
        else:
            print("\nyou should enter the number of you request")


def length_menu():
    loading("length menu")
    print("Welcome to length menu.")
    while 1:
        print("\nwhat do you want to convert?")
        print("1-centimeter")
        print("2-meter")
        print("3-millimeter")
        print("4-kilometer")
        print("5-mile")
        print("0-back to home menu")
        first = input("your request: ")
        if first == "0":
            print(f"\n")
            loading("backing to home menu")
            break
        elif first == "1":
            while 1:
                try:
                    second = int(input("how many centimeter? "))
                    length("cm", second)
                    break
                except Exception as e:
                    print(e)
                    print("enter a valid number")
        elif first == "2":
            while 1:
                try:
                    second = int(input("how many meter? "))
                    length("m", second)
                    break
                except Exception as e:
                    print(e)
                    print("enter a valid number")
        elif first == "3":
            while 1:
                try:
                    second = int(input("how many millimeter? "))
                    length("mm", second)
                    break
                except Exception as e:
                    print(e)
                    print("enter a valid number")
        elif first == "4":
            while 1:
                try:
                    second = int(input("how many kilometer? "))
                    length("km", second)
                    break
                except Exception as e:
                    print(e)
                    print("enter a valid number")
        elif first == "5":
            while 1:
                try:
                    second = int(input("how many miles? "))
                    length("mile", second)
                    break
                except Exception as e:
                    print(e)
                    print("enter a valid number")
        else:
            print("\nyou should enter the number of you request")


def calculator():
    loading("\033[1m"+"welcome to the caculator"+"\033[0m")
    create_history()
    while 1:
        print("home menu")
        print("what is your request?")
        print("1-operation menu")
        print("2-apv menu")
        print("3-bmi menu")
        print("4-length menu")
        print("5-history menu")
        print("0-exit")
        while 1:
            try:
                request = int(input("your request: "))
                break
            except ValueError:
                print("\nyou should enter the number of you request")
        if request == 0:
            print("\nthe calculator has been stopped")
            break
        elif request == 1:
            operation_menu()
        elif request == 2:
            apv_menu()
        elif request == 3:
            bmi_menu()
        elif request == 4:
            length_menu()
        elif request == 5:
            history_menu()
        else:
            print("\nyour entry is not a valid option")


# ====================================================================

# run part
calculator()
