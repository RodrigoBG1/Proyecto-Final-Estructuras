import os
import time
import random
import threading
import tkinter as tk
from itertools import islice

Titulo = """
$$$$$$$\                      $$\                        $$\     $$\                         $$\       
$$  __$$\                     $$ |                       $$ |    $$ |                        $$ |      
$$ |  $$ | $$$$$$\  $$$$$$$\  $$ |  $$\        $$$$$$\ $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$$\ $$ |  $$\ 
$$$$$$$\ | \____$$\ $$  __$$\ $$ | $$  |       \____$$  _$$  _|\_$$  _|   \____$$\ $$  _____|$$ | $$  |
$$  __$$\  $$$$$$$ |$$ |  $$ |$$$$$$  /        $$$$$$$ | $$ |    $$ |     $$$$$$$ |$$ /      $$$$$$  / 
$$ |  $$ |$$  __$$ |$$ |  $$ |$$  _$$<        $$  __$$ | $$ |$$\ $$ |$$\ $$  __$$ |$$ |      $$  _$$<  
$$$$$$$  |\$$$$$$$ |$$ |  $$ |$$ | \$$\       \$$$$$$$ | \$$$$  |\$$$$  |\$$$$$$$ |\$$$$$$$\ $$ | \$$\ 
\_______/  \_______|\__|  \__|\__|  \__|       \_______|  \____/  \____/  \_______| \_______|\__|  \__|
"""
Personaje = """
                        .------.
                       / j      ;
                      :.d;       ;
                      $$P        :
           .m._       $$         :
          dSMMSSSss.__$$b.    __ :
         :MMSMMSSSMMMSS$$$b  $$P ;
         SMMMSMMSMMMSSS$$$$     :b
        dSMMMSMMMMMMSSMM$$$b.dP SSb.
       dSMMMMMMMMMMSSMMPT$$=-. /TSSSS.
      :SMMMSMMMMMMMSMMP  `$b_.'  MMMMSS.
      SMMMMMSMMMMMMMMM \  .'\    :SMMMSSS.             
     dSMSSMMMSMMMMMMMM  \/\_/; .'SSMMMMSSSm            
    dSMMMMSMMSMMMMMMMM    :.;'" :SSMMMMSSMM;          
  .MMSSSSSMSSMMMMMMMM;    :.;   MMSMMMMSMMM;           
 dMSSMMSSSSSSSMMMMMMM;    ;.;   MMMMMMMSMMM            
:MMMSSSSMMMSSP^TMMMMM     ;.;   MMMMMMMMMMM            
MMMSMMMMSSSSP   `MMMM     ;.;   :MMMMMMMMM;
"TMMMMMMMMMM      TM;    :`.:    MMMMMMMMM;
   )MMMMMMM;     _/     :`.:    :MMMMMMMM
  d$SS$$$MMMb.  |._\    :`.:     MMMMMMMM
  T$$S$$$$$$$$$$m;O"-;`.:_.-  MMMMMMM;
 :$$$$$$$$$$$$$$$b_l./ ;`.:    mMMSSMMM;
 :$$$$$$$$$$$$$$$$$$$./;`.:  .$$MSMMMMMM
  $$$$$$$$$$$$$$$$$$$$. `.:.$$$$SMSSSMMM;
  $$$$$$$$$$$$$$$$$$$$$. .:$$$$$SSMMMMMMM
  :$$$$$$$$$$$$$$$$$$$$$.//.:$$$$SSSSSSSMM;
  :$$$$$$$$$$$$$$$$$$$$$$.`.:$$SSSSSSSMMMP
"""
print(Titulo, Personaje)

class Juego:
    def dialogos(self, mensaje):
        dialogo = """
                    dS$$S$S$S$S$S$S$$Sb                    
                   :$$S^S$S$S$S$S$S^S$$;                   
                   SSP   `^$S$S$^'   TSS                   
                   $$       `"'       $$                   
                  _SS ,-           -  SS_      ___________________________________            
                 :-.|  _    - .-   _  |.-;    |                                   
                 :\(; ' "-._.'._.-" ` |)/;    |    {}                            
                  \`|  , o       o .  |'/     |                                 
                   ":     -'   `-     ;"      |                                   
                     ;.              :        |                                   
                     : `    ._.    ' ;       /____________________________________            
                   .sSb   ._____.   dSs.                   
                _.d8dSSb.   ._.   .SSbT8b._                
            _.oOPd88SSSS T.     .P SSSS888OOo.             
        _.mMMOOPd888SSSSb TSqqqSP dSSSS88OMOOOMm._         
     .oOMMMOMOOM8O8OSSSSSb TSSSP dSSSSS8OOMMOOMMOOOo._     
   .OOMMOOOMMOOMOOOO  "^SSSTSSP dSSS^"OOOOMMOOMMMOOMMMb.   
  dOOOMMMOMMOOOMOOOO      "^SSSS^"   :OOO8MMMOOMMOOMMOMMb  
 :MMMOOMMOMMOOMMO8OS         `P      8O8OPdMMOOMMOMMOMMMM; 
 MMMMOOMMMMMOOMbTO8S;               :8888MMMMMOMMOMMOMMMMM 
 OMMMMOOMMMMOOOMMOOOS        S     :O8OPdMOMMMOMOMMOOMMMMO 
:OMMMMOOMMOMMOOMbTObTb.     :S;   .PdOPdMOOMMMMMOMMOMMMMMO;
MOOMMMMOMMOMMOOMMMOObTSSg._.SSS._.PdOPdMOOMMMMOMMMMOMMMMOOM
MMOMMMMOMMMOMMOOMMbT8bTSSSSSSSSSPd8OPdOOOMMMMOOMMMMOMMMOOMM
MMOMMMOMMMMMOMMOOMMMbT8bTSSSSSPd88PdOOOOMMMMOOMMMMMMMMOOMMM """.format(mensaje)
        return dialogo.format(mensaje)
    
    def game_over(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        game_over = """ 
        
        
        
        
        
                                                                                                                    
                                             ██████████████          ████████         ██████        █████    ████████████████████ 
                                             ███████████████        █████████         ██████        ██████   ████████████████████ 
                                          ███████                ███████  ██████      █████████  █████████   ██████
                                        █████████              █████████  █████████   ████████████████████   ██████ 
                                        ██████                 ██████        ██████   ████████████████████   ██████████████ 
                                        ██████     █████████   ██████        ██████   ████████████████████   ███████████████
                                        ██████     █████████   ████████████████████   ████████████████████   ███████
                                        ██████▓       ██████   ████████████████████   ██████  ████  ██████   ██████
                                          ▒██████     ██████   ██████        ██████   ██████        ██████   ██████                   
                                           █████████████████   ██████        ██████   ██████        ██████   ████████████████████
                                             ███████████████   ██████        ██████   ██████        ██████   ████████████████████    
                                                
                                                                                                                                                                                                                    
                                           █████████████       ██████        █████    ████████████████████   █████████████████
                                          ███████████████      ██████        ██████   ████████████████████   █████████████████
                                        ██████        ██████   ██████        ██████   ██████                 ██████       ███████ 
                                        ██████        ██████   ██████        ██████   ██████                 ██████       ███████
                                        ██████        ██████   ██████        ██████   ██████████████         ██████       ███████
                                        ██████        ██████   █████████  █████████   ███████████████        ██████     █████████ 
                                        ██████        ██████   ███████████████████    ██████████████         ███████████████████ 
                                        ██████        ██████     ███████████████      ██████                 ███████████████ 
                                        ██████        ██████        █████████         ██████                 ██████  █████████
                                        ███████████████████          ████████         ████████████████████   ██████  ████████████ 
                                          ███████████████              ████           ████████████████████   ██████     █████████ 
                                                                                                                                                    
        """
        print(game_over)
        exit()
        
    def __init__(self, nom):
        self.nom = nom
        self.vidas = 3
        self.codigo_caja_fuerte = ""
        self.intentos_caja_fuerte = 3
        self.decisiones = {
"inicio": {
    "mensaje": "Buenas tardes {} hemos estado viendo el banco central de Mexico y el de Buenos Aires, \n\t\t\t\t\t\tcreemos que tu eres la mejor opcion para esete atraco. De que mision quieres formar parte?(Mexico, Buenos Aires)".format(self.nom),
    "opciones": {
        "mexico": "Mexico",
        "buenos aires": "Buenos Aires"
    }
},
    "Mexico": {
        "mensaje": "Bienvenido a la mision de Mexico, en esta mision asaltaremos al banco central de Mexico. Para este tenemos opciones de atraco: \n\t\t\t\t\t\t\t- Cabar un tunel \n\t\t\t\t\t\t\t- Asalto a mano armada",
        "opciones": {
            "tunel":  "tunel",
            "mano": "mano"
        }
            },
        "tunel": {
            "mensaje": "Has elegido cabar un tunel, ahora puede que los caluclos fallen, puedes ver el mapa o seguir",
            "opciones": {
                "mapa": self.mapa,
                "seguir": "laverinto"
            }
            },
            
                "laverinto":{
                    "mensaje": "Es momento de iniciar el atraco, no sabemos con exactitud donde saldra el tunel asi que tienes que estar preparado para todo, escribe vamos",
                    "opciones": 
                    {
                        "vamos":  self.laverinto,
                        "seguir": "Camaras",
                    }
                },
                    "Camaras":{
                        "mensaje": "Hemos salido del laverinto, es hora de dirigirnos a la caja fuerte pero hay que pasar por desapercibido, por lo tanto intentaremos no ser vistos por las camaras, escribe adelante para continuar",
                        "opciones": 
                        {
                            "adelante": self.minijuego_0,
                            "seguir": "Desifrar",
                        }
                    },

                        "Desifrar":{
                            "mensaje": "Hemos pasado las cámaras de las oficinas, ahora para continuar con el atraco, debemos pasar por las cajas, el problema es que la puerta tiene un código que debemos descubrir escribe adivinar para acceder al proceso",
                            "opciones":
                            {
                                "adivinar": self.minijuego_1,
                                "seguir": "Cajas"
                            }
                        },

                            "Cajas": {
                                "mensaje": "Listo, has llegado a las cajas para continuar las tendrás que asaltar y conseguir dinero",
                                "opciones":
                                {
                                    "asaltar": self.minijuego_2,
                                    "seguir": "Donde"
                                }
                            },

                                "Donde": {
                                    "mensaje": "Has pasado la sección de cajas exitosamente, pero hay un problema, se te ha olvidado el mapa y no sabes a donde ir,\n\t\t\t\t\t\tno sabes si es a la izquierda, a la derecha, arriba o abajo, si viste el mapa al inicio esto será facil para ti.\n\t\t\t\t\t\tA donde te diriges?",
                                    "opciones":
                                    {
                                        "abajo": self.decifrar_caja_fuerte,
                                        "izquierda": self.perder_vida,
                                        "arriba": self.perder_vida,
                                        "derecha": self.perder_vida,
                                        "regresar": "Donde"
                                    }
                                },
        "mano": {
            "mensaje": "Haz elegido hacer el atraco a mano armada, por lo que se te asignara un sufusil, quieres ver el mapa antes de entrar o quieres seguir?",
            "opciones": {
                "mapa": self.mapa2,
                "seguir": "Atraco"
            }
        },

            "Atraco": {
                "mensaje": "Perfecto, has llegado por la entrada principal y disparas alteradamente hacía el techo para avisar que llegaste jeje,\n\t\t\t\t\t\t\tAhora te diriges a las cajas, escribe 'continuar'",
                "opciones":{
                    "continuar": self.minijuego_mano_0,
                    "seguir": "Pasillo"
                }
            },

                "Pasillo": {
                    "mensaje": "Excelente, después de sacar un poco de dinero ahora te encuentras en un pasillo lleno de cámaras y para llegar a la bóbeda a fuerzas tienes que pasar por el,\n\t\t\t\t\t\t\t escribe 'vamos' para avanzar por el pasillo",
                    "opciones":{
                        "vamos": self.minijuego_mano_1,
                        "avanzar": "Oficinas"
                    }
                },

                    "Oficinas":{
                        "mensaje": "Pasaste el pasillo exitosamente, ahora has llegado a las oficinas y hay un grupo de policias, en esta ocasión tendrás que dispararles, escribe 'disparar' para empezar el juego",
                        "opciones": {
                            "disparar": self.minijuego_mano_2,
                            "regresar": "Ejecutivo"
                        }
                    },

                        "Ejecutivo":{
                            "mensaje": "Felicidades, le has disparado a todos los policias, ahora vamos a la última sección para abrir la bóveda, escribe 'continuar'",
                            "opciones":{
                                "continuar": self.minijuego_mano_3,
                                "regresar": "BombaOculta"
                            }
                        },

                            "BombaOculta":{
                                "mensaje": "Excelente, ahora tienes que pasar la sección de seguridad para poder abrir la bóveda, escribe 'avanzar' para ir a la última sección",
                                "opciones":{
                                    "avanzar": self.minijuego_mano_4,
                                    "decifrar": self.decifrar_caja_fuerte
                                }
                            },

"Buenos Aires": {
    "mensaje": "Che {} bienvenido a la mision de atraco de Buenos Aires, para este atracto tenemos tres opciones: \n\t\t\t\t\t\t\t - Captura de rehenes \n\t\t\t\t\t\t\t - Hackea la base de datos".format(self.nom),
    "opciones": {
        "rehen":  "rehen",
        "hack": "hack"
    }
            },
        "rehen": {
            "mensaje": "Has decidido tomar rehenes, por lo que tendremos que actuar de manera rapida en un inicio, y despus resistir, para empezar ",
            "opciones": {
                "rehen":  "rehen",
                "hack": "hack"
    }
            },
        "hack": {
            "mensaje": "Has decidido la opcion de hackear la base de datos del banco, asi podremos recuperar datos y usarlso a tu favor ",
            "opciones": {
                "rehen":  "rehen",
                "hack": "hack"
    }
            },
            "fin": {
                "mensaje": "El juego ha terminado. ¿Quieres jugar de nuevo?",
                "opciones": {
                    "si": "inicio",
                    "no": None
                }
            }
        }
        self.estado_actual = "inicio"


    def mostrar_dialogo(self, mensaje, mostrar_art=True): #DUDA, QUE ES MOSTRAR_ART ?
        os.system('cls' if os.name == 'nt' else 'clear')
        if mostrar_art:
            print(self.dialogos(mensaje))
        else:
            print(mensaje)

    def jugar(self):
            decision = self.decisiones[self.estado_actual]
            self.mostrar_dialogo(decision["mensaje"])
            while True:
                respuesta = input().lower() 
                for opcion, estado in decision["opciones"].items():
                    if opcion in respuesta:
                        if callable(estado):  # Verifica si es una función antes de llamarla
                            estado()
                        else:
                            # Verifica y actualiza las vidas después de cada decisión
                            if "vidas" in decision: #PORQUE PONE VIDAS EN COMILLAS ?
                                self.vidas += decision["vidas"]
                            
                            # Verifica si se ha agotado el número de vidas
                            if self.vidas <= 0:
                                print("Has perdido todas tus vidas. ¡Fin del juego!")
                                self.estado_actual = None
                                print(self.game_over())
                                break
                            else: 
                                self.estado_actual = estado
                                decision = self.decisiones[self.estado_actual]
                                self.mostrar_dialogo(decision["mensaje"])

                        break
                if not self.estado_actual:
                    break
    
    def j(self):
        print("hola")
        
    def mapa2(self):
        print("Este será el mapa del banco, no te lo podras llevar por lo que te lo tienes que aprender")
        mapa = """
                                                                                                            
          ████████████████████████████████████████████████████████████████████████████████████████████            
          █ ██                             ███           █        █                               █               
          █ ██                             ███           █        █                               █               
          █ ██                             ███           █        █               █               █               
          █ ██                             ███           █        █               █               █               
          █ ██       Bobeda                ███           █        █               █               █            
          █ ██                             ███                                    █               █               
          █ ██                             ███             Cajas                  █              ██████████         
          █ ██                             ███                                    █                            
          █ ███████ ████████ █████████████████      ███████████████████████████████                Entrada                
          █ ██      ████████               ███                                  ███               principal                  
          █ ██      ████████               ███             Pasillo              ███                                   
          █ ██                             ███                                  ███              ██████████              
          █ ██                             ██████████████████████████████       ███████████████████████████               
          █ ██                                                █                                   █               
          █ ██        Seguridad                               █                                   █                
          █ ██                             ███                █                                   █
          █ ██                             ███    ejecutivo   █             oficinas              █        
          █ ██                             ███                █                                   █               
          █ ██                             ███                █                                   █               
          █ ██                             ███                                                    █               
          █████████████████████████████████████████████████████████████████████████████████████████                                                                          
        """
        print(mapa)
        print("Escribe seguir para avanzar")
    
    def mapa(self):
        print("Este será el mapa del banco, no te lo podras llevar por lo que te lo tienes que aprender")
        mapa = """
                                                                                                            
          ████████████████████████████████████████████████████████████████████████████████████████████            
          █ ██                             ███           █        █                               █               
          █ ██                             ███           █        █                               █               
          █ ██                             ███           █        █               █               █               
          █ ██                             ███           █        █               █               █               
          █ ██      #No se como ponerle                  █        █               █               █            
          █ ██                                                                    █               █               
          █ ██                             ███             cajas                  █              ██████████         
          █ ██                             ███                                    █                            
          █ ███████████████████████████████████████      ██████████████████████████                Entrada                
          █ ██                            █████████   Entrada                   ███                principal                  
          █ ██                            █████████    a la                     ███                                   
          █ ██                            █████████   bobeda                    ███              ██████████              
          █ ██                            ██████████████████████████████████████████      █████████               
          █ ██                             ███                █                                   █               
          █ ██           Bobeda            ███                █                                   █                
          █ ██                             ███                █                                   █
          █ ██                             ███    ejecutivo   █             oficinas              █        
          █ ██                             ███                █                                   █               
          █ ██                             ███                █                                   █               
          █ ██                             ███                                                    █               
          █████████████████████████████████████████████████████████████████████████████████████████                                                                          
        """
        print(mapa)
        print("Escribe seguir para avanzar")
        
    def laverinto(self):
        laverinto = """
           ██████████████████████████████████████████████████████████████████████████████           
           ██████████████████████████████████████████████████████████████████████████████           
           ███                      ███                                               ███           
           ███                      ███                                    k          ███           
           ███                      ███                                               ███           
           ███     ████████████     ███     █████████████████████████████     ███████████           
           ███             ████             ███                      ████     ███                   
           ███     p       ████    i    j   ███                      ████     ███    salida               
           ███             ████             ███                      ████     ███                   
           ████████████████████     ████████████████████████████     ████████████     ███           
           ████████████████████     ████████████████████████████     ████████████     ███           
           ███             ████                              ███                      ███           
           ███             ████    g                         ███  q                y  ███           
           ███             ████                           r  ███                      ███           
           ███     ███     ████     ████████████████████     ███     ████████████     ███           
           ███     ███     ████     ████████████████████     ███     ████████████     ███           
           ███     ███     ████     ███              ███     ███     ████     ███     ███           
           ███     ███     ████     ███              ███     ███     ████     ███     ███           
           ███     ████████████████████     ███      ███     ███     ████     ███     ███           
           ███     ████████████████████     ███      ███     ███     ████     ███     ███           
                                            ███      ███     ███     ████     ███     ███           
       Entrada   a               b          ███      ███     ███     ████     ███     ███           
                                            ███      ███     ███     ████     ███     ███           
           ████████████████████     ███████████      ███     ███     ████     ███████████           
           ████████████████████     ███████████      ███     ███     ████     ███████████           
           ███                      ███                      ███     ████             ███           
           ███                  c   ███           f          ███     ████          c  ███           
           ███      ██████████      ███████████      ███     ███     ███████████      ███           
           ███     ████████████     ███     ███      ███     ███     ████████████     ███           
           ███     ███              ███     ███      ███     ███              ███     ███           
           ███     ███              ███     ███      ███     ███              ███     ███           
           ███     ███              ███     ███      ███     ███              ███     ███           
           ███  h  ████████████████████     ███      ████████████████████     ███     ███           
           ███     ████████████████████     ███      ████████████████████     ███     ███           
           ███     ███              ███     ███                               ███     ███           
           ███     ███              ███     ███                             m ███     ███           
           ███     ███              ███     ███                               ███     ███           
           ███     ████████████     ███     █████████████████████████████     ███     ███           
           ███                                               ███                      ███           
           ███                   d        e                  ███                      ███           
           ███                                               ███                      ███           
           ██████████████████████████████████████████████████████████████████████████████           
           ██████████████████████████████████████████████████████████████████████████████ 
        """
        print(laverinto)
        print("Has salido por la oficinas, pero te has quedado atorado, es momento de salir")
        print("Escribe la letra a la que te quieres dirigir")
        print("Intentos restantes:", self.vidas)
        c = input("Inicias en 'a' a donde vas?")
        if self.vidas -1 > 0:
            if c  == "b":
                    d = input("Estas en 'b' a donde vas?")
                    if d == "f":
                            e = input("Estas en 'f' a donde vas?")
                            if e == "m":
                                    f = input("Estas en 'm' a donde vas?")
                                    if f == "q":
                                            g = input("Estas en 'q' a donde vas?")
                                            if g == "y":
                                                print("Has salido de las oficinas Felicidades, escribe seguir par continuar")
                                                x = random.randint(0,9)
                                                print("El número de esta sección es el:", x)
                                                self.codigo_caja_fuerte += x
                                            else:
                                                self.vidas -= 1
                                                print("Intentalo una vez mas")
                                                self.laverinto()
                                    else:
                                            self.vidas -= 1
                                            print("Intentalo una vez mas")
                                            self.laverinto()
                            else:
                                    self.vidas -= 1
                                    print("Intentalo una vez mas")
                                    self.laverinto()
                    else:
                            self.vidas -= 1
                            print("Intentalo una vez mas")
                            self.laverinto()
            else: 
                    self.vidas -= 1
                    print("Intentalo una vez mas")
                    self.laverinto()          
        else:
            self.game_over()
        

    def perder_vida(self):
        self.vidas -= 1
        print("Perdiste una vida, te quedan:", self.vidas, "escribe 'regresar'")
    
    def minijuego_0(self):
        print("\nLlegaste a un pasillo donde hay cámaras que cambian de lado cada 2 segundos, primero apuntan\na la izquierda y luego a la derecha pero si te pones abajo de la cámara la evitarás")
        print("\nInstrucciones: Tendrás que escribir el número de pasos exactos para estar debajo de la cámara para que así no te vea")
        print("\nEjemplo: La camara esta apuntando a la izquierda, tu tendrás que escribir la palabra 'esperar' de lo contrario la cámara de verá,\n         después de 2 segundos la cámara apuntará a la derecha y es entonces cuando podrás moverte.")
        print("         Si la camara apuntaba en un rango de 1 - 5 darás entonces 6 pasos para quedar abajo y cuando la cámara apunte de nuevo a la \n         izquierda ya podrás moverte, pero ten en cuenta los pasos que darás porque después de una cámara sigue otra")
        print("\nTienes 3 intentos, si no pierdes una vida")
        game = Juego(None)
        a = self.vidas
        class ej():
            def __init__(self):
                self.vidas = a
                self.intentos = 3
            def caso_base(self):
                ini = 1
                fin = random.randint(2,10)
                ini2 = fin + 2
                fin2 = random.randint(ini2+1, ini2+11)
                
                ini3 = fin2 + 1
                fin3 = random.randint(ini3+1, ini3+11)

                ini4 = fin3 + 2
                fin4 = random.randint(ini4+1, ini4+11)
                return ini, fin, ini2, fin2, ini3, fin3, ini4, fin4

            def case1(self,a, b, ini, fin, ini4, fin4):
                print("-->La camara", a, "apunta a la izquierda con un rango de: ", ini, "-", fin)
                print("-->La camara", b, "apunta a la derecha con un rango de:", ini4, "-", fin4)
                respuesta = input("Si vas a avanzar escribe el número de pasos, de lo contrario escribe 'esperar': ")
                if respuesta != 'esperar': 
                    if int(respuesta) > fin3 and int(respuesta) < ini4:
                        print("\nListo, avanzaste", respuesta, "pasos")
                        print("{ Te encuentras abajo de la cámara", b, "}")
                    else:
                        self.intentos -= 1
                        if self.intentos == 0:
                            print("Ya fueron 3 intentos, debes continuar, pero perderás una vida,\nTus vidas:", self.vidas-1)
                            self.vidas -= 1
                            if self.vidas == 0:
                                game.game_over()
                            self.intentos = 3
                        else: 
                            print("¡¡¡La cámara te vio, te quedan", self.intentos, "oportunidades para no perder vidas!!!")
                        print("Vuelve a intentarlo, sigues abajo de la cámara", a)
                        self.case1(a, b, ini, fin, ini4, fin4)
                elif respuesta == 'esperar':
                    print("Bien, ahora espera a que giren las cámaras para poder avanzar")
                    time.sleep(3)
                    print()
                    print("Listo, las camaras han cambiado")

            def case2(self, a, b, ini2, fin2, ini3, fin3):
                print("-->La camara", a, "apunta a la derecha con un rango de:", ini2, "-", fin2)
                print("-->La camara", b, "apunta a la izquierda con un rango de:", ini3, "-", fin3)
                respuesta = input("Si vas a avanzar escribe el número de pasos, de lo contrario escribe 'esperar': ")
                if respuesta != 'esperar':
                    if int(respuesta) > fin and int(respuesta) < ini2:
                        print("\nListo, avanzaste", respuesta, "pasos")
                        print("{ Te encuentras abajo de la camara", a, "}")
                    else:
                        self.intentos -= 1
                        if self.intentos == 0:
                            print("Ya fueron 3 intentos, debes continuar, pero perderás una vida,\nTus vidas:", self.vidas-1)
                            self.vidas -= 1
                            if self.vidas == 0:
                                game.game_over()
                            self.intentos = 3
                        else:
                            print("¡¡¡La cámara te vio, te quedan,", self.intentos, "oportunidades para no perder vidas!!!")
                        print("Vuelve a intentarlo, sigues abajo de la cámara", b)
                        self.case2(a, b, ini2, fin2, ini3, fin3)
                elif respuesta == 'esperar':
                    print("Bien, ahora espera a que giren las cámaras para poder avanzar")
                    time.sleep(3)
                    print()
                    print("Listo, las camaras han cambiado")
            
            def case4(self, b):
                print("La camara", b, "apunta a la izquierda")
                a = input("Escribe 'seguir' para continuar")

        ob = ej()
        ini, fin, ini2, fin2, ini3, fin3, ini4, fin4 = ob.caso_base()
        print("{Te encuentras al inicio del pasillo}")
        a = 1
        b = 2
        s = 0
        while(self.vidas > 0):
            ob.case1(a,b,ini, fin, ini4, fin4)
            ob.case2(a,b,ini2, fin2, ini3, fin3)
            ob.case1(a,b,ini, fin, ini4, fin4)
            ini, fin, ini2, fin2, ini3, fin3, ini4, fin4 = ob.caso_base()
            s+= 1
            if s == 4:
                ob.case4(b)
                break
            a += 1
            b += 1
        print("Felicidadeeees")
        x = random.randint(0,9)
        print("El número de esta sección es el:", x)
        self.codigo_caja_fuerte += x

    def minijuego_1(self):
        print("Instrucciones: Para saber que código es el correcto tendrás que adivinar en cual de las 6 cajas se encuentra el número")
        print("Pista: son 5 digitos y si su posicion es imparpar se encuentra en una caja de posicion impar, lo mismo para posiciones pares")
        print("Ejemplos: el tercer digito podría encontrarse en la caja 1, 3 o 5")

        cajas = """
                ████████      ████████      ████████    
                ██  1 ██      ██  2 ██      ██  3 ██
                ████████      ████████      ████████

                ████████      ████████      ████████    
                ██  4 ██      ██  5 ██      ██  6 ██
                ████████      ████████      ████████
                """
        lista = ""
        for i in range(1, 6):
            print(cajas)
            x = random.randint(0, 9)
            lista += str(x)
            if i % 2 != 0:
                y = random.randrange(1, 6, 2)
                #print(y)
                a = 0
                while a != y:
                    a = input("En que caja crees que esté el dígito? ")
                    if int(a) == y:
                        print("El digito", i, "es:", x)
                        break
            else:
                y = random.randrange(2, 7, 2)
                #print(y)
                a = 0
                while a != y:
                    a = input("En que caja crees que esté el dígito?")
                    if int(a) == y:
                        print("El digito", i, "es:", x)
                        break
            input("Presiona enter después de que anotes o te memorices el dígito")
            os.system('cls' if os.name == 'nt' else 'clear')
        p = input("Escribe el número que econtraste en las cajas: ")
        if p == lista:
            print("Felicidadeeeees")
        else:
            print("SE ACTIVÓ LA ALARMA Y ALERTASTE A LOS POLICIAS...")
            time.sleep(2)
            self.game_over()
        #print(lista)       
        print("Escribe 'seguir' para continuar con la misión")
        x = random.randint(0,9)
        print("El número de esta sección es el:", x)
        self.codigo_caja_fuerte += x

    def minijuego_2(self):
        duracion_ciclo = 20

        print("Listo, ahora vas a asaltar las cajas")
        print("Instrucciones: Se te daran palabras, y tu tendras que escribirlas, si te equivocas en una palabra no importa, puedes continuar con la siguiente palabra mientras no se te acabe el tiempo")
        print("Entre más palabras escribas más dinero obtendrás")

        class Temporizador(threading.Thread):
            def __init__(self, duracion):
                super().__init__()
                self.duracion = duracion
                self.terminado = threading.Event()

            def run(self):
                time.sleep(self.duracion)
                self.terminado.set()

        class Lector(threading.Thread):
            def __init__(self):
                super().__init__()
                self.palabra = ""
                self.respuesta = None
                self.contador = 0

            def run(self):
                while not temporizador.terminado.is_set():
                    for _ in range(7):
                        x = random.randint(97, 122)
                        letra = chr(x)
                        self.palabra += letra
                    print("Escribe la palabra:", self.palabra)
                    self.respuesta = input()
                    if self.respuesta.lower() == self.palabra:
                        self.contador += 1
                        print("Bieeeeen")
                    else:
                        tiempo = int(duracion_ciclo - (time.time() - tiempo_inicio))
                        if tiempo >= 0:
                            print("Palabra incorrecta\t Te quedan:", tiempo, "segundos")
                    self.respuesta = None
                    self.palabra = ""

        temporizador = Temporizador(duracion_ciclo)
        lector = Lector()

        inpu = 'a'
        while inpu != 's':
            inpu = input("Para comenzar presiona la letra s\n")
            if inpu == 's':
                temporizador.start()
                lector.start()
                tiempo_inicio = time.time()

        while not temporizador.terminado.is_set():
            continue

        if temporizador.terminado.is_set():
            print()
            print("Se acabó el tiempo")
        dinero_robado = lector.contador * 19999
        print("Lograste robar $", dinero_robado)
        print("Escribe 'seguir' para continuar el asalto")
        x = random.randint(0,9)
        print("El número de esta sección es el:", x)
        self.codigo_caja_fuerte += x

    def decifrar_caja_fuerte(self):
        def botton_1():
            x = int(label1.cget("text")) + 1
            if x == 10:
                x = 0
            x = str(x)
            label1.config(text=x)
        def botton_2():
            x = int(label2.cget("text")) + 1
            if x == 10:
                x = 0
            x = str(x)
            label2.config(text=x)
        def botton_3():
            x = int(label3.cget("text")) + 1
            if x == 10:
                x = 0
            x = str(x)
            label3.config(text=x)
        def botton_4():
            x = int(label4.cget("text")) + 1
            if x == 10:
                x = 0
            x = str(x)
            label4.config(text=x)
        def botton_5():
            x = int(label1.cget("text"))
            if x == 0:
                x = 9
            else:
                x -= 1
            x = str(x)
            label1.config(text=x)
        def botton_6():
            x = int(label2.cget("text"))
            if x == 0:
                x = 9
            else:
                x -= 1
            x = str(x)
            label2.config(text=x)
        def botton_7():
            x = int(label3.cget("text"))
            if x == 0:
                x = 9
            else:
                x -= 1
            x = str(x)
            label3.config(text=x)
        def botton_8():
            x = int(label4.cget("text"))
            if x == 0:
                x = 9
            else:
                x -= 1
            x = str(x)
            label4.config(text=x)

        def botton_9():
            numero = ""
            numero += label1.cget("text")
            numero += label2.cget("text")
            numero += label3.cget("text")
            numero += label4.cget("text")
            if numero == self.codigo_caja_fuerte:
                print("Felicidaaaaadeeeeees!!!!!!, Lograste entrar a la caja fuerte")
                print("Fin del juego")
                exit()
            else:
                if self.intentos_caja_fuerte > 0:
                    print("Ese no es el número, te quedan", self.intentos_caja_fuerte, "más")
                    self.decifrar_caja_fuerte()
                else:
                    print("Se acabaron tus intentos")
                    self.game_over()

        # Crear la ventana principal
        ventana = tk.Tk()
        ventana.title("")

        contenedor0 = tk.Frame(ventana)
        contenedor0.pack(expand=True)

        # Crear un botón
        button1 = tk.Button(contenedor0, text="^", command=botton_1)
        button1.grid(row=0, column=0, padx=25, pady=20)

        button2 = tk.Button(contenedor0, text="^", command=botton_2)
        button2.grid(row=0, column=1, padx=25, pady=20)

        button3 = tk.Button(contenedor0, text="^", command=botton_3)
        button3.grid(row=0, column=2, padx=25, pady=20)

        button4 = tk.Button(contenedor0, text="^", command=botton_4)
        button4.grid(row=0, column=3, padx=25, pady=20)


        contenedor1 = tk.Frame(ventana)
        contenedor1.pack(expand=True)

        # Crear un etiqueta
        label1 = tk.Label(contenedor1, text="0")
        label1.grid(row=0, column=0, padx=28, pady=20)

        label2 = tk.Label(contenedor1, text="0")
        label2.grid(row=0, column=1, padx=28, pady=20)

        label3 = tk.Label(contenedor1, text="0")
        label3.grid(row=0, column=2, padx=28, pady=20)

        label4 = tk.Label(contenedor1, text="0")
        label4.grid(row=0, column=3, padx=28, pady=20)

        contenedor2 = tk.Frame(ventana)
        contenedor2.pack(expand=True)

        # Crear un botón
        button5 = tk.Button(contenedor2, text="v", command=botton_5)
        button5.grid(row=0, column=0, padx=25, pady=20)

        button6 = tk.Button(contenedor2, text="v", command=botton_6)
        button6.grid(row=0, column=1, padx=25, pady=20)

        button7 = tk.Button(contenedor2, text="v", command=botton_7)
        button7.grid(row=0, column=2, padx=25, pady=20)

        button8 = tk.Button(contenedor2, text="v", command=botton_8)
        button8.grid(row=0, column=3, padx=25, pady=20)

        contenedor3 = tk.Frame(ventana)
        contenedor3.pack(expand=True)

        botton9 = tk.Button(contenedor3, text="Aceptar", command=botton_9)
        botton9.grid(row=0, column=3, padx=25, pady=20)

        # Iniciar el bucle principal de la interfaz gráfica
        ventana.mainloop()





    def minijuego_mano_0(self):
        class ClickGame:
            def __init__(self, ventana):
                self.ventana = ventana
                self.ventana.title("Click Game")

                self.label = tk.Label(ventana, text="Haz clic en el botón")
                self.label.pack(pady=10)

                self.button = tk.Button(ventana, text="¡Clic aquí!", command=self.on_button_click)
                self.button.pack(pady=20)

                self.click_count = 0
                self.start_time = None
                self.click_count2 = 0
                self.start_time2 = None

            def on_button_click(self):
                if self.start_time is None:
                    self.start_time = time.time()
                    self.ventana.after(10000, self.change_botton)  # Juego de 10 segundos
                self.click_count += 1
            
            def change_botton(self):
                self.button.config(state=tk.DISABLED)  
                self.button2 = tk.Button(ventana, text="¡Clic aquí!", command=self.on_button_click)
                self.button2.pack(padx = 30, pady=20)
                if self.start_time2 is None:
                    self.start_time2 = time.time() 
                    self.ventana.after(10000, self.end_game)  # Juego de 10 segundos
                self.click_count2 += 1

            def end_game(self):
                cps = self.click_count + self.click_count2  # Clics por segundo
                self.label.config(text= "Fin del juego\nClics totales: " + str(cps))
                self.button2.config(state=tk.DISABLED)  # Desactivar el botón después del juego
                print("Felicidades, pasaste las cajas y robaste $", cps*1999)

        if __name__ == "__main__":
            ventana = tk.Tk()
            game = ClickGame(ventana)
            ventana.mainloop()
        print("Escribe 'seguir' para continuar")
        x = random.randint(0,9)
        print("El número de esta sección es el:", x)
        self.codigo_caja_fuerte += x


    def mover_jugador(self, posicion_jugador, pasos):
        return posicion_jugador + pasos

    def detectar_camara(self, posiciones_camaras, posicion_jugador):
        for posicion_camara in posiciones_camaras:
            if posicion_camara in range(posicion_jugador, posicion_jugador + 1 ):
                return True
        return False

    def minijuego_mano_1(self):
        posicion_jugador = 0
        rango_vision = 10
        pasos_totales = 0
        contador_multiplo = 5
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("\n\nHas logrado pasar por cajas, pero se acerca el pasillo donde hay mayor vigilancia, vas a tener que escabar de las camaras de suguridad")
        print("\tPara ello hemos tomado un registro de la ubicacion de las camaras de suguridad, y hemos notado que tienen un patron ")
        print("\tla primer camara se encuentra a un rango de 2 pasos, te iremos dando la informacion conforme vayas avanzando")
        print("\t¡Cuidado! si te detectan te atraparan y perderas una vida en el juego\n\n")
        
        while True:
            posiciones_camaras = list(range(0, 20, 2)) + list(range(20, 38, 3)) + list(range(38, 63, 5)) + list(range(63, 85, 7))
            
            pasos = int(input("¿Cuántos pasos quieres moverte? "))
            posicion_jugador = self.mover_jugador(posicion_jugador, pasos)
            pasos_totales += pasos
            
            if self.detectar_camara(posiciones_camaras, posicion_jugador):
                print("¡Has sido atrapado por una cámara de seguridad!")
                self.vidas -= 1
                self.game_over()
                return    
                
            if pasos < 20:
                print("Sigues en un rango de camara por cada dos pasos")
            elif pasos > 20 and pasos < 38:
                print("Ahora estas en un rango de camara por cada tres pasos")
            elif pasos > 38 and pasos < 63:
                print("Ahora estas en un rango de camara por cada cinco pasos")
            elif pasos > 63 and pasos < 84:
                print("Ahora estas en un rango de camara por cada siete pasos")

            if pasos_totales >= 80:
                print("¡Felicidades! Has dado 100 pasos sin ser atrapado por una cámara de seguridad.")
                print("Escribe 'avanzar' para continuar")
                x = random.randint(0,9)
                print("El número de esta sección es el:", x)
                self.codigo_caja_fuerte += x
                return


    def minijuego_mano_2(self):
        print("Has entrado a un minijuego\n En esta ocasión entraras en combate con un grupo de policias")
        print("Instrucciones: Oprime la letra que aparezca en pantalla para dispararle, si te equivocas él te disparará y te quitara vida")
        print("Comencemos...")
        time.sleep(7)
        vida_oponente = 10
        while vida_oponente > 0 and self.vidas > 0:
            x = chr(random.randint(97, 122))
            print(x)
            a = input("Dispara ")
            if a == x:
                vida_oponente -= 1
            else:
                self.vidas -= 1
        if self.vidas > 0:
            print("Felicidades!!!")
            print("Haz completado la prueba, escribe 'regresar' para continuar")
            print("Vidas: ", self.vidas)
            x = random.randint(0,9)
            print("El número de esta sección es el:", x)
            self.codigo_caja_fuerte += x
        else:
            print("Lo siento, tus vidas se han acabado")
            self.game_over()


    def minijuego_mano_3(self):
        print("ALV!!!!(hasta la vista) atrás de ti sigue un policia vivo")
        print("Tendrás esquivar las balas para continuar a la siguiente sección")
        print("Instrucciones: Muevete al lado contrario de donde venga la bala, por ejemplo: si la bala viene a la derecha muevete a la izquierda")
        print("Teclas: \nW:Saltar\nA:Izquierda\nS:Agacharse:\nD:Derecha")
        print("Comencemos")
        i = 0
        while i < 10 and self.vidas > 0:
            x = random.randint(1, 4)
            if x == 1:
                i += 1
                movida = input("La bala viene ARRIBA ")
                movida.lower()
                if movida == 's':
                    continue
                else:
                    print('/' * self.vidas, '-->', '/' * (self.vidas - 1))
                    self.vidas -= 1
            elif x == 2:
                i += 1
                movida = input("La bala viene a la IZQUIERDA ")
                print()
                movida.lower()
                if movida == 'd':
                    continue
                else:
                    print('/' * self.vidas, '-->', '/' * (self.vidas - 1))
                    self.vidas -= 1
            elif x == 3:
                i += 1
                movida = input("La bala viene ABAJO ")
                print()
                movida.lower()
                if movida == 'w':
                    continue
                else:
                    print('/' * self.vidas, '-->', '/' * (self.vidas - 1))
                    self.vidas -= 1
            else:
                i += 1
                movida = input("La bala viene a la DERECHA ")
                print()
                movida.lower()
                if movida == 'a':
                    continue
                else:
                    print('/' * self.vidas, '-->', '/' * (self.vidas - 1))
                    self.vidas -= 1
        if self.vidas > 0:
            print("Felicidades!!!")
            print("Haz completado la prueba, escribe 'regresar' para continuar")
            x = random.randint(0,9)
            print("El número de esta sección es el:", x)
            self.codigo_caja_fuerte += x
        else:
            print("Lo siento, tus vidas se han acabado")
            self.game_over()


    def minijuego_mano_4(self):
        duracion_ciclo = 40
        codigos = []
        diccionario = {'A': '1000', 'B': '1100', 'C': '1110', 'D': '1111', 'E': '0100', 'F': '0110', 'G': '0111', 'H': '0010', 'I': '0011', 'J': '0000', 'K': '1001', 'L': '1010', 'M': '0101', 'N': '0001', 'O': '1101', 'P': '1011'}
        print("ADVERTENCIA !!! \nSe te olvidó que la sección de seguriadad tiene cámaras, te vieron y se activo una bomba, tienes que desactivar la bomba en menos de 40 segundos")
        print("Instrucciones: Se te dara una secuencia de codigos, tu tendras que ver que letra le corresponde a cada código con el siguiente diccionario")

        #Imprime el diccionario
        for key, value in islice(diccionario.items(), 16):
            print(f'{key}: {value}')

        #Crea 10 codigos de 4 digitos cada uno
        for i in range(10):
            codigo = ""
            for _ in range(4):
                x = random.randint(0,1)
                codigo += str(x) 
            codigos.append(codigo)
        #La computadora mapea la palabra según los códigos anteriores y el diccionario
        aux = ""
        for i in range (10):
            for clave, valor in diccionario.items():
                if codigos[i] == valor:
                    aux += str(clave)
        print(aux.lower())

        class Temporizador(threading.Thread):
            def __init__(self, duracion):
                super().__init__()
                self.duracion = duracion
                self.terminado = threading.Event()

            def run(self):
                time.sleep(self.duracion)
                self.terminado.set()

        class Lector(threading.Thread):
            def __init__(self):
                super().__init__()
                self.palabra = None
                self.detener = threading.Event()

            def run(self):
                while not self.detener.is_set() and not temporizador.terminado.is_set():
                    self.palabra = input("Escribe tu palabra: ")
                    if self.palabra.lower() == aux.lower():
                        self.detener.set()
                        temporizador.terminado.set()
                        print("FELICIDADES!!!!!\nEspera unos segundos...")

        temporizador = Temporizador(duracion_ciclo)
        lector = Lector()
        inpu = 'a'
        while inpu != 's':
            inpu = input("Para comenzar presiona la letra s\n")
            if inpu == 's':
                print(codigos)
                temporizador.start()
                lector.start()
                tiempo_inicio = time.time()

        while not temporizador.terminado.is_set():
            if lector.palabra is not None:
                if lector.palabra.lower() != aux.lower():
                    tiempo = int(duracion_ciclo - (time.time() - tiempo_inicio))
                    print("Palabra incorrecta\t Te quedan:", tiempo, "segundos")
                    lector.palabra = None

        if temporizador.terminado.is_set() and not lector.detener.is_set():
            print()
            print("Se acabó el tiempo")
            lector.detener.set()
            self.game_over()
        #OJO AQUI
        x = random.randint(0,9)
        print("El número de esta sección es el:", x)
        self.codigo_caja_fuerte += x
        print("Excelente, has pasado todas las pruebas ahora solo escribe 'decifrar' para llegar a la bóveda y decifrar el código") #OJO AQUI


    def decifrar_caja_fuerte_mano(self):
        def botton_1():
            x = int(label1.cget("text")) + 1
            if x == 10:
                x = 0
            x = str(x)
            label1.config(text=x)
        def botton_2():
            x = int(label2.cget("text")) + 1
            if x == 10:
                x = 0
            x = str(x)
            label2.config(text=x)
        def botton_3():
            x = int(label3.cget("text")) + 1
            if x == 10:
                x = 0
            x = str(x)
            label3.config(text=x)
        def botton_4():
            x = int(label4.cget("text")) + 1
            if x == 10:
                x = 0
            x = str(x)
            label4.config(text=x)
        def botton_5():
            x = int(label1.cget("text"))
            if x == 0:
                x = 9
            else:
                x -= 1
            x = str(x)
            label1.config(text=x)
        def botton_6():
            x = int(label2.cget("text"))
            if x == 0:
                x = 9
            else:
                x -= 1
            x = str(x)
            label2.config(text=x)
        def botton_7():
            x = int(label3.cget("text"))
            if x == 0:
                x = 9
            else:
                x -= 1
            x = str(x)
            label3.config(text=x)
        def botton_8():
            x = int(label4.cget("text"))
            if x == 0:
                x = 9
            else:
                x -= 1
            x = str(x)
            label4.config(text=x)

        def botton_9():
            numero = ""
            numero += label1.cget("text")
            numero += label2.cget("text")
            numero += label3.cget("text")
            numero += label4.cget("text")
            if numero == self.codigo_caja_fuerte:
                print("Felicidaaaaadeeeeees!!!!!!, Lograste entrar a la caja fuerte")
                print("Fin del juego")
                time.sleep(3)
                self.minijuego_mano_5
            else:
                if self.intentos_caja_fuerte > 0:
                    print("Ese no es el número, te quedan", self.intentos_caja_fuerte, "más")
                    self.decifrar_caja_fuerte()
                else:
                    print("Se acabaron tus intentos")
                    self.game_over()

        # Crear la ventana principal
        ventana = tk.Tk()
        ventana.title("")

        contenedor0 = tk.Frame(ventana)
        contenedor0.pack(expand=True)

        # Crear un botón
        button1 = tk.Button(contenedor0, text="^", command=botton_1)
        button1.grid(row=0, column=0, padx=25, pady=20)

        button2 = tk.Button(contenedor0, text="^", command=botton_2)
        button2.grid(row=0, column=1, padx=25, pady=20)

        button3 = tk.Button(contenedor0, text="^", command=botton_3)
        button3.grid(row=0, column=2, padx=25, pady=20)

        button4 = tk.Button(contenedor0, text="^", command=botton_4)
        button4.grid(row=0, column=3, padx=25, pady=20)


        contenedor1 = tk.Frame(ventana)
        contenedor1.pack(expand=True)

        # Crear un etiqueta
        label1 = tk.Label(contenedor1, text="0")
        label1.grid(row=0, column=0, padx=28, pady=20)

        label2 = tk.Label(contenedor1, text="0")
        label2.grid(row=0, column=1, padx=28, pady=20)

        label3 = tk.Label(contenedor1, text="0")
        label3.grid(row=0, column=2, padx=28, pady=20)

        label4 = tk.Label(contenedor1, text="0")
        label4.grid(row=0, column=3, padx=28, pady=20)

        contenedor2 = tk.Frame(ventana)
        contenedor2.pack(expand=True)

        # Crear un botón
        button5 = tk.Button(contenedor2, text="v", command=botton_5)
        button5.grid(row=0, column=0, padx=25, pady=20)

        button6 = tk.Button(contenedor2, text="v", command=botton_6)
        button6.grid(row=0, column=1, padx=25, pady=20)

        button7 = tk.Button(contenedor2, text="v", command=botton_7)
        button7.grid(row=0, column=2, padx=25, pady=20)

        button8 = tk.Button(contenedor2, text="v", command=botton_8)
        button8.grid(row=0, column=3, padx=25, pady=20)

        contenedor3 = tk.Frame(ventana)
        contenedor3.pack(expand=True)

        botton9 = tk.Button(contenedor3, text="Aceptar", command=botton_9)
        botton9.grid(row=0, column=3, padx=25, pady=20)

        # Iniciar el bucle principal de la interfaz gráfica
        ventana.mainloop()


    def minijuego_mano_5(self):
        print("AUN NO GANAS, TE HAN ATRAPADOOOO!")
        print("Para escapar escribe un número del 1 al 7, generaremos un número al azar, si coincide con el tuyo PIERDES si no coincide GANARAS")
        a = input("Escribe tu numero: ")
        x = random.randint(1, 7)
    
        if x == a:
            print("Lo siento, perdiste")
            self.game_over()
        else:
            print("Ufff, por poco pierdes, ahora si GANASTE")
        
nom = input("Ingresa tu nombre: ")
print("Cargando...")
time.sleep(2) 
os.system('cls' if os.name == 'nt' else 'clear')
juego = Juego(nom)
juego.jugar()
