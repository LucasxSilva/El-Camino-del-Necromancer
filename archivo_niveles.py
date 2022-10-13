import pygame,sys,os,time,math,random
from pygame.locals import *

nivel0 = [

"NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
"NNNN                                 vvvvmmvvvv                                            NNN",
"NMMNN                                 mmmmmmmmvvvvv                                          N",
"NMM                                          mmmmmvvvvVVVVVvvvvvvvvv                         N",
"NM                                               mmmmmmmmmmmmmmmmmmvvvvvvvvvvvvvvvvv         N",
"NM                                                                mmmmmmmmmmmmmmmmmvv        N",
"N                                                                                            N",
"NMM           N                                                                              N",
"NMNNN       NNN                                                                            NNN",
"NNNNNNNNNNNNN                                                                              NNN",
"N                                                       NNNNMMNNNNN                     VVVVVN",
"N                                                      NMM      N                       MMMMMN",
"N    B                       NNNNNNNNNNNNNN                     N                     MMMMMMMN",
"N                          NNNMMMMMMMMMMNNNNNNNNN               N     vvv    vvvvvv          N",
"NNNNNNNNN       MMM        LLLNMMMMMMMMMMMMMMMMMMMNlllllllllllllNNLLLLLmLLLLLLmmmmLLLLLLLLLLLN",
"NMMMMMMMMMMMMMMMMMLLLLLLLLLNMMMMMMMMMMMMMMMMMMMNNNNNMMMMMMMMMNNNLLLLLLLLLLLLLLLLLLLLLLLLLLLLLN",
"NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
"NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
"N                                                                                            N",
"N                                                                                            N",
"N                                                                                            N",
"N                                                                                            N",
"N                                                                                            N",
"N                                                                                            N",
"N                                                                                            N",
"N                                                                                            N",
"N                                                                                            N",
"N                                                                                            N",
"N                                                                                            N",
"NNNNNNNNNNNNNNNNNN                                                                           N",
"N                                                                                            N",
"N                                                                                            N",
"N                      VVVVVV                                                                N",
"N                       MMMM          NNNNN                                                  N",
"N                        NN            NNNNN       VVVVV                                     N",
"N                  MMM                              MMM       MMMMMMMMMMMM                   N",
"N                   N                                           NNNNNNNN                     N",
"NMMMMMMMMMMMMMMMM                                                               B            N",
"NMMMMMMMMMMMMMMLLLLLLLLLLLLLLLLLL                 LLLLLLL                                    N",
"NMMMMMMMMMMMMMMMMMMMMMMMMMMLLLLLLLLLLLLLMMMMMMMMMMMMLLLLLLLLLMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN",
"NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
]

nivel1 = [
"NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
"NNNNNN                                              NNN NNNNNNNNNN NNNNNN                    N",
"NNNN                                                N    NNNNNNN       NNNN                  N",
"NN                                                         N         NNN                     N",
"NNN                                                                                          N",
"N                                                                                            N",
"N                                                                                            N",
"N                                    vvv                                                     N",
"N                          vvvv    vvmmv      vvvvvvv                         NNNNNNNNNNNNNNNN",
"N                      vvvvvvvvvvvvvvvvvvvvvvvvvvvmmvvvvvvvv   vvvvvvvvvvvv       NNNNNNMMMMMN",
"N             vvvvvvvvvm                                        mmmmmmmmmm             NNNNNMN",
"N         VVVVm                                                                            NNN",
"N          MM                                                                                N",
"N                                                                                            N",
"NN                                                                                           N",
"NNNN                                                                                         N",
"N                                 vvvvvvvvv         vvvvvvvvv                                N",
"NNNNNNN                    vvv            mv       vm      vvvvv   vvvvvvvvvv                N",
"NNNNNNNNNN   vvvvvvvvv      m              mv     vm                mmmmmmmm      vvvv       N",
"N             mmmmmmm                       mmmmmmm                                mm        N",
"N                                                                                            N",
"N                                                                                         NNNN",
"N                                                                                          NNN",
"N                                                          vvvvvvv                           N",
"N                                                    vvvvvvmmmmmmvvvvvvvv        NNNNNNNNNNNNN",
"N                vvvvvv                    v                            vvvv       NNNNNMMMMMN",
"N          vvvvvvm    mvvvvvvv          vvvv                                           NNNNNMN",
"NNNN                                 vvvvmmvvvv                                            NNN",
"NMMNN                                 mmmmmmmmvvvvv                                          N",
"NMM                                          mmmmmvvvvVVVVVvvvvvvvvv                         N",
"NM                                               mmmmmmmmmmmmmmmmmmvvvvvvvvvvvvvvvvv         N",
"NM                                                                mmmmmmmmmmmmmmmmmvv        N",
"N                                                                                            N",
"NMM           N                                                                              N",
"NMNNN       NNN                                                                            NNN",
"NNNNNNNNNNNNN                                                                              NNN",
"N                                                       NNNNMMNNNNN                     VVVVVN",
"N                                                      NMM      N                       MMMMMN",
"N    B                       NNNNNNNNNNNNNN                     N                     MMMMMMMN",
"N                          NNNMMMMMMMMMMNNNNNNNNN               N     vvv    vvvvvv          N",
"NNNNNNNNN       MMM        LLLNMMMMMMMMMMMMMMMMMMMNlllllllllllllNNLLLLLmLLLLLLmmmmLLLLLLLLLLLN",
"NMMMMMMMMMMMMMMMMMLLLLLLLLLNMMMMMMMMMMMMMMMMMMMNNNNNMMMMMMMMMNNNLLLLLLLLLLLLLLLLLLLLLLLLLLLLLN",
"NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
]

nivel2 = [
"NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
"NMN            NMMN                                          NNN NNN                       NMN",
"NN             NMMN                                           N   N                         NN",
"N               NN                                                                           N",
"N               N                                                                            N",
"N                                                                                           NN",
"N    B                                                                                     NNN",
"N                                 EEMMMMMMMMMMMMMMMEE                         NNNNNNNNEE    MN",
"N                                 EE M   M   M   M EE                      NNNNN      EE     N",
"NNNNNNNNNNNNNNNNNNNNN             EE M   M   M   M EE                  NNNNNNNNN             N",
"NMMMMMMMMMMMMMNNNNNNNNNN             M   M   M   M                   NNNMMMMMMMM            MN",
"NMMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNEEN      NNNNNNNNNNNMMMMMMMMMMMMMMMMN",
"NNNNNNNNNNNMNNNNNNNNNNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMNN    EE     NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
"N        MM                      NNMMMMMMMMMMMMMMMNN     EE                              M   N",
"N       M                         NNMMMMMMMMMMMMMNN      EE                               MMMN",
"N      M                           NNNNMMMMMMMNNNN                                           N",
"N    MM                               NNNNNNNNN                                              N",
"N   M                                    NNN            VVVV                                 N",
"N MM                                                     MM                           NN     N",
"N M                                                                                NNNNN     N",
"NM                                                                  EENNNNNNNNNNNNNNNMMNNNNNNN",
"N                                                                   EE    NNNNNNNNNMMMMMMMMMMN",
"N                                                                             M   NNNNNNNNNNNN",
"N                          EEMMMMMMMMMMEE                                      MM            N",
"N                          EE  M    M  EE         EE      VVVVVVVVV            NNMM          N",
"N                          EE  M    M  EE                  NMMMMMNNNNNLLLLLLLLLLNN M         N",
"N                              M    M                    NNNNNMMMMMMMMMMMMMMMMMMMMMMMM       N",
"N                      VVVVVVVVVVVVVVVVVVVVVVV           M       M                    MMM    N",
"N     EEMMMMMMMMMMMMVVVNNNMMMMMMMMMMMMMMMMMNN            M     MM                        M   N",
"N     EE        M        MNNMMMMMMMMMMMMMMMNNMLLLLLLLLLLLM   MM                           MMMN",
"N                MMMMMMMM  NNNNNNNNNNNNNNNNN  MMLLLLLLLLLM MM                               MN",
"N                                               MMMLLMMMMMM                                  N",
"N                                                 MMMM                                       N",
"N                                                  MM                                        N",
"N                        EE                        MM              EE       EE   EE       EE N",
"NLMMM                    EE                                        EEMMMMMMMEE   EEMMMMMMMEE N",
"NL  MMMMMMM                                                        EE   M   EE   EE   M   EE N",
"NLMMMMMMMMMMMMMMM                                                  EE   M             M   EE N",
"NL  M     M     MMMM                                               EE   M             M   EE N",
"NLMMMMMMMMMMMMMMMMMMM        EEMMMMMM                              EE   M             M   EE N",
"NL  M     M     M  M         EEM                     EEMMMMMMM     EE   M             M   EE N",
"NLMMMMMMMMMMMMMMMMMMN         NMLLLLLLLLLLLLLNNNN        M  M           M             M      N",
"NLLLLLLLLLLLLLLLLLLLLLLLLLLLLLNNMLLLLLLNNLLLNNMMMNNNLLLLLM  MNLLLLLLLLLNM             MLLLLLLN",
"NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
]

nivel3 = [
"NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
"N                                                                                            N",
"N                                                                                            N",
"N                                                                                            N",
"N    B                                                                                       N",
"N                                                                                            N",
"N                                                                                            N",
"VVVVVVVVVVVV                                                                                 N",
"NMMMMMMMMMMVVVVVVVVVVVV                      MMMMMMMMMMMMMMMM                                N",
"NMMMMMMMMMMMMMMMMMMMMMVVVVVVV                 MMMMMMMMMMMMMM       PEE                       N",
"NMMMMMMMMMMMMMMMMMMMMMMMMMMMVVVVVVVVVP            PPPPP            PEE                       N",
"NMMMMPPPPPMMMMMMMMMMMMMMMMMMMMMMMMMMMPLLLLLLLLLLLLLLLLLLLLLLLLLLLLLPEE                       N",
"NMMMMPPPPPMMMMMMMMMMMMMMMMMMMMMMMMMMMMPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPEE                       N",
"NMMMMMMMMMMMMMMMMMMMMMPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPEE                       N",
"NMMMPPMMMMMMMMMMMPPPPPP                                             EE                       N",
"NMMMPPMMMMMMMPPPPP                                                  EE                       N",
"NMMMMMMMMPPPPP                                                      EE                       N",
"NMMMMMMMPP                                                          EE                       N",
"NMMMPP                                                              EE                       N",
"NPPPP                                                               EE                       N",
"N                                                                   EE           VVVVVVVVVVVVN",
"N        NNNN                                                       VVVVVVVVVVVVVVMMMMMMMMMMMN",  
"N           NNNNN                                           VVVVVVVVVVMMMMMMMMMMMMMMMMMMMMMMMN",
"N                     EEPPPPPPP                    VVVVVVVVVVMMMMMMMMMMMMMPPPMMMMMMMMMMMMMMMMN",
"N                     EE NNNN               EEVVVVVVMMMMMMMMMMMMMMMMMMMMMMPPPMMMMMMMMMMMMMMMMN",
"N                     EE                    EE MMMMMMMMMMMPPMMMMMMMMMMMMMMMMMMMPMMMMMMMMMMMMMN",
"N                     EE                    EE  MMMMMMMMMMPPMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN",
"N                                           EE    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN",
"N       N                                                               MMMMMMMMMMPPPPMMMMMMMN",
"N       N                                                                        MMMMMMMMMMMMN",
"N       NPPPPPMEEPP      PPPEE                                                               N",
"N       NPPPPP EEP          EE                                                               N",
"N              EEP          EE                                                               N",
"N                           EE                                                               N",
"N                           EE                                                               N",
"N                           EE                                                               N",
"N                                                                                            N",
"N           VVVVVVVVV              VVVVVVVVVVVV                                              N",
"NP           MMMMMMM                MMPPPPMMMM                                               N",
"NP             PPP                    PPPP            PVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVN",
"NPLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLPMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN",
"NPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN",
"NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
]


class Muro_verde(object):
    def __init__(self, pos):
        muros_verdes.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 10, 10)

class Muro_marron(object):
    def __init__(self, pos):
        muros_marrones.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 10, 10)

class Muro_negro(object):
    def __init__(self, pos):
        muros_negros.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 10, 10)

class lava(object):
    def __init__(self, pos):
        lavas.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 10, 10)

class escalera(object):
    def __init__(self, pos):
        escaleras.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 10, 10)
        self.x=pos[0]
        self.y=pos[1]

class piedra(object):
    def __init__(self, pos):
        piedras.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 10, 10)    

muros_verdes = []
muros_marrones = []
muros_negros = []
lavas=[]
escaleras=[]
piedras=[]


def cargar_nivel(nivel):
    muros_verdes.clear()
    muros_marrones.clear()
    muros_negros.clear()
    lavas.clear()
    escaleras.clear()
    piedras.clear()

    if nivel==0:
        x = y = 0
        for row in nivel0:
            for col in row:
                if col == "P" or col=="p":
                    piedra((x, y)) 
                if col == "V" or col=="v":
                    Muro_verde((x, y))
                if col == "M" or col=="m":
                    Muro_marron((x, y))
                if col == "N" or col=="n":
                    Muro_negro((x, y))
                if col == "L" or col=="l":
                    lava((x, y))
                if col =="E" or col=="e":
                    escalera((x,y))
                x += 10
            y += 10
            x = 0

    elif nivel==1:
        x = y = 0
        for row in nivel1:
            for col in row:
                if col == "V" or col=="v":
                    Muro_verde((x, y))
                if col == "M" or col=="m":
                    Muro_marron((x, y))
                if col == "N" or col=="n":
                    Muro_negro((x, y))
                if col == "L" or col=="l":
                    lava((x, y))
                if col =="E" or col=="e":
                    escalera((x,y))
                x += 10
            y += 10
            x = 0
    elif nivel==2:
        x = y = 0
        for row in nivel2:
            for col in row:
                if col == "V" or col=="v":
                    Muro_verde((x, y))
                if col == "M" or col=="m":
                    Muro_marron((x, y))
                if col == "N" or col=="n":
                    Muro_negro((x, y))
                if col == "L" or col=="l":
                    lava((x, y))
                if col =="E" or col=="e":
                    escalera((x,y))
                x += 10
            y += 10
            x = 0
    elif nivel==3:
        x = y = 0
        for row in nivel3:
            for col in row:
                if col == "P" or col=="p":
                    piedra((x, y)) 
                if col == "V" or col=="v":
                    Muro_verde((x, y))
                if col == "M" or col=="m":
                    Muro_marron((x, y))
                if col == "N" or col=="n":
                    Muro_negro((x, y))
                if col == "L" or col=="l":
                    lava((x, y))
                if col =="E" or col=="e":
                    escalera((x,y))
                x += 10
            y += 10
            x = 0
    else:
        pass