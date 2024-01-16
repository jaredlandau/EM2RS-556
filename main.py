from driver import Driver
from motor import Motor
from console import Console

PORT = "COM4"
DEBUG_MODE = False


def main():
    driver = Driver(PORT, DEBUG_MODE)
    motor = Motor(driver)
    console = Console(motor)

    console.main()


if __name__ == "__main__":
    main()
