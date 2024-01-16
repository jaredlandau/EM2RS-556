import os


class Console:
    def __init__(self, motor):
        self.motor = motor
        self.start()

    @staticmethod
    def display_menu():
        os.system('cls')
        print()
        print("HELP						Displays this information again.")
        print("CLOCKWISE <steps> <speed>			Steps the motor clockwise.")
        print("COUNTERCLOCKWISE <steps> <speed>		Steps the motor counterclockwise.")
        print("STOP						Engages the quick-stop functionality on the motor.")
        print("EXIT						Exits the program.")
        print()

    def start(self):
        self.display_menu()

        is_running = True
        while is_running:
            user_input = str.upper(input())

            if user_input == "HELP":
                display_menu()

            elif any(user_input.startswith(prefix) for prefix in ["CLOCKWISE", "CW", "COUNTERCLOCKWISE", "CCW"]):
                try:
                    direction, steps, speed = user_input.split()
                    steps = int(steps)
                    speed = int(speed)

                    if not (0 <= speed <= 5000):
                        raise ValueError

                    self.motor.start_thread(direction, steps, speed)
                except ValueError:
                    print("[ERROR] Invalid argument(s).")

            elif user_input == "STOP":
                self.motor.stop()

            elif user_input == "EXIT":
                is_running = False
                break

            else:
                print("[ERROR] Invalid command. Type HELP for the list of commands.\n")
