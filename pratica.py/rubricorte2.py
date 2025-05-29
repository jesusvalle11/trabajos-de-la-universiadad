from collections import deque
class centro_vacu:
    def __init__(self):
        self.vacunacion= deque()


    def regi_person(self,nombre,identificaacion,sexo):
        persona= {"nombre":nombre, "identificacion":identificaacion,"sexo":sexo}
        self.vacunacion.append(persona)
        print(f"{nombre} ({sexo}) ya se ha registrado a una persona en la cola de vacunacion")
    
    
    def aten_p(self):
        if self.vacunacion:
            persona= self.vacunacion.popleft()
            print(f"Atendiendo a {persona['nombre']} ({persona['sexo']}) con identificacion {persona['identificacion']}")
        else:
            print("No hay personas en la cola de vacunacion")
    
    
    def consu_es(self):
        print(f"hay{len(self.vacunacion)} personas esperando. ")
    
    def siguientes(self):
        if self.vacunacion:
            print("Las siguientes personas en la cola son:")
            for persona in self.vacunacion:
                print(f"{persona['nombre']} ({persona['sexo']}) con identificacion {persona['identificacion']}")
        else:
            print("No hay personas en la cola de vacunacion")
        

centro= centro_vacu()   
centro.regi_person("Jesus", "1043661935", "Masculino")
centro.regi_person("eshter", "1104334343", "Femenino")
centro.consu_es()
centro.siguientes()
centro.aten_p()
centro.consu_es()
centro.siguientes()
