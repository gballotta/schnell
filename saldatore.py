class SaldatoriS(object):
    def __init__(self):
        self.traslazioney = 135.0
        self.traslazionez = 18.0
        self.scatto = 15.0
        self.tempotraslazioney = 1.0
        self.temposaldatura = 1.0
        self.temposcatto = 1.0
        self.passaggioasuperiori = 6

    def salda(self, framestart, fps):
        """
        Esegue cicli di saldatura
        :param framestart:
        :param fps:
        :return:
        """

        cbuf = []
        ciclisaldatura = 12
        cframe = framestart
        pospari = -1  # posizione dei saldatori : -1 sono in basso +1 sono in alto
        posdispari = -1

        frmsaldamezzo = int(self.temposaldatura * fps / 2) - 1
        frmsaldatutto = int(self.temposaldatura * fps)
        frmspostamento = int(self.tempotraslazioney * fps) - 1
        frmspostementocarrello = int(self.temposcatto * fps) - 1

        for i in range(0, ciclisaldatura):
            s1gs = cframe
            s1ge = s1gs + frmsaldamezzo
            s1ss = s1ge + 1
            s1se = cframe + frmsaldatutto
            ts = s1se + 1
            te = ts + frmspostamento
            s2gs = te + 1
            s2ge = s2gs + frmsaldamezzo
            s2ss = s2ge + 1
            s2se = te + frmsaldatutto
            tempopari = 0
            tempodispari = 0

            # saldatori pari
            if i > 2:  # i saldatori pari non partono prima
                if i < (self.passaggioasuperiori + 2):
                    # punto 1
                    cbuf.append("at time %s animate on move $ctl_saldatori_pari [0, 0, 0]" % s1gs)
                    cbuf.append("at time %s animate on move $ctl_saldatori_pari [0, 0, -%s]" % (s1ge, self.traslazionez))
                    cbuf.append("at time %s animate on move $ctl_saldatori_pari [0, 0, 0]" % s1ss)
                    cbuf.append("at time %s animate on move $ctl_saldatori_pari [0, 0, %s]" % (s1se, self.traslazionez))
                    # traslazione
                    cbuf.append("at time %s animate on move $ctl_saldatori_pari [0, 0, 0]" % ts)
                    cbuf.append("at time %s animate on move $ctl_saldatori_pari [0, %s, 0]" % (te, self.traslazioney * -pospari))
                    pospari *= -1
                    # punto 2
                    cbuf.append("at time %s animate on move $ctl_saldatori_pari [0, 0, 0]" % s2gs)
                    cbuf.append("at time %s animate on move $ctl_saldatori_pari [0, 0, -%s]" % (s2ge, self.traslazionez))
                    cbuf.append("at time %s animate on move $ctl_saldatori_pari [0, 0, 0]" % s2ss)
                    cbuf.append("at time %s animate on move $ctl_saldatori_pari [0, 0, %s]" % (s2se, self.traslazionez))
                    tempopari = s2se - s1gs
                else:
                    if pospari == -1:
                        cbuf.append("at time %s animate on move $ctl_saldatori_pari [0, 0, 0]" % cframe)
                        cbuf.append("at time %s animate on move $ctl_saldatori_pari [0, %s, 0]" % ((cframe + frmspostamento), self.traslazioney))
                        s1gs = cframe + frmspostamento + 1
                        s1ge = s1gs + frmsaldamezzo
                        s1ss = s1ge + 1
                        s1se = cframe + frmspostamento + frmsaldatutto
                        pospari *= -1
                    cbuf.append("at time %s animate on move $saldatori_pari_s [0, 0, 0]" % s1gs)
                    cbuf.append("at time %s animate on move $saldatori_pari_s [0, 0, -%s]" % (s1ge, self.traslazionez))
                    cbuf.append("at time %s animate on move $saldatori_pari_s [0, 0, 0]" % s1ss)
                    cbuf.append("at time %s animate on move $saldatori_pari_s [0, 0, %s]" % (s1se, self.traslazionez))
                    tempopari = s1se - cframe

            # saldatori dispari
            if i >= 0:  # i saldatori dispari partono subito
                if i < self.passaggioasuperiori:
                    # punto 1
                    cbuf.append("at time %s animate on move $ctl_saldatori_dispari [0, 0, 0]" % s1gs)
                    cbuf.append("at time %s animate on move $ctl_saldatori_dispari [0, 0, -%s]" % (s1ge, self.traslazionez))
                    cbuf.append("at time %s animate on move $ctl_saldatori_dispari [0, 0, 0]" % s1ss)
                    cbuf.append("at time %s animate on move $ctl_saldatori_dispari [0, 0, %s]" % (s1se, self.traslazionez))
                    # traslazione
                    cbuf.append("at time %s animate on move $ctl_saldatori_dispari [0, 0, 0]" % ts)
                    cbuf.append("at time %s animate on move $ctl_saldatori_dispari [0, %s, 0]" % (te, self.traslazioney * -posdispari))
                    posdispari *= -1
                    # punto 2
                    cbuf.append("at time %s animate on move $ctl_saldatori_dispari [0, 0, 0]" % s2gs)
                    cbuf.append("at time %s animate on move $ctl_saldatori_dispari [0, 0, -%s]" % (s2ge, self.traslazionez))
                    cbuf.append("at time %s animate on move $ctl_saldatori_dispari [0, 0, 0]" % s2ss)
                    cbuf.append("at time %s animate on move $ctl_saldatori_dispari [0, 0, %s]" % (s2se, self.traslazionez))
                    tempodispari = s2se - s1gs
                else:
                    if posdispari == -1:
                        cbuf.append("at time %s animate on move $ctl_saldatori_dispari [0, 0, 0]" % cframe)
                        cbuf.append("at time %s animate on move $ctl_saldatori_dispari [0, %s, 0]" % ((cframe + frmspostamento), self.traslazioney))
                        s1gs = cframe + frmspostamento + 1
                        s1ge = s1gs + frmsaldamezzo
                        s1ss = s1ge + 1
                        s1se = cframe + frmspostamento + frmsaldatutto
                        posdispari *= -1
                    cbuf.append("at time %s animate on move $saldatori_dispari_s [0, 0, 0]" % s1gs)
                    cbuf.append("at time %s animate on move $saldatori_dispari_s [0, 0, -%s]" % (s1ge, self.traslazionez))
                    cbuf.append("at time %s animate on move $saldatori_dispari_s [0, 0, 0]" % s1ss)
                    cbuf.append("at time %s animate on move $saldatori_dispari_s [0, 0, %s]" % (s1se, self.traslazionez))
                    tempodispari = s1se - cframe

            # carrello
            cs = cframe + tempopari
            if tempodispari > tempopari:
                cs = cframe + tempodispari
            ce = cs + frmspostementocarrello
            cbuf.append("select $vassoio")
            cbuf.append("selectMore $rete")
            cbuf.append("at time %s animate on move $ [0, 0, 0]" % cs)
            cbuf.append("at time %s animate on move $ [-%s, 0, 0]" % (ce, self.scatto))
            cbuf.append("clearSelection()")

            cframe = ce + 1

        return {"tempo": (cframe - framestart), "buffer": cbuf}
