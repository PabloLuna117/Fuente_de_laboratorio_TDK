import TDK
import time
def SETconfiguracionesDeFuenteTDK(port,addr):
    return TDK.SETconfiguracionesDeFuenteTDK(port,addr)
def SETvoltajeANDCorriente(voltage, current,ONOFF):
    return TDK.SETvoltajeANDCorriente(voltage, current,ONOFF)
def GETVoltajeCurrent():
    return TDK.GETVoltajeCurrent()
