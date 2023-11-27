import os
import time
import random
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
            "mensaje": "Has elegido cabar un tunel, ahora puede que los caluclos fallen, puedes ver el mapa o seguir, puedes ver mapa o seguir",
            "opciones": {
                "mapa": self.mapa,
                "seguir": "laverinto"
            }
            },
            
                    "laverinto":{
                        "mensaje": "Es momento de iniciar el atraco, no sabemos con exactitud donde saldra el tunel asi que tienes que estar preparado para todo, escribe vamos ",
                        "opciones": 
                        {
                            "vamos":  self.laverinto,
                            "seguir": "donde",
                        }
                    },
                    "donde":{
                        "mensaje": "Hemos salido del laverinto, es hora de dirigirnos a la caja fuerte pero hay que pasar por desapercibido, hay eu intenttar no ser vistos por las camaras, escribe adelante para poder seguir",
                        "opciones": 
                        {
                            "adelante": "polla",
                            "ejecutivo": "Esconder",
                        }
                    },
                    "Golpear":{
                        "mensajeje":"Listo ya tienes un policia menos, que te esta",
                        "opciones": 
                        {
                            "disparar": "Disparar",
                            "esconderme": "Esconder",
                            "golpear": "Golpear",
                        }
                    },

        "mano": {
            "mensaje": "Haz elegido hacer el atraco a mano armada, por lo que se te asignara un sufusil ",
            "opciones": {
                "toma": "fin",
                "deja": "inicio"
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


    def mostrar_dialogo(self, mensaje, mostrar_art=True):
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
                            if "vidas" in decision:
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
        
    def mapa(self):
        print("Este será el mapa del banco, no te lo podras llevar por lo que te lo tienes que aprender")
        mapa = """
                                                                                                            
          ████████████████████████████████████████████████████████████████████████████████████████████            
          █ ██                             ███           █        █               █               █               
          █ ██                             ███           █        █               █               █               
          █ ██                             ███           █        █               █               █               
          █ ██                             ███           █        █               █               █               
          █ ██                             ███           █        █               █               █               
          █ ██                             ███                                    █               █               
          █ ██                             ███             cajas                  █           ██████████         
          █ ██                             ███                                    █                            
          █ ██                            ████████████████████                  ███            Entrada                
          █ ██                            █████████   Entrada                                 principal                  
          █ ██          Bobeda            █████████    a la                                                        
          █ ██                            █████████   bobeda                                  ██████████              
          █ ██                            █████████████████████      ███████████████████████      █               
          █ ██                             ███                █                                   █               
          █ ██                             ███                █                                   █                
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
           ███             ████    i    j   ███                      ████     ███    salida               
           ███             ████             ███                      ████     ███                   
           ████████████████████     ████████████████████████████     ████████████     ███           
           ████████████████████     ████████████████████████████     ████████████     ███           
           ███             ████                              ███                      ███           
           ███             ████    g                         ███  n                l  ███           
           ███             ████                              ███                      ███           
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
           ███                  c   ███           f          ███     ████             ███           
           ███      ██████████      ███████████      ███     ███     ███████████      ███           
           ███     ████████████     ███     ███      ███     ███     ████████████     ███           
           ███     ███              ███     ███      ███     ███              ███     ███           
           ███     ███              ███     ███      ███     ███              ███     ███           
           ███     ███              ███     ███      ███     ███              ███     ███           
           ███     ████████████████████     ███      ████████████████████     ███     ███           
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
        print("tendras que poner a para arriba, d para derecha, h para ir abajo e i para ir a la   izquierda ")
        c = input("Inicias en 'a' a donde vas?")
        if self.vidas > 0:
            if c  == "d":
                    d = input("Estas en 'b' a donde vas?")
                    if d == "d":
                            e = input("Estas en 'f' a donde vas?")
                            if e == "h":
                                    f = input("Estas en 'm' a donde vas?")
                                    if f == "a":
                                            g = input("Estas en 'n' a donde vas?")
                                            if g == "d":
                                                    h = input("Estas en 'l' a donde vas?")
                                                    if h == "a":
                                                        print("has salido de las oficinas Felicidades, escribe seguir par continuar") 
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
        

    def j2(self):
        print("TE HAN ATRAPADOOOO!")
        print("Para escapar escribe un número del 1 al 7, generaremos un número al azar, si coincide con el tuyo PIERDES si no coincide GANARAS")
        a = input("Escribe tu numero: ")
        x = random.randint(1, 7)
    
        if x == a:
            print("Lo siento, perdiste")
        else:
            print("Ufff, por poco pierdes, escribe 'regresar' para continuar")
            
            
    def j3(self):
        print("Has entrado a un minijuego\n En esta ocasión entraras en combate con un policia")
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
        else:
            print("Lo siento, tus vidas se han acabado")
            #Que te mande al GAME OVER   
            
        
        
nom = input("Ingresa tu nombre: ")
print("Cargando...")
time.sleep(2) 
os.system('cls' if os.name == 'nt' else 'clear')
juego = Juego(nom)
juego.jugar()
