import minimalmodbus


class Driver:
    def __init__(self, port="COM4", debug_mode=False):
        self.driver = minimalmodbus.Instrument(port, 1, minimalmodbus.MODE_RTU)

        self.driver.mode = minimalmodbus.MODE_RTU
        self.driver.close_port_after_each_call = True
        self.driver.serial.baudrate = 38400
        self.driver.serial.parity = 'N'
        self.driver.serial.bytesize = 8
        self.driver.serial.stopbits = 1
        self.driver.serial.timeout = 0.05
        self.driver.clear_buffers_before_each_transaction = True

        self.debug_mode = debug_mode

    def read_register(self, reg_address, decimals):
        try:
            value = self.driver.read_register(reg_address, decimals)
            if self.debug_mode:
                print(f"[DEBUG] REG: {hex(reg_address)}, VALUE: {value}\n")
        except IOError:
            print("[ERROR] Failed to read data from driver.")

    def write_register(self, reg_address, value, decimals):
        try:
            self.driver.write_register(reg_address, value, decimals)
            self.driver.read_register(reg_address, decimals)
            if self.debug_mode:
                print("[DEBUG] Data written successfully.")
        except IOError:
            print("[ERROR]: Failed to write data to driver.")
