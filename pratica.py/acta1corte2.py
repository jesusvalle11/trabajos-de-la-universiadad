from collections import deque
from dataclasses import dataclass

@dataclass
class Archivo:
    def __init__(self,titulo,autor,prioridad):
        self.titulo=titulo
        self.autor=autor
        self.prioridad=prioridad
        
    def mostrar(self):
     return f"Documento:{self.titulo}, prioridad: {self.prioridad}"

class impre:
    def __init__(self):
        self.cola_prioridad_alta = deque()
        self.cola_prioridad_normal= deque()
        
    def agre_docu(self,titulo,autor,prioridad):
        doc = Archivo(titulo,autor,prioridad)
        if prioridad == 1:          
            self.cola_prioridad_alta.append(doc)
        else:                                  
            self.cola_prioridad_normal.append(doc)
        print("el documento ya esta agregado.")
        
    def sigui_doc(self):
        if self.cola_prioridad_alta:
            doc= self.cola_prioridad_alta.popleft()
        elif self.cola_prioridad_normal:
            doc= self.cola_prioridad_normal.popleft()
        else:
            print("documento no he encontrado en la cola ")
            return
        print("procesando: ", doc)
        
    def estado(self):
        print("documento en la cola de impresion")
        
        if not self.cola_prioridad_alta and not self.cola_prioridad_normal:
            print("la cola esta vacia\n")
            return
        
        if self.cola_prioridad_alta:
            print("\n prioridad alta")
            for doc in self.cola_prioridad_alta:
                print(f" {doc.titulo} | usuario: {doc.autor}")
        else:
            print("\n prioridad Alta: si documento")
        
        if self.cola_prioridad_normal:
            print("\n prioridad normal:")
            for doc in self.cola_prioridad_normal:
                print(f"{doc.titulo} | usuario: {doc.autor}")
        else:
            print("prioridad normal: sin documebtos")
            
print("")
print("\n---------------")

cola= impre()
cola.agre_docu("informe de cuenta.pdf","maria",1)
cola.agre_docu("informe de fisica.pdf","mario",2)  
cola.agre_docu("pendulo fisico.pdf","davis",2) 
cola.estado()
cola.sigui_doc()
cola.estado()
        