class Trasportatori(object):
    def __init__(self):
        self.velocitay = 315  # velocita orizzontale dei traportatori
        self.velocitaz = 126  # velocita verticale dei traportatori
        self.tragittoy = 630  # tragitto orizzontale dei trasportatori
        self.tragittoz = 126  # tragitto verticale dei trasportatori
        self.temporotazione = 1  # tempo di rotazione del trasportatore 1 in secondi
        self.velocitavassoio = 100  # velocita orizzontale del vassoio
        self.ruotatoprima = False  # flag per verificare se in precedenza c'era stata una rotazione
        self.ruotatocoeff = 0  # flag per verificare l'ultima rotazione : +1 antiorario -1 orario

    def trasporta(self, ntrasp, sezione, ruota, spostvassoio, framestart, fps):
        """
        Anima i traportatori per tutto il ciclo (partenza, arrivo, presa, ritorno, reset)
        :param ntrasp: numero di traportatori da muovere (1 - singolo, 2 - tutti e due)
        :param sezione: la sezione da trasportare
        :param ruota: se settato a 0 il traportatore 1 non ruota di 90, se settato a 1 si
        :param spostvassoio: spostamento orizzontale del vassoio
        :param framestart: il frame di partenza dell'animazione
        :param fps: i frames per second dell'animazione
        :return:
        """
        # inizializzazione variabili comuni

        cbuf = []  # buffer dei comandi da ritornare
        t1fstart = framestart + 1  # frame di partenza tragitto 1 (da reset a p1)
        t1fend = t1fstart + self.tragittoy / self.velocitay * fps - 1  # frame di arrivo tragitto 1
        t1frstart = 0
        t1frend = t1fend
        if self.ruotatoprima:
            t1frstart = t1fend + 1  # frame di partenza della rotazione
            t1frend = t1frstart + self.temporotazione * fps - 1
        t2fstart = t1frend + 1  # frame di partenza tragitto 1 (da p1 a p1 abbassato)
        t2fend = t2fstart + self.tragittoz / self.velocitaz * fps - 1  # frame di arrivo tragitto 2
        t3fstart = t2fend + 1  # frame di partenza tragitto 3 (da p1 abbassato a p1)
        t3fend = t3fstart + self.tragittoz / self.velocitaz * fps - 1  # frame di arrivo tragitto 3
        t3rfstart = 0
        t3rfend = t3fend  # inizializziamo queste variabili in modo da tenere lo scope nella funzione
        if ruota == 1:
            t3rfstart = t3fend + 1  # frame di partenza della rotazione
            t3rfend = t3rfstart + self.temporotazione * fps - 1  # frame di arrivo della rotazione
        t4fstart = t3rfend + 1  # frame di partenza tragitto 4 (da p1 a reset)
        t4fend = t4fstart + self.tragittoy / self.velocitay * fps - 1  # frame di arrivo tragitto 4
        t5fstart = t4fend + 1  # frame di partenza tragitto 5 (da reset a p2 abbassato)
        t5fend = t5fstart + self.tragittoz / self.velocitaz * fps - 1  # frame di arrivo tragitto 5
        t6fstart = t5fend + 1  # frame di partenza tragitto 6 (da p2 abbassato a reset)
        t6fend = t6fstart + self.tragittoz / self.velocitaz * fps - 1  # frame di arrivo tragitto 6
        vstart = t4fstart
        vend = vstart + int(abs(spostvassoio) / self.velocitavassoio * fps) - 1

        # tragitto 1 (da reset a p1)
        cbuf.append("clearSelection()")
        cbuf.append("maxOps.setDefaultTangentType #slow #slow")  # i trasportatori muovono slow
        cbuf.append("select $ctl_t1_y")
        if ntrasp == 2:
            cbuf.append("selectMore $ctl_t2_y")
        s = "at time %s animate on move $ [0, 0, 0]" % t1fstart
        cbuf.append(s)
        s = "at time %s animate on move $ [0, %s, 0]" % (t1fend, self.tragittoy)
        cbuf.append(s)

        # eventuale rotazione di aggiustamento
        if self.ruotatoprima:
            if self.ruotatocoeff == 1:
                cbuf.append("nruoto = eulerangles 0 0 -90")
            else:
                cbuf.append("nruoto = eulerangles 0 0 90")
            cbuf.append("ruotof = eulerangles 0 0 0")
            s = "at time %s animate on rotate $ctl_t1_rot ruotof" % t1frstart
            cbuf.append(s)
            s = "at time %s animate on rotate $ctl_t1_rot nruoto" % t1frend
            cbuf.append(s)
            self.ruotatoprima = False

        # tragitto 2 (da p1 a p1 abbassato)
        cbuf.append("select $ctl_t1_z")
        if ntrasp == 2:
            cbuf.append("selectMore $ctl_t2_z")
        s = "at time %s animate on move $ [0, 0, 0]" % t2fstart
        cbuf.append(s)
        s = "at time %s animate on move $ [0, 0, -%s]" % (t2fend, self.tragittoz)
        cbuf.append(s)

        # presa
        cbuf.append("select $ctl_t1_z")
        if ntrasp == 2:
            cbuf.append("selectMore $ctl_t2_z")
        s = "selectMore $sbarra_%s*" % sezione
        cbuf.append(s)

        # tragitto 3 (da p1 abbassato a p1)
        s = "at time %s animate on move $ [0, 0, 0]" % t3fstart
        cbuf.append(s)
        s = "at time %s animate on move $ [0, 0, %s]" % (t3fend, self.tragittoz)
        cbuf.append(s)

        # eventuale rotazione
        if ruota != 0:
            # variabili
            if ruota == 1:
                cbuf.append("ruoto = eulerangles 0 0 90")  # inserisce il verso di rotazione giusto
                self.ruotatocoeff = 1
            else:
                cbuf.append("ruoto = eulerangles 0 0 -90")
                self.ruotatocoeff = -1
            if ruota == 1:
                cbuf.append("nruoto = eulerangles 0 0 -90")  # e anche per la rotazione di ritorno
            else:
                cbuf.append("nruoto = eulerangles 0 0 90")
            cbuf.append("ruotof = eulerangles 0 0 0")
            cbuf.append("poso = $ctl_t1_rot.pivot")
            # allineamento pivot
            s = "select $sbarra_%s*" % sezione
            cbuf.append(s)
            # cbuf.append("for i in selection do ( i.pivot = [150, 550, 0] )")
            # spostamento
            cbuf.append("selectMore $ctl_t1_rot")
            cbuf.append("for i in selection do (")
            s = "   at time %s animate on rotate i ruotof" % t3rfstart
            cbuf.append(s)
            s = "   at time %s animate on rotate i ruoto" % t3rfend
            cbuf.append(s)
            cbuf.append("   )")
            # riselezione di sbarre e trasportatore (se si ruota si puo' usare solo il traportatore 1)
            cbuf.append("select $ctl_t1_y")
            s = "selectMore $sbarra_%s*" % sezione
            cbuf.append(s)

        # tragitto 4 (da p1 a reset)
        cbuf.append("select $ctl_t1_y")
        if ntrasp == 2:
            cbuf.append("selectMore $ctl_t2_y")
        s = "selectMore $sbarra_%s*" % sezione
        cbuf.append(s)
        s = "at time %s animate on move $ [0, 0, 0]" % t4fstart
        cbuf.append(s)
        s = "at time %s animate on move $ [0, -%s, 0]" % (t4fend, self.tragittoy)
        cbuf.append(s)

        # correzione dell'abbassamento in caso di rotazione (i ferri finiscono un po piu' sopra)
        appoggio = self.tragittoz
        if ruota == 1:
            appoggio = self.tragittoz - 1

        # tragitto 5 (da reset a p2 abbassato)
        cbuf.append("select $ctl_t1_z")
        if ntrasp == 2:
            cbuf.append("selectMore $ctl_t2_z")
        s = "selectMore $sbarra_%s*" % sezione
        cbuf.append(s)
        s = "at time %s animate on move $ [0, 0, 0]" % t5fstart
        cbuf.append(s)
        s = "at time %s animate on move $ [0, 0, -%s]" % (t5fend, appoggio - 22)  # correzione hardcode offset vassoio
        cbuf.append(s)

        # tragitto 6 (da p2 abbassato a reset)
        cbuf.append("select $ctl_t1_z")
        if ntrasp == 2:
            cbuf.append("selectMore $ctl_t2_z")
        s = "at time %s animate on move $ [0, 0, 0]" % t6fstart
        cbuf.append(s)
        s = "at time %s animate on move $ [0, 0, %s]" % (t6fend, appoggio - 22)  # correzione anche qui
        cbuf.append(s)

        # eventuale spostamento del vassoio
        if spostvassoio != 0:
            cbuf.append("select $ctl_vassoio")
            for i in range(1, sezione):  # dobbiamo spostare anche i ferri nel vassoio
                s = "selectMore $sbarra_%s*" % i
                cbuf.append(s)
            s = "at time %s animate on move $ [0, 0, 0]" % vstart
            cbuf.append(s)
            s = "at time %s animate on move $ [%s, 0, 0]" % (vend, spostvassoio)
            cbuf.append(s)

        # settaggio del flag in caso di rotazione in questo trasporto

        if ruota == 1:
            self.ruotatoprima = True

        return {"tempo": (t6fend - framestart), "buffer": cbuf, "break": t4fstart}
