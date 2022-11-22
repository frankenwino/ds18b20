import glob
import time
from datetime import datetime


class DS18B20:
    """Gets temperature in delciuous and farenheit using a ds18b20 sensor.
    """    
    def __init__(self) -> None:
        """__init__ Constructor.
        """        
        self.temp_c, self.temp_f = self.read_temp()

    def now(self) -> str:
        """now gets the current date and time.

        Returns:
            str: Date/time in format YYYY-MM-DD HH:MM:SS
        """        
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def read_temp_raw(self) -> list[str]:
        """read_temp_raw gets raw data from ds18b20 sensor

        Returns:
            list[str]: raw data from ds18b20 sensor
        """        
        base_dir = "/sys/bus/w1/devices/"
        device_folder = glob.glob(base_dir + "28*")[0]
        device_file = device_folder + "/w1_slave"
        with open(device_file, "r") as f:
            lines = f.readlines()

        return lines

    def read_temp(self) -> tuple[float, float]:
        """read_temp parses raw data from the ds18b20 sensor

        Returns:
            tuple[float, float]: celsius, farenheit
        """        
        lines = self.read_temp_raw()
        while lines[0].strip()[-3:] != "YES":
            time.sleep(0.2)
            lines = self.read_temp_raw()
        equals_pos = lines[1].find("t=")
        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2 :]
            temp_c = float(temp_string) / 1000.0
            temp_c = round(temp_c, 1)
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            temp_f = round(temp_f, 1)

            return temp_c, temp_f

    def celsius(self) -> float:
        """celsius gets the current temperature in celsius.

        Returns:
            float: Current temperature in celsius.
        """        
        return self.temp_c

    def farenheit(self) -> float:
        """farenheit gets the current temperature in farenheit.

        Returns:
            float:Current temperature in farenheit.
        """        
        return self.temp_f


if __name__ == "__main__":
    t = DS18B20()
    print(t.now())
    print(f"Celsius: {t.celsius()}c")
    print(f"Farenheit: {t.farenheit()}f")
