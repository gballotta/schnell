import macchina

schnell = macchina.Macchina()
schnell.setzonacorrente(1)
schnell.estrudibarre([100.0, 100.0, 100.0, 100.0, 100.0, 1.0, 1.0, 400.0, 400.0, 400.0])
schnell.posabarre(1)
schnell.spostacatenaria(3)
schnell.dumpascript()
