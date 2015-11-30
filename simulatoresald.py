import macchina
import saldatore

schnell = macchina.Macchina()
schnell.outputfile = "saldi.ms"
schnell.linea = saldatore.SaldatoriS()

schnell.saldatura()
schnell.dumpascript()



