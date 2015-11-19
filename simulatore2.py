import macchina

barrepasso01 = [0.0, 255.0, 255.0, 255.0, 255.0,
                255.0, 255.0, 255.0, 255.0, 255.0,
                255.0, 255.0, 255.0, 255.0, 600.0,
                600.0, 600.0, 600.0, 600.0, 600.0]

barrepasso02 = [0.0, 240.0, 240.0, 240.0, 240.0,
                240.0, 240.0, 240.0, 240.0, 240.0,
                240.0, 240.0, 240.0, 240.0, 0.0,
                0.0, 0.0, 0.0, 0.0, 0.0]

barrepasso03 = [0.0, 0.0, 0.0, 0.0, 300.0,
                300.0, 300.0, 300.0, 300.0, 300.0,
                300.0, 300.0, 300.0, 300.0, 300.0,
                300.0, 300.0, 300.0, 300.0, 300.0]

barrepasso04 = [0.0, 0.0, 0.0, 0.0, 0.0,
                300.0, 300.0, 300.0, 300.0, 300.0,
                300.0, 300.0, 300.0, 300.0, 300.0,
                300.0, 300.0, 300.0, 300.0, 300.0]

schnell = macchina.Macchina()
schnell.setzonacorrente(1)
schnell.estrudibarre(barrepasso01)
schnell.setzonacorrente(2)
schnell.estrudibarre(barrepasso02)
schnell.setzonacorrente(3)
schnell.estrudibarre(barrepasso03)
schnell.setzonacorrente(4)
schnell.estrudibarre(barrepasso04)
schnell.setzonacorrente(1)
schnell.posabarre(1)
schnell.spostacatenaria(1)
schnell.trasporta(2, 0, 0)
schnell.spostacatenariaindietro(20)
schnell.setzonacorrente(2)
schnell.posabarre(2)
schnell.spostacatenaria(1)
schnell.trasporta(1, 0, -360)
schnell.spostacatenariaindietro(20)
schnell.setzonacorrente(3)
schnell.posabarre(3)
schnell.spostacatenaria(1)
schnell.trasporta(1, 1, 360)
schnell.spostacatenariaindietro(20)
schnell.setzonacorrente(4)
schnell.posabarre(4)
schnell.spostacatenaria(1)
schnell.trasporta(1, 1, -360)
schnell.spostacatenariaindietro(20)
schnell.muovivassoio(360)

schnell.portasumanuale()
schnell.portasusaldatori()
schnell.saldatura()
schnell.portasucarico()
schnell.scendivassoio()
schnell.portaindietro()
schnell.salivassoio()

schnell.dumpascript()
