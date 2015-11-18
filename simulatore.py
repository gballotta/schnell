import macchina

barrepasso01 = [90.0, 90.0, 90.0, 90.0, 90.0,
                90.0, 90.0, 90.0, 90.0, 90.0,
                90.0, 90.0, 90.0, 90.0, 360.0,
                360.0, 360.0, 360.0, 360.0, 360.0]

schnell = macchina.Macchina()
schnell.setzonacorrente(1)
schnell.estrudibarre(barrepasso01)
schnell.posabarre(1)
schnell.spostacatenaria(1)
schnell.dumpascript()
