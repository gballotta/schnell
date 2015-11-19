import macchina

barrepasso01 = [90.0, 90.0, 90.0, 90.0, 90.0,
                90.0, 90.0, 90.0, 90.0, 90.0,
                90.0, 90.0, 90.0, 90.0, 360.0,
                360.0, 360.0, 360.0, 360.0, 360.0]

barrepasso02 = [432.0, 432.0, 432.0, 432.0, 432.0,
                300.0, 300.0, 300.0, 300.0, 300.0,
                300.0, 300.0, 300.0, 300.0, 1.0,
                1.0, 1.0, 1.0, 1.0, 1.0]

schnell = macchina.Macchina()
schnell.setzonacorrente(1)
schnell.estrudibarre(barrepasso01)
schnell.setzonacorrente(2)
schnell.estrudibarre(barrepasso02)
schnell.setzonacorrente(1)
schnell.posabarre(1)
schnell.spostacatenaria(1)
schnell.trasporta(1, 0, 0)
schnell.spostacatenariaindietro(20)
schnell.setzonacorrente(2)
schnell.posabarre(2)
schnell.spostacatenaria(1)
schnell.trasporta(1, 0, -170.0)
schnell.dumpascript()
