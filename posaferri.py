class PosaFerri(object):
    def __init__(self, risoluzione, numeroferri):
        self.optime = 1.5  # tempo in secondi dell'operazione
        self.risoluzione = risoluzione  # distanza tra un ferro e l'altro
        self.numeroferri = numeroferri  # numero dei ferri in un settore

    def posa(self, settore, framestart, fps):
        """
        crea i comandi di animazione per la posa di tutti i ferri nel settore
        :param settore:
        :param framestart: il frame di partenza dell'animazione
        :param fps: frames per second
        :return:
        """
        cbuf = []
        cframe = framestart
        framemovimentocatenaria = int((self.optime - 1) * fps) - 1
        framemovimentoferri = int(fps - 13)

        # settaggio dei pivot delle sbarre per la rotazione

        for i in range(0, self.numeroferri):
            pivy = 850 + self.risoluzione * (20 - i) - 12.5  # Correzione hardcoded di 12.5 per animazione finale
            s = "$sbarra_%s_%s.pivot = [150, %s, 102]" % (settore, (i + 1), pivy)
            cbuf.append(s)

        # spostamento della catenaria

        for i in range(1, (self.numeroferri + 1)):
            cbuf.append("maxOps.setDefaultTangentType #slow #slow")  # la catenaria si muove smooth
            cbuf.append("select $catenaria")
            if i is not 1:
                for j in range(1, i):
                    s = "selectMore $sbarra_%s_%s" % (settore, j)
                    cbuf.append(s)
            s = "at time %s animate on move $ [0, 0, 0]" % cframe
            cbuf.append(s)
            cframe += framemovimentocatenaria
            s = "at time %s animate on move $ [0, -%s, 0]" % ((cframe - 1), self.risoluzione)
            cbuf.append(s)
            cbuf.append("maxOps.setDefaultTangentType #step #step")
            cbuf.append("select $catenaria")
            s = "at time %s animate on move $ [0, %s, 0]" % (cframe, self.risoluzione)
            cbuf.append(s)
            cbuf.append("maxOps.setDefaultTangentType #slow #slow")
            cframe += 1

            # caduta dei ferri

            s = "select $sbarra_%s_%s" % (settore, i)
            cbuf.append(s)
            s = "at time %s animate on move $ [0, 0, 0]" % cframe
            cbuf.append(s)
            cframe += framemovimentoferri
            cbuf.append("maxOps.setDefaultTangentType #slow #linear")  # il ferro si muove linear
            # s = "at time %s animate on $.position = $hlp_sbarre_origine_catenaria.position" % cframe
            s = "at time %s animate on move $ [0, -72.5, - 57.2]" % cframe
            cbuf.append(s)
            cbuf.append("clearSelection()")  # proviamo cosi'
            cframe += 1

        return {"tempo": (cframe - framestart), "buffer": cbuf}

    def spostacatenaria(self, passi, settore, framestart, fps):
        """
        genera i comandi d'animazione per spostare la catenaria di n passi senza far cadere ferri
        :param passi: numero di passi a vuoto
        :param settore:
        :param framestart: il frame di partenza dell'animazione
        :param fps: frames per second
        :return: lista di comandi
        """

        cbuf = []  # buffer dei comandi da ritornare

        # settaggio frame durata spostamento
        framemovimentocatenaria = int((self.optime - 1) * fps) - 1

        # selezione catenaria e ferri
        cbuf.append("select $catenaria")
        s = "selectMore $sbarra_%s*" % settore
        cbuf.append(s)

        # spostamento elementi

        cframe = framestart
        cbuf.append("maxOps.setDefaultTangentType #slow #slow")  # la catenaria si muove smooth
        s = "at time %s animate on move $ [0, 0, 0]" % cframe
        cbuf.append(s)
        framemovimentocatenaria = int((self.optime - 1) * fps)
        cframe += framemovimentocatenaria * passi - 1
        s = "at time %s animate on move $ [0, -%s, 0]" % (cframe, passi * self.risoluzione)
        cbuf.append(s)
        cframe += 1

        return {"tempo": (cframe - framestart), "buffer": cbuf}

    def spostacatenariaindietro(self, passi, framestart, fps):
        """
        come spostacatenaria, ma la sposta all'indietro e senza muovere ferri.
        serve solamente per resettarla nella simulazione di preview al cliente.
        :param passi: numero di passi a vuoto
        :param framestart: il frame di partenza dell'animazione
        :param fps: frames per second
        :return: lista di comandi
        :return:
        """
        cbuf = []  # buffer dei comandi da ritornare

        # settaggio frame durata spostamento
        framemovimentocatenaria = int((self.optime - 1) * fps) - 1

        # selezione catenaria e spostamento
        cbuf.append("select $catenaria")

        cframe = framestart
        cbuf.append("maxOps.setDefaultTangentType #slow #slow")  # la catenaria si muove smooth
        s = "at time %s animate on move $ [0, 0, 0]" % cframe
        cbuf.append(s)
        framemovimentocatenaria = int((self.optime - 1) * fps)
        cframe += 24
        s = "at time %s animate on move $ [0, %s, 0]" % (cframe, passi * self.risoluzione)
        cbuf.append(s)
        cframe += 1

        return {"tempo": (cframe - framestart), "buffer": cbuf}
