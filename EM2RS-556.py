import minimalmodbus
import threading
import time
import os

# GLOBAL VARIABLES
PORT = 'COM4'
DRIVER = minimalmodbus.Instrument(PORT, 1, minimalmodbus.MODE_RTU)
STOP_FLAG = threading.Event()
DEBUG_MODE = False

# REGISTER ADDRESSES
REG_MOTORDIRECTION = 0x0007     # (Pr0.03)	default: 0		decimals: 0
REG_PEAKCURRENT = 0x0191        # (Pr5.00)	default: 10		decimals: 1
REG_BAUDRATE = 0x01BD           # (Pr5.22) 	default: 4		decimals: 0
REG_JOGVELOCITY = 0x01E1        # (Pr6.00)	default: 60		decimals: 0
REG_PRCONTROL = 0x6002          # (Pr8.02)	default: 256	decimals: 0
REG_CONTROLWORD = 0x1801        # (------)	default: 0		decimals: 0

DIRECTION_CODES = {
    "CLOCKWISE": 0x4001,
    "CW": 0x4001,
    "COUNTERCLOCKWISE": 0x4002,
    "CCW": 0x4002
}

# Writing value 0x40 to register 0x6002 (PRCONTROL) will quick-stop the motor
# Writing value 0x4001 to register 0x1801 (CONTROLWORD) will turn the motor clockwise
# Writing value 0x4002 to register 0x1801 (CONTROLWORD) will turn the motor counter-clockwise


def start_thread(function):
    currentThread = threading.Thread(target=stepClockwise, args=(steps, speed))
    STOP_FLAG.clear()
    currentThread.start()


def step_motor(direction, steps, speed=60):
    print(f"INFO: Stepping {direction} {steps} times.\n")

    directionCode = DIRECTION_CODES.get(direction)

    write_register(REG_JOGVELOCITY, speed, 0)
    for i in range(steps):
        if (STOP_FLAG.is_set()):
            break
        write_register(REG_CONTROLWORD, directionCode, 0)

    write_register(REG_JOGVELOCITY, 60, 0)


def stop_motor():
    if not (read_register(REG_PRCONTROL, 0) == 0x40):
        write_register(REG_PRCONTROL, 0x40, 0)
    STOP_FLAG.set()
    print("INFO: Motor quick-stop engaged.\n")


def read_register(reg_address, decimals):
    try:
        value = DRIVER.read_register(reg_address, decimals)
        reg_address_str = str(hex(reg_address))
        if DEBUG_MODE:
            print(reg_address_str + ": " + str(value) + "\n")
    except IOError:
        print("ERROR: Failed to read data from driver.")


def write_register(regAddress, value, decimals):
    try:
        DRIVER.write_register(regAddress, value, decimals)
        read_register(regAddress, decimals)
        if DEBUG_MODE:
            print("INFO: Data written successfully.")
    except IOError:
        print("ERROR: Failed to write data to driver.")


def displayMenu():
    os.system('cls')
    print()
    print("HELP						Displays this information again.")
    print("CLOCKWISE <steps> <speed>			Steps the motor clockwise.")
    print("COUNTERCLOCKWISE <steps> <speed>		Steps the motor counterclockwise.")
    print("STOP						Engages the quick-stop functionality on the motor.")
    print("EXIT						Exits the program.")
    print()


def main():
    # Driver Parameters
    DRIVER.mode = minimalmodbus.MODE_RTU
    DRIVER.close_port_after_each_call = True
    DRIVER.serial.baudrate = 38400
    DRIVER.serial.parity = 'N'
    DRIVER.serial.bytesize = 8
    DRIVER.serial.stopbits = 1
    DRIVER.serial.timeout = 0.05
    DRIVER.clear_buffers_before_each_transaction = True

    # === === === === === #
    current_thread = None

    if DEBUG_MODE:
        DRIVER.debug = True
        print(DRIVER)

    displayMenu()

    is_running = True
    while is_running:
        user_input = str.upper(input())

        if user_input == "HELP":
            displayMenu()
        elif any(user_input.startswith(prefix) for prefix in ["CLOCKWISE", "CW", "COUNTERCLOCKWISE", "CCW"]):
            try:
                direction, steps, speed = user_input.split()
                steps = int(steps)
                speed = int(speed)

                if not ((speed >= 0) and (speed <= 5000)):
                    raise ValueError

                if current_thread and current_thread.is_alive():
                    current_thread.join()

                current_thread = threading.Thread(target=step_motor, args=(direction, steps, speed))
                STOP_FLAG.clear()
                current_thread.start()
            except ValueError:
                print("ERROR: Invalid argument(s).")
        elif user_input == "STOP":
            stop_motor()
            if current_thread and current_thread.is_alive():
                current_thread.join()
        elif user_input == "EXIT":
            is_running = False
            break
        else:
            print("ERROR: Invalid command. Type HELP for the list of commands.\n")

if __name__ == "__main__":
    main()
