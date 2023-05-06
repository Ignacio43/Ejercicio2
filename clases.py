class ViajeroFrecuente:
    __num_viajero= 0
    __dni=''
    __nombre=''
    __apellido=''
    __millas_acum=0

    def __init__(self,num_viajero,dni,nombre,apellido,millas_acum):
        self.__num_viajero=num_viajero
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido    
        self.__millas_acum=millas_acum
        
    def cantidadTotalMillas(self):
        return self.__millas_acum
    
    def acumularMillas(self,millas_recorridas):
        self.__millas_acum+=millas_recorridas
        return self.__millas_acum
    
    def canjearMillas(self,millas_canje):
        if millas_canje <= self.__millas_acum:
           self.__millasacum-=millas_canje
           print("se pudo realizar el canje")
        else:
            print("error en la operacion")              
    
    def get_num_viaje(self):
        return self.__num_viajero