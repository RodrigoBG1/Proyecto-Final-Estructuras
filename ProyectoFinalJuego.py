import os
import time
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
        
        
dialogos = """
                    dS$$S$S$S$S$S$S$$Sb                    
                   :$$S^S$S$S$S$S$S^S$$;                   
                   SSP   `^$S$S$^'   TSS                   
                   $$       `"'       $$                   
                  _SS ,-           -  SS_      ___________________________________            
                 :-.|  _    - .-   _  |.-;    |                                   |
                 :\(; ' "-._.'._.-" ` |)/;    |                                   |
                  \`|  , o       o .  |'/     |                                   |
                   ":     -'   `-     ;"      |                                   |
                     ;.              :        |                                   |
                     : `    ._.    ' ;       /____________________________________|            
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
MMOMMMOMMMMMOMMOOMMMbT8bTSSSSSPd88PdOOOOMMMMOOMMMMMMMMOOMMM """

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
        return dialogo
        
        
    def __init__(self, nom):
        self.nom = nom
        self.decisiones = {
            "inicio": {
                "mensaje": "Buenas tardes {} hemos estado viendo el banco central de Mexico y el de Buenos Aires, \n\t\t\t\t\t\tcreemos que tu eres la mejor opcion para esete atraco. De que mision quieres formar parte?".format(self.nom),
                "opciones": {
                    "mexico": "Mexico",
                    "buenos aires": "Buenos Aires"
                }
            },
    "Mexico": {
        "mensaje": "Bienvenido a la mision de Mexico, en esta mision asaltaremos al banco central de Mexico. Para este tenemos opciones de atraco: \n\t\t\t\t\t\t\t- Cabar un tunel \n\t\t\t\t\t\t\t- Asalto a mano armada",
        "opciones": {
            "tunel": self.j,
            "regresar": "tunel",
            "mano": "mano"
        }
            },
        "tunel": {
            "mensaje": "Has elegido cabar un tunel para poder hacer el atraco, escoge tus armas(Debido a que tu atraco es por tunel solo puedes escoger 2 armas): \n\t\t\t\t\t\t\t-Fusil \n\t\t\t\t\t\t\t-Escopeta \n\t\t\t\t\t\t\t-Subfusil \n\t\t\t\t\t\t\t-Bombas",
            "opciones": {
                "fusil y escopeta": "FUSIL/ESCOPETA",
                "escopeta y fusil": "FUSIL/ESCOPETA",

                "fusil y subfusil": "FUSIL/SUBFUSIL",
                "subfusil y fusil": "FUSIL/SUBFUSIL",

                "fusil y bombas": "FUSIL/BOMBAS",
                "bombas y fusil": "FUSIL/BOMBAS",

                "escopeta y subfusil": "ESCOPETA/SUBFUSIL",
                "subfusil y escopeta": "ESCOPETA/SUBFUSIL",

                "escopeta y bombas": "ESCOPETA/BOMBAS",
                "bombas y escopeta": "ESCOPETA/BOMBAS",

                "subfusil y bombas": "SUBFUSIL/BOMBAS",
                "bombas y subfusil": "SUBFUSIL/BOMBAS",
            }
            },
                "FUSIL/ESCOPETA": 
                {
                    "mensaje": "Elegiste fusil y escopeta, para finalizar el plan del golpe necesitas escoger tu vehiculo de escape",
                    "opciones":
                    {
                        "carro": "Carro",
                        "moto": "Moto",
                        "camion": "Camion",
                        "helicoptero": "Helicop",
                    }
                },
                    "Carro":
                    {
                        "mensaje": "Ya has hecho tu tunel y has aparecido en el sotano, el dinero se encuentra en la caja fuerte pasando las oficinas, te alistas \n\t\t\t\t\t\t y subes las escaleras un guardia viene caminando, que decides hacer?",
                        "opciones": 
                        {
                            "disparar": "Disparar",
                            "esconderme": "Esconder",
                            "golpear": "Golpear",
                        }
                    },
                        "Disparar":
                        {
                            "mensaje": "Alertaste a los policias y te metieron a la carcel, para repetir esa parte escribe 'Repetir'",
                            "opciones": 
                            {"repetir": "Carro"}
                        },

                        "Esconder":
                        {
                            "mensaje": "Listo, el policia se fue y no te vio, ahora camina por el pasillo...\n\t\t\t\t\t\tTerminando el pasillo del lado izquierdo",
                            
                        },

                "FUSIL/SUBFUSIL":
                {

                },

                "FUSIL/BOMBAS":
                {

                },

                "ESCOPETA/SUBFUSIL":
                {

                },

                "ESCOPETA/BOMBAS":
                {

                },

                "SUBFUSIL/BOMBAS":
                {

                },

        "mano": {
            "mensaje": "¡Has encontrado un tesoro! ¿Lo tomas o lo dejas?",
            "opciones": {
                "toma": "fin",
                "deja": "inicio"
            }
        },
    "Buenos Aires": {
        "mensaje": "Bienvenido a la mision de Buenos Aires, ",
        "opciones": {
            "toma": "fin",
            "deja": "inicio"
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

    def mostrar_dialogo(self, mensaje):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.dialogos(mensaje))

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
                        self.estado_actual = estado
                        decision = self.decisiones[self.estado_actual]
                        self.mostrar_dialogo(decision["mensaje"])
                    break
                    """self.estado_actual = estado
                    break"""
            if not self.estado_actual:
                break

    def j(self):
        print("hola")

nom = input("Ingresa tu nombre: ")
print("Cargando...")
time.sleep(2) 
os.system('cls' if os.name == 'nt' else 'clear')
juego = Juego(nom)
juego.jugar()
