import macchina

schnell = macchina.Macchina()
schnell.outputfile = "parte2.ms"

schnell.portasumanuale()
schnell.portasusaldatori()
schnell.saldatura()
schnell.portasucarico()
schnell.scendivassoio(1)
schnell.portaindietro()
schnell.salivassoio(2)
schnell.muovivassoio(-700)

schnell.dumpascript()
