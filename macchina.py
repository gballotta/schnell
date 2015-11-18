import macchinainterface
import sputaferri
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
        self.spessoresbarra = 1.0  # lo spessore della sbarra
        self.zonacorrente = 1  # la zona corrente di lavorazione (1-4 superiori, 5-8 inferiori)

        # buffers dei files di output
        self.outputfilebuf = []
        self.outputsetupbuf = []

        # sputaferri (SPF)
        self.sputaferri = sputaferri.SputaFerri()

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
        # aggiunta del tempo impiegato
        self.timer1.passseconds(self.sputaferri.optime)
        # richiesta delle istruzioni
        c = self.sputaferri.sputaferro(self.spessoresbarra, altezza, self.zonacorrente, fid)
        self.outputfilebuf.extend(c)

    def estrudibarre(self, lunghezze):
        """
        estrude piu barre con un solo comando
        :param lunghezze: lista contenente le varie lunghezze
        :return:
        """
        contatore = 1
        for i in lunghezze:
            self.estrudibarra(i, contatore, 0)
            contatore += 1
