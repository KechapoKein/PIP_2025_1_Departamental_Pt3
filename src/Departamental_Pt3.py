import sys
import serial
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "../Interfaz/Departamental.ui"

class MiVentana(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(qtCreatorFile, self)

        self.label_luz = self.findChild(QtWidgets.QLabel, "label_luz")
        self.arduino = None

        try:
            self.arduino = serial.Serial('COM3', 9600, timeout=1)
            print("✅ Conectado al Arduino en COM3")
        except Exception as e:
            print("❌ Error al conectar con Arduino:", e)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.leer_arduino)
        self.timer.start(500)

    def leer_arduino(self):
        if self.arduino and self.arduino.in_waiting:
            try:
                raw = self.arduino.readline().decode(errors='ignore').strip()
                print(f"[DEBUG] Dato crudo recibido: '{raw}'")

                if "Nivel de luz:" in raw:
                    self.label_luz.setText(raw)

                    partes = raw.split(":")
                    if len(partes) > 1:
                        valor = int(partes[1].strip())

                        if valor > 500:
                            self.cambiar_fondo("dia")
                        else:
                            self.cambiar_fondo("noche")
                else:
                    self.label_luz.setText("Esperando luz...")

            except Exception as e:
                self.label_luz.setText("Error de lectura")

    def calcular_puntos_luz(self, valor_luz):
        if valor_luz < 450:
            return 4
        elif valor_luz < 550:
            return 2
        else:
            return 0

    def cambiar_fondo(self, modo):
        if modo == "dia":
            self.setStyleSheet(
                "QMainWindow { background-image: url(../assets/Day.jpg); background-repeat: no-repeat; background-position: center; }")
        elif modo == "noche":
            self.setStyleSheet(
                "QMainWindow { background-image: url(../assets/Night.jpg); background-repeat: no-repeat; background-position: center; }")
        print("Sip, me encanta el Frutiger Aero")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec_())