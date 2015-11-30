import macchina

barrepasso01 = [90.0, 90.0, 90.0, 90.0, 90.0,
                90.0, 90.0, 90.0, 90.0, 90.0,
                90.0, 90.0, 90.0, 90.0, 600.0,
                600.0, 600.0, 600.0, 600.0, 0.0]

barrepasso02 = [425.0, 425.0, 425.0, 425.0, 425.0,
                95.5, 95.5, 95.5, 95.5, 95.5,
                95.5, 95.5, 95.5, 95.5, 0.0,
                0.0, 0.0, 0.0, 0.0, 0.0]

barrepasso03 = [0.0, 0.0, 0.0, 0.0, 0.0,
                200.0, 200.0, 200.0, 200.0, 200.0,
                200.0, 200.0, 200.0, 200.0, 0.0,
                0.0, 0.0, 0.0, 0.0, 0.0]

barrepasso04 = [80.0, 80.0, 300.0, 300.0, 300.0,
                300.0, 300.0, 300.0, 300.0, 0.0,
                0.0, 0.0, 0.0, 0.0, 300.0,
                300.0, 300.0, 300.0, 300.0, 300.0]

barrepasso05 = [0.0, 300.0, 300.0, 300.0, 300.0,
                300.0, 300.0, 300.0, 300.0, 300.0,
                300.0, 300.0, 300.0, 300.0, 80.0,
                80.0, 80.0, 80.0, 80.0, 80.0]

barrepasso06 = [80.0, 80.0, 80.0, 80.0, 80.0,
                0.0, 0.0, 0.0, 0.0, 0.0,
                0.0, 0.0, 80.0, 80.0, 80.0,
                80.0, 80.0, 80.0, 80.0, 80.0]

schnell = macchina.Macchina()
schnell.setzonacorrente(1)
schnell.estrudibarre(barrepasso01)
schnell.setzonacorrente(2)
schnell.estrudibarre(barrepasso02)
schnell.setzonacorrente(3)
schnell.estrudibarre(barrepasso03)
schnell.setzonacorrente(4)
schnell.estrudibarre(barrepasso04)
schnell.setzonacorrente(5)
schnell.estrudibarre(barrepasso05)
schnell.setzonacorrente(6)
schnell.estrudibarre(barrepasso06)

schnell.setzonacorrente(1)
schnell.posabarre(1)
schnell.trasporta(2, 0, 0)
schnell.setzonacorrente(2)
schnell.posabarre(2)
schnell.trasporta(2, 0, -175)
schnell.setzonacorrente(3)
schnell.posabarre(3)
schnell.trasporta(1, 0, -225)
schnell.setzonacorrente(4)
schnell.posabarre(4)
schnell.trasporta(1, 1, 390)
schnell.setzonacorrente(5)
schnell.posabarre(5)
schnell.trasporta(1, 1, -300)
schnell.setzonacorrente(6)
schnell.posabarre(6)
schnell.trasporta(1, -1, 220)

schnell.dumpascript()
