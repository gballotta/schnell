class Linea(object):
    def __init__(self):
        self.velocitavassoio = 200.0  # velocita vassoio in centimetri al secondo
        self.velocitavassoiovert = 20  # velocita vassoio verticale in centimetri al secondo
        self.tragitto_0_1 = -1000  # tragitto vassoio da automatico a manuale
        self.tragitto_1_2 = -700  # tragitto da manuale a saldatori
        self.tragitto_2_3 = -70  # tragitto da saldatori a uscita
        self.tragitto_3_4 = 3100  # tragitto di ritorno
        self.abbassamentocarrello = 40  # abbassamento del carrello per il viaggio di ritorno
        self.velocitasaldatori = 1  # velocita dei saldatori in secondi
        self.velocitapassocarrello = 1  # tempo in secondi per lo scostamento carrello nelle saldature
        self.traslazionesaldatori = 20  # traslazione in centimetri dei saldatori
        self.velocitalatsaldatori = 150  # velocita laterale saldatori in centimetri al secondo

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
        print "debug framestart %s" % fstart
        print "debug framend %s" % fdest

        # selezione oggetti da spostare

        cbuf.append("select $ctl_vassoio")
        cbuf.append("selectMore $rete")

        # spostamento

        s = "at time %s animate on move $ [0, 0, 0]" % fstart
        cbuf.append(s)
        s = "at time %s animate on move $ [%s, 0, 0]" % (fdest, tragitto)
        cbuf.append(s)

        return {"tempo": (fdest - framestart), "buffer": cbuf}

    def spostavassoiovert(self, tragitto, settore, framestart, fps):
        """
        Sposta il vassoio verticalmente
        :param tragitto: percorso da compiere in centimetri (positivo verso dx, negativo verso sx)
        :param settore: 1: parte sinistra della macchina - 2: parte destra
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
        cbuf.append("selectMore $rete")
        if settore == 1:
            cbuf.append("selectMore $ctl_alzatore_sx")
        else:
            cbuf.append("selectMore $ctl_alzatore_dx")

        # spostamento

        s = "at time %s animate on move $ [0, 0, 0]" % fstart
        cbuf.append(s)
        s = "at time %s animate on move $ [0, 0, %s]" % (fdest, tragitto)
        cbuf.append(s)

        return {"tempo": (fdest - framestart), "buffer": cbuf}

    def vassoiogiu(self, settore, framestart, fps):
        return self.spostavassoiovert(self.abbassamentocarrello * -1, settore, framestart, fps)

    def vassoiosu(self, settore, framestart, fps):
        return self.spostavassoiovert(self.abbassamentocarrello, settore, framestart, fps)

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

        for i in range(0, 42):
            s1s = cframe
            s1e = s1s + tmezzasaldatura
            s2s = s1e
            s2e = s2s + tmezzasaldatura
            s3s = s2e
            s3e = s3s + int(150 / self.velocitalatsaldatori) * fps
            s4s = s3e
            s4e = s4s + tmezzasaldatura
            s5s = s4e
            s5e = s5s + tmezzasaldatura
            s6s = s5e
            s6e = s6s + int(150 / self.velocitalatsaldatori) * fps
            if i < 40:  # i saldatori dispari dallo spostamento 20 in poi non funzionano piu'
                s = "at time %s animate on move $ctl_saldatori_dispari [0, 0, 0]" % s1s  # discesa 1
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_dispari [0, 0, -%s]" % (s1e, self.traslazionesaldatori)
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_dispari [0, 0, 0]" % s2s  # salita 1
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_dispari [0, 0, %s]" % (s2e, self.traslazionesaldatori)
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_dispari [0, 0, 0]" % s3s  # laterale 1
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_dispari [0, 150, 0]" % s3e
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_dispari [0, 0, 0]" % s4s  # discesa 2
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_dispari [0, 0, -%s]" % (s4e, self.traslazionesaldatori)
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_dispari [0, 0, 0]" % s5s  # salita 2
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_dispari [0, 0, %s]" % (s5e, self.traslazionesaldatori)
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_dispari [0, 0, 0]" % s6s  # laterale 2
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_dispari [0, -150, 0]" % s6e
                cbuf.append(s)
            if i > 2:  # i saldatori pari cominciano a funzionare dallo spostamento 3
                s = "at time %s animate on move $ctl_saldatori_pari [0, 0, 0]" % s1s  # discesa 1
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_pari [0, 0, -%s]" % (s1e, self.traslazionesaldatori)
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_pari [0, 0, 0]" % s2s  # salita 1
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_pari [0, 0, %s]" % (s2e, self.traslazionesaldatori)
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_pari [0, 0, 0]" % s3s  # laterale 1
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_pari [0, 150, 0]" % s3e
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_pari [0, 0, 0]" % s4s  # discesa 2
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_pari [0, 0, -%s]" % (s4e, self.traslazionesaldatori)
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_pari [0, 0, 0]" % s5s  # salita 2
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_pari [0, 0, %s]" % (s5e, self.traslazionesaldatori)
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_pari [0, 0, 0]" % s6s  # laterale 2
                cbuf.append(s)
                s = "at time %s animate on move $ctl_saldatori_pari [0, -150, 0]" % s6e
                cbuf.append(s)
            # carrello
            cstart = s6s
            cend = s6s + (self.velocitapassocarrello * fps)
            cbuf.append("select $ctl_vassoio")
            cbuf.append("selectMore $rete")
            s = "at time %s animate on move $ [0, 0, 0]" % cstart
            cbuf.append(s)
            s = "at time %s animate on move $ [-15, 0, 0]" % cend
            cbuf.append(s)
            # aggiornamento cframe
            cframe = s6e + 1

        return {"tempo": (cframe - framestart), "buffer": cbuf}

    def salda2(self, framestart, fps):
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
