import pyvisa
import time # for sleep
import binascii

def main():
    rm = pyvisa.ResourceManager()
    ADR = 'TCPIP0::11.0.0.2::5025::INSTR'
    ps = rm.open_resource(ADR)
    ps.query('*IDN?')
    time.sleep(0.04) #Wait
    ps.query('OUTP CH1,ON') #Turn on output
    time.sleep(2) #Wait
    ps.query('OUTP CH1,OFF') #Turn off output
    time.sleep(1) #Wait
    ps.close() #Close instrument VISA session

if __name__ == '__main__':
    main()
