import serial
class scanner_reader():
    def __init__(self):
        self.port = "/dev/tty.usbserial-BH001H04"
        self.baudrate = 9600


    def start_reader(self,onoroff):
        connection = serial.Serial(port=self.port,baudrate=self.baudrate)
        fullUPC = b""
        while onoroff:
            fullUPC+=connection.read()
            if len(fullUPC) == 12:
                return fullUPC







#reader = scanner_reader()
#reader.start_reader(onoroff=True)
