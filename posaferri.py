class PosaFerri(object):
    def __init__(self, risoluzione, numeroferri):
        self.optime = 2.0  # tempo in secondi dell'operazione
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
        framemovimento = int(self.optime / 2 * fps) - 1
        # spostamento della catenaria selectMore

        # settaggio curve di transizioni per le chiavi
        cbuf.append("maxOps.setDefaultTangentType #slow #slow")

        for i in range(1, (self.numeroferri + 1)):
            cbuf.append("select $catenaria")
            if i is not 1:
                for j in range(1, i):
                    s = "selectMore $sbarra_%s_%s" % (settore, j)
                    cbuf.append(s)
            s = "at time %s animate on move $ [0, 0, 0]" % cframe
            cbuf.append(s)
            cframe += framemovimento
            s = "at time %s animate on move $ [0, -%s, 0]" % (cframe, self.risoluzione)
            cbuf.append(s)
            cframe += 1

            # caduta dei ferri

            s = "select $sbarra_%s_%s" % (settore, i)
            cbuf.append(s)
            s = "at time %s animate on move $ [0, 0, 0]" % cframe
            cbuf.append(s)
            cframe += framemovimento
            s = "at time %s animate on $.position = $hlp_sbarre_origine_catenaria.position" % cframe
            cbuf.append(s)
            cframe += 1

        return cbuf
