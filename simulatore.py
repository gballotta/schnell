import macchina

schnell = macchina.Macchina()
schnell.setzonacorrente(1)
schnell.estrudibarre([100.0, 420.0, 50.0, 50.0, 700.0])
schnell.posabarre(1)
schnell.dumpascript()
