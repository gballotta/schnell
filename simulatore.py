import macchina

barrepasso01 = [90.0, 90.0, 90.0, 90.0, 90.0,
                90.0, 90.0, 90.0, 90.0, 90.0,
                90.0, 90.0, 90.0, 90.0, 600.0,
                600.0, 600.0, 600.0, 600.0, 0.0]

barrepasso02 = [300.0, 300.0, 300.0, 300.0, 300.0,
                300.0, 300.0, 300.0, 300.0, 300.0,
                300.0, 300.0, 300.0, 300.0, 300.0,
                300.0, 300.0, 300.0, 300.0, 0.0]

schnell = macchina.Macchina()
schnell.setzonacorrente(1)
schnell.estrudibarre(barrepasso01)
schnell.setzonacorrente(2)
schnell.estrudibarre(barrepasso02)
schnell.setzonacorrente(1)
schnell.posabarre(1)
schnell.trasporta(2, 0, 0)
schnell.setzonacorrente(2)
schnell.posabarre(2)
schnell.trasporta(1, 1, 0)
schnell.dumpascript()