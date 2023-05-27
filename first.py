# -*- coding: utf-8 -*-
"""
Created on Wed May 24 02:49:18 2023

@author: rafa0
"""
#Librerias necesarias para poder correr el codigo, lo hice en terminal IDE de SPyder No Funciona

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import threading
import time


#La clase tradingApp es la que se encarga de verificar la conexion y notificar de cualquier error que suceda

class tradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self,self)
        self.connect("127.0.0.1", 7497, clientId=1)
  
    def error(self, reqId, errorCode, errorString):
        print("Error {} {} {}".format(reqId, errorCode,errorString))
    
    def contractDetails(self, reqId, contractDetails):
        print("reqId: {}, contract:{}".format(reqId, contractDetails))

    def run(self):
        super().run()
    
def websocket_con(): #Ejecuta en otro thread Daemon
    app.run()

app = tradingApp()
#app.connect("127.0.0.1", 7497, clientId=1)  #Codigo necesario para confirmar el puerto y el ID del dispositivo


con_thread = threading.Thread(target=websocket_con, daemon=True) #Creamos otro thread daemon para correr la app.
con_thread.start()
time.sleep(1)


#Cada Contrato requiere que se le confirme SYMBOL, SECURITY TYPE, CURRENCY, EXCHANGE y otras varian dependiendo el tipo de contrato

#Toda esa informacion se encuentra en la plataforma de TWS
contract = Contract()
contract.symbol = "ETH"
contract.secType = "CRYPTO"
contract.currency = "USD"
contract.exchange = "PAXOS" 

app.reqContractDetails(100, contract)
time.sleep(5)


