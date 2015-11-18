class SputaFerri(object):
    def __init__(self):
        self.optime = 2.0  # tempo in secondi dell'operazione

    def sputaferro(self, diametro, altezza, settore, fid):
        """
        ritorna una lista di istruzioni maxscript per la creazione di un ferro e la sua posa sulla catenaria
        :param diametro: diametro della sbarra
        :param altezza: lunghezza della sbarra
        :param settore: settore di lavorazione
        :param fid: id del ferro
        :return: lista di istruzioni
        """
        commandsbuf = []  # buffer di comandi da ritornare

        # creazione del cilindro
        s = "foo = Cylinder name:\"sbarra_%s_%s\" radius:%s height:%s heightsegs:1 sides:16" % (settore, fid, diametro/2, altezza)
        commandsbuf.append(s)
        # rotazione
        s = "rotate foo rotazionesbarra"
        commandsbuf.append(s)
        # posizionamento
        s = "foo.position = $hlp_origine_sbarre.position"
        commandsbuf.append(s)

        # nel caso l'altezza del ferro sia 1 si deve attivare un trigger speciale
        # questo ferro sara' invisibile
        # lo facciamo perche' nella fila di ferri messi dentro ci devono potere essere buchi

        if altezza == 1:
            s = "foo.visibility = 0.0"
            commandsbuf.append(s)

        # ritorno della lista
        return commandsbuf
