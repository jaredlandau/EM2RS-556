import threading

# GLOBAL VARIABLES
STOP_FLAG = threading.Event()

# REGISTER ADDRESSES
REG_MOTORDIRECTION  = 0x0007        # (Pr0.03)	default: 0		decimals: 0
REG_PEAKCURRENT     = 0x0191        # (Pr5.00)	default: 10		decimals: 1
REG_BAUDRATE        = 0x01BD        # (Pr5.22) 	default: 4		decimals: 0
REG_JOGVELOCITY     = 0x01E1        # (Pr6.00)	default: 60		decimals: 0
REG_PRCONTROL       = 0x6002        # (Pr8.02)	default: 256	decimals: 0
REG_CONTROLWORD     = 0x1801        # (------)	default: 0		decimals: 0

DIRECTION_CODES = {
    "CLOCKWISE": 0x4001,
    "CW": 0x4001,
    "COUNTERCLOCKWISE": 0x4002,
    "CCW": 0x4002
}


class Motor:
    def __init__(self, driver):
        self.driver = driver
        self.current_thread = None

    def start_thread(self, direction, steps, speed):
        if self.current_thread and self.current_thread.is_alive():
            self.current_thread.join()

        current_thread = threading.Thread(target=self.step_motor, args=(direction, steps, speed))
        STOP_FLAG.clear()
        current_thread.start()

    def step_motor(self, direction, steps, speed=60):
        print(f"[INFO] Stepping {direction} {steps} times.\n")

        direction_code = DIRECTION_CODES.get(direction)

        self.driver.write_register(REG_JOGVELOCITY, speed, 0)
        for i in range(steps):
            if STOP_FLAG.is_set():
                break
            self.driver.write_register(REG_CONTROLWORD, direction_code, 0)

        self.driver.write_register(REG_JOGVELOCITY, 60, 0)

    def stop(self):
        STOP_FLAG.set()

        #if not self.driver.read_register(REG_PRCONTROL, 0) == 0x40:
            #self.driver.write_register(REG_PRCONTROL, 0x40, 0)

        if self.current_thread and self.current_thread.is_alive():
            self.current_thread.join()

        print("[INFO] Motor quick-stop engaged.\n")
