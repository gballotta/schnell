class Linea(object):
    def __init__(self):
        self.velocitavassoio = 200  # velocita vassoio in centimetri al secondo
        self.velocitavassoiovert = 20  # velocita vassoio verticale in centimetri al secondo
        self.tragitto_0_1 = -700  # tragitto vassoio da automatico a manuale
        self.tragitto_1_2 = -700  # tragitto da manuale a saldatori
        self.tragitto_2_3 = -70  # tragitto da saldatori a uscita
        self.tragitto_3_4 = 2030  # tragitto di ritorno
        self.abbassamentocarrello = 20  # abbassamento del carrello per il viaggio di ritorno
        self.velocitasaldatori = 1  # velocita dei saldatori in secondi
        self.velocitapassocarrello = 1  # tempo in secondi per lo scostamento carrello nelle saldature
        self.traslazionesaldatori = 20  # traslazione in centimetri dei saldatori

    def spostavassoio(self, tragitto, framestart, fps):
        """
        Sposta il vassoio orizzontalmente lungo la linea
        :param tragitto: percorso da compiere in centimetri (positivo verso dx, negativo verso sx)
        :param framestart: frame di partenza
        :param fps: frames al secondo di animazione
        :return:
        """
        # calcolo frames e inizializzazione cbuf

        cbuf = []

        fstart = framestart
        fdest = framestart + int(abs(tragitto) / self.velocitavassoio * fps - 1)

        # selezione oggetti da spostare

        cbuf.append("select $ctl_vassoio")
        cbuf.append("selectMore $sbarra_*")

        # spostamento

        s = "at time %s animate on move $ [0, 0, 0]" % fstart
        cbuf.append(s)
        s = "at time %s animate on move $ [%s, 0, 0]" % (fdest, tragitto)
        cbuf.append(s)

        return {"tempo": (fdest - framestart), "buffer": cbuf}

    def spostavassoiovert(self, tragitto, framestart, fps):
        """
        Sposta il vassoio verticalmente
        :param tragitto: percorso da compiere in centimetri (positivo verso dx, negativo verso sx)
        :param framestart: frame di partenza
        :param fps: frames al secondo di animazione
        :return:
        """
        # calcolo frames e inizializzazione cbuf

        cbuf = []

        fstart = framestart
        fdest = framestart + int(abs(tragitto) / self.velocitavassoiovert + fps - 1)

        # selezione oggetti da spostare

        cbuf.append("select $ctl_vassoio")
        cbuf.append("selectMore $sbarra_*")

        # spostamento

        s = "at time %s animate on move $ [0, 0, 0]" % fstart
        cbuf.append(s)
        s = "at time %s animate on move $ [0, 0, %s]" % (fdest, tragitto)
        cbuf.append(s)

        return {"tempo": (fdest - framestart), "buffer": cbuf}

    def vassoiogiu(self, framestart, fps):
        return self.spostavassoiovert(self.abbassamentocarrello * -1, framestart, fps)

    def vassoiosu(self, framestart, fps):
        return self.spostavassoiovert(self.abbassamentocarrello, framestart, fps)

    def vtragitto_0_1(self, framestart, fps):
        """
        Sposta il vassoio dalla posizione iniziale a quella per il posizionamento manuale
        Il vassoio deve essere nella posizione iniziale
        :param framestart:
        :param fps:
        :return:
        """
        return self.spostavassoio(self.tragitto_0_1, framestart, fps)

    def vtragitto_1_2(self, framestart, fps):
        """
        Sposta il vassoio dalla posizione per il posizionamento manuale a quella dei saldatori
        Il vassoio deve essere nella posizione di posizionamento manuale
        :param framestart:
        :param fps:
        :return:
        """
        return self.spostavassoio(self.tragitto_1_2, framestart, fps)

    def vtragitto_2_3(self, framestart, fps):
        return self.spostavassoio(self.tragitto_2_3, framestart, fps)

    def vtragitto_3_4(self, framestart, fps):
        return self.spostavassoio(self.tragitto_3_4, framestart, fps)

    def salda(self, framestart, fps):
        """
        Salda i ferri
        :param framestart:
        :param fps:
        :return:
        """
        # inizializzazione cbuf e cframe

        cbuf = []
        cframe = framestart

        # calcolo dei tempi di saldatura e dello spostamento del carrello

        tmezzasaldatura = int(self.velocitasaldatori * fps / 2)
        tspostamentocarrello = int(self.velocitapassocarrello * fps / 2)

        # ciclo for di saldatura

        for i in range(0, 21):
            # saldature
            tsald1start = cframe  # inizio e fine saldatura in giu'
            tsald1end = tsald1start + tmezzasaldatura
            tsald2start = tsald1end + 1  # inizio e fine saldatura in su'
            tsald2end = tsald2start + tmezzasaldatura
            tmovstart = tsald2end + 1  # inizio e fine movimento carrello
            tmovend = tmovstart + tspostamentocarrello
            if i < 20:  # i saldatori dispari dallo spostamento 20 in poi non funzionano piu'
                s = "at time %s animate on move $ctl_saldatori_dispari [0, 0, 0]" % tsald1start
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_dispari [0, 0, -%s]" % (tsald1end, self.traslazionesaldatori)
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_dispari [0, 0, 0]" % tsald2start
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_dispari [0, 0, %s]" % (tsald2end, self.traslazionesaldatori)
                cbuf.append(s)
            if i > 2:  # i saldatori pari cominciano a funzionare dallo spostamento 3
                s = "at time %s animate on move $ctl_saldatori_pari [0, 0, 0]" % tsald1start
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_pari [0, 0, -%s]" % (tsald1end, self.traslazionesaldatori)
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_pari [0, 0, 0]" % tsald2start
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_pari [0, 0, %s]" % (tsald2end, self.traslazionesaldatori)
                cbuf.append(s)
            # spostamento carrello
            cbuf.append("select $ctl_vassoio")
            cbuf.append("selectMore $sbarra_*")
            s = "at time %s animate on move $ [0, 0, 0]" % tmovstart
            cbuf.append(s)
            s = "at time %s animate on move $ [-30, 0, 0]" % tmovend
            cbuf.append(s)
            # aggiornamento cframe
            cframe = tmovend + 1

        return {"tempo": (cframe - framestart), "buffer": cbuf}
