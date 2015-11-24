import macchinainterface
import sputaferri
import posaferri
import trasportatori
import linea
import anitimer.anitimer


class Macchina(macchinainterface.MacchinaInterface):
    def __init__(self):
        # parametri generali della macchina
        self.outputfile = "script.ms"  # script maxscript della simulazione
        self.outputsetup = "setup.txt"  # script maxscript di setup (da lanciare prima della simulazione)
        self.timer1 = anitimer.anitimer.AniTimer()  # timer 1 della macchina e relativo setup
        self.timer1.startframe = 0
        self.timer1.fps = 25

        # parametri della simulazione
        self.numeroferri = 20  # numero di ferri massimo in un settore
        self.risoluzione = 15.0  # la risoluzione della macchina
        self.spessoresbarra = 1.0  # lo spessore della sbarra
        self.zonacorrente = 1  # la zona corrente di lavorazione

        # buffers dei files di output
        self.outputfilebuf = []
        self.outputsetupbuf = []

        # sputaferri (SPF)
        self.sputaferri = sputaferri.SputaFerri()
        self.breakpoint = 0  # frame di inizio per il ciclo successivo

        # posaferri (PSF)
        self.posaferri = posaferri.PosaFerri(self.risoluzione, self.numeroferri)

        # trasportatori (TRS)
        self.trasportatori = trasportatori.Trasportatori()

        # linea (LNE)
        self.linea = linea.Linea()

    def setzonacorrente(self, zonacorrente):
        """
        Setta la zona di lavorazione corrente
        :param zonacorrente: intero da 1 a 8
        :return:
        """
        self.zonacorrente = zonacorrente

    def inizializzasetup(self):
        """
        inizializza i comandi da dumpare nel file di setup
        :return:
        """
        # durata totale dell'animazione
        s = "animationRange = (interval 0f %sf)" % self.timer1.endframe
        self.outputsetupbuf.append(s)
        # rotazione delle sbarre
        s = "rotazionesbarra = eulerangles 0 90 0"
        self.outputsetupbuf.append(s)
        # mappatura barre
        self.outputsetupbuf.append("mappac = Uvwmap()")
        self.outputsetupbuf.append("mappac.maptype = 1")
        s = "mappac.length = %s" % (self.spessoresbarra + 0.2)
        self.outputsetupbuf.append(s)
        s = "mappac.width = %s" % (self.spessoresbarra + 0.2)
        self.outputsetupbuf.append(s)
        self.outputsetupbuf.append("mappac.height = 2.4")
        self.outputsetupbuf.append("utile = 2")

    def dumpasetup(self):
        """
        scrive il file di setup
        :return:
        """
        f = open(self.outputsetup, 'w')
        for i in self.outputsetupbuf:
            siringa = i + '\n'
            f.write(siringa)
        f.close()

    def dumpascript(self):
        """
        scrive il file di maxscript dell'animazione
        :return:
        """
        f = open(self.outputfile, 'w')

        # scrittura della parte di setup

        self.inizializzasetup()  # il setup va inizializzato dopo perche' serve l'animazione completa

        for i in self.outputsetupbuf:
            siringa = i + '\n'
            f.write(siringa)

        # scrittura dello script

        for i in self.outputfilebuf:
            siringa = i + '\n'
            f.write(siringa)
        f.close()

    def estrudibarra(self, altezza, fid, framestart):
        """
        invia al wrapper sputaferri il comando di creare una barra
        :param altezza: lunghezza della sbarra
        :param fid: id della barra (da 1 a boh)
        :param framestart: frame di partenza
        :return:
        """
        # richiesta delle istruzioni
        c = self.sputaferri.sputaferro(self.spessoresbarra, altezza, self.zonacorrente, fid)
        self.outputfilebuf.extend(c)

    def estrudibarre(self, lunghezze):
        """
        estrude piu barre con un solo comando
        se il valore di lunghezza e' uguale a 0 la sbarra non verra' creata
        :param lunghezze: lista contenente le varie lunghezze (inserire 1 per non mettere una sbarra in sequenza)
        :return:
        """
        contatore = 1
        for i in lunghezze:
            if i is not 0:
                self.estrudibarra(i, contatore, 0)
            contatore += 1

    def posabarre(self, settore):
        """
        invia al wrapper posaferri il comando di posare tutte le sbarre del settore
        :param settore: il settore di sbarre da posare
        :return:
        """
        c = self.posaferri.posa(settore, self.breakpoint, self.timer1.fps)
        self.outputfilebuf.extend(c['buffer'])

        # calcolo del tempo di esecuzione a aggiornamento del timer

        self.timer1.endframe += c['tempo']
        self.timer1.currentframe = self.timer1.endframe

        print self.timer1.endframe

        # tempoesecuzione = self.posaferri.optime * self.numeroferri
        # self.timer1.passseconds(tempoesecuzione)
        # print self.timer1.endframe

    def spostacatenaria(self, passi):
        """
        invia al wrapper posaferri il comando di spostare la catenaria di n passi
        :param passi:
        :return:
        """
        c = self.posaferri.spostacatenaria(passi, self.zonacorrente, self.timer1.currentframe, self.timer1.fps)
        self.outputfilebuf.extend(c['buffer'])

        # calcolo del tempo di esecuzione a aggiornamento del timer

        self.timer1.endframe += c['tempo']
        self.timer1.currentframe = self.timer1.endframe

        # tempoesecuzione = (self.posaferri.optime - 1) * passi
        # self.timer1.passseconds(tempoesecuzione)
        # self.timer1.endframe += 1
        print self.timer1.currentframe

    def spostacatenariaindietro(self, passi):
        """
        invia al wrapper posaferri il comando di spostare la catenaria di n passi
        :param passi:
        :return:
        """
        c = self.posaferri.spostacatenariaindietro(passi, self.timer1.endframe, self.timer1.fps)
        self.outputfilebuf.extend(c['buffer'])

        # calcolo del tempo di esecuzione a aggiornamento del timer

        self.timer1.endframe += c['tempo']
        self.timer1.currentframe = self.timer1.endframe

        # tempoesecuzione = (self.posaferri.optime - 1) * passi
        # self.timer1.passseconds(tempoesecuzione)
        # self.timer1.endframe += 1
        print self.timer1.endframe

    def trasporta(self, ntrasp, ruota, spostvassoio):
        """
        Invia al wrapper il comando di azionare i trasportatori
        :param ntrasp:
        :param ruota:
        :param spostvassoio:
        :return:
        """
        r = self.trasportatori.trasporta(ntrasp, self.zonacorrente, ruota, spostvassoio, self.timer1.endframe, self.timer1.fps)

        self.outputfilebuf.extend(r['buffer'])
        self.timer1.endframe += (r['tempo'])
        self.timer1.currentframe = self.timer1.endframe
        print self.timer1.endframe
        self.breakpoint = r['break']

    def muovivassoio(self, tragitto):
        """
        sposta il vassoio arbitrariamente (per esempio per metterlo a posto)
        :param tragitto: percorso in centimetri
        :return:
        """
        r = self.linea.spostavassoio(tragitto, self.timer1.currentframe, self.timer1.fps)
        self.outputfilebuf.extend(r['buffer'])
        self.timer1.endframe += (r['tempo'])
        self.timer1.currentframe = self.timer1.endframe
        print self.timer1.endframe

    def portasumanuale(self):
        """
        Invia al wrapper il comando di portare il vassoio nella posizione di posa manuale
        :return:
        """
        r = self.linea.vtragitto_0_1(self.timer1.currentframe, self.timer1.fps)
        self.outputfilebuf.extend(r['buffer'])
        self.timer1.endframe += (r['tempo'])
        self.timer1.currentframe = self.timer1.endframe
        print self.timer1.endframe

    def portasusaldatori(self):
        """
        Invia al wrapper il comando di portare il vassoio nella posizione di inizio saldatura
        :return:
        """
        r = self.linea.vtragitto_1_2(self.timer1.currentframe, self.timer1.fps)
        self.outputfilebuf.extend(r['buffer'])
        self.timer1.endframe += (r['tempo'])
        self.timer1.currentframe = self.timer1.endframe
        print self.timer1.endframe

    def saldatura(self):
        """
        Invia al wrapper i comandi di saldatura
        :return:
        """
        r = self.linea.salda(self.timer1.currentframe, self.timer1.fps)
        self.outputfilebuf.extend(r['buffer'])
        self.timer1.endframe += (r['tempo'])
        self.timer1.currentframe = self.timer1.endframe
        print self.timer1.endframe

    def portasucarico(self):
        """
        Invia al wrapper il comando di portare il vassoio nella posizione di carico
        :return:
        """
        r = self.linea.vtragitto_2_3(self.timer1.currentframe, self.timer1.fps)
        self.outputfilebuf.extend(r['buffer'])
        self.timer1.endframe += (r['tempo'])
        self.timer1.currentframe = self.timer1.endframe
        print self.timer1.endframe

    def portaindietro(self):
        """
        Invia al wrapper il comando di portare il vassoio nella posizione iniziale
        :return:
        """
        r = self.linea.vtragitto_3_4(self.timer1.currentframe, self.timer1.fps)
        self.outputfilebuf.extend(r['buffer'])
        self.timer1.endframe += (r['tempo'])
        self.timer1.currentframe = self.timer1.endframe
        print self.timer1.endframe

    def scendivassoio(self, settore):
        """
        Invia al wrapper il comando di fare scendere il vassoio
        :param settore
        :return:
        """
        r = self.linea.vassoiogiu(settore, self.timer1.currentframe, self.timer1.fps)
        self.outputfilebuf.extend(r['buffer'])
        self.timer1.endframe += (r['tempo'])
        self.timer1.currentframe = self.timer1.endframe
        print self.timer1.endframe

    def salivassoio(self, settore):
        """
        Invia al wrapper il comando di fare salire il vassoio
        :param settore
        :return:
        """
        r = self.linea.vassoiosu(settore, self.timer1.currentframe, self.timer1.fps)
        self.outputfilebuf.extend(r['buffer'])
        self.timer1.endframe += (r['tempo'])
        self.timer1.currentframe = self.timer1.endframe
        print self.timer1.endframe