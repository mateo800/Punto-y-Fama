# app_mejorado_funcional.py
import sys
import random
from datetime import date
from pathlib import Path
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit,
    QVBoxLayout, QHBoxLayout, QStackedWidget, QTableWidget,
    QTableWidgetItem, QAbstractItemView, QFrame, QSpacerItem,
    QSizePolicy, QHeaderView
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

if getattr(sys, 'frozen', False):
    # Cuando el programa está empacado con PyInstaller, sys.executable apunta al exe
    APP_DIR = Path(sys.executable).parent
else:
    # Cuando se ejecuta en modo .py
    APP_DIR = Path(__file__).parent

HISTORIAL_FILE = APP_DIR / "historialJuego.txt"
# ---------------- Datos ----------------
codigo = random.sample(range(10), 4)
hoy = str(date.today())
HISTORIAL_FILE = Path("historialJuego.txt")

# ---------------- App ----------------
app = QApplication(sys.argv)

# --- CAMBIO ESTÉTICO: tema global para toda la app (colores, botones, inputs, tablas) ---
app.setStyleSheet("""
    QWidget { background-color: #0f1724; color: #e6eef8; font-family: 'Segoe UI', Arial, sans-serif; }
    QLabel#title { font-size: 22px; font-weight: 700; color: #f8fafc; }
    QLabel#subtitle { font-size: 13px; color: #cbd5e1; }
    QFrame#card { background-color: rgba(255,255,255,0.06); border-radius: 14px; }
    QPushButton {
        background-color: #e6f0ff; color: #072146; border-radius: 10px; padding: 8px 12px; min-height: 36px;
    }
    QPushButton:hover { background-color: #cfe6ff; }
    QLineEdit {
        background-color: rgba(255,255,255,0.98); color: #052033; border-radius: 8px; padding: 8px;
    }
    QTableWidget { background-color: rgba(255,255,255,0.98); color: #052033; border-radius: 8px; }
    QHeaderView::section { background-color: #2563eb; color: white; font-weight: 600; padding: 6px; border: none; }
""")
# --- FIN CAMBIO ESTÉTICO ---

# ---------------- Stacked windows ----------------
VentanaLogin = QWidget()
VentanaPrincipal = QWidget()
VentanaJuego = QWidget()
VentanaHistorial = QWidget()

# Set sizes and titles
VentanaLogin.setFixedSize(420, 460)
VentanaLogin.setWindowTitle("LOGIN")

VentanaPrincipal.setFixedSize(900, 600)
VentanaPrincipal.setWindowTitle("PRINCIPAL")

VentanaJuego.setFixedSize(900, 600)
VentanaJuego.setWindowTitle("JUEGO")

VentanaHistorial.setFixedSize(900, 600)
VentanaHistorial.setWindowTitle("HISTORIAL")

stack = QStackedWidget()
stack.addWidget(VentanaLogin)     # index 0
stack.addWidget(VentanaPrincipal) # index 1
stack.addWidget(VentanaJuego)     # index 2
stack.addWidget(VentanaHistorial) # index 3
stack.setFixedSize(420, 460)
stack.show()

# ---------------- LOGIN ----------------
# --- CAMBIO ESTÉTICO: fondo degradado y tarjeta central (glass) ---
VentanaLogin.setStyleSheet("""
    QWidget {
        background: qlineargradient(spread:pad, x1:0,y1:0, x2:1,y2:1, stop:0 #0f1724, stop:1 #0b1220);
    }
""")

L_login = QVBoxLayout()

card_login = QFrame()
card_login.setObjectName("card")
card_login.setFixedWidth(360)
card_login_layout = QVBoxLayout(card_login)
card_login_layout.setSpacing(12)
card_login_layout.setContentsMargins(18, 18, 18, 18)

lbl_welcome = QLabel("BIENVENIDO")
lbl_welcome.setObjectName("title")
lbl_welcome.setAlignment(Qt.AlignCenter)

lbl_ingresar = QLabel("Ingresa tu nombre")
lbl_ingresar.setObjectName("subtitle")
lbl_ingresar.setAlignment(Qt.AlignCenter)

txt_nombre = QLineEdit()
txt_nombre.setPlaceholderText("Tu nombre...")
txt_nombre.setFixedHeight(44)
txt_nombre.setAlignment(Qt.AlignCenter)
txt_nombre.setStyleSheet("""
    QLineEdit {
        color: white;
        font-size: 16px;
    }
""")


btn_ingresar = QPushButton("Ingresar")
btn_ingresar.setFixedHeight(44)
btn_ingresar.setStyleSheet("""
    QPushButton {
        color: white;
        font-size: 16px;
    }
""")

card_login_layout.addWidget(lbl_welcome)
card_login_layout.addWidget(lbl_ingresar)
card_login_layout.addWidget(txt_nombre)
card_login_layout.addWidget(btn_ingresar)

L_login.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
L_login.addWidget(card_login, alignment=Qt.AlignCenter)
L_login.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
VentanaLogin.setLayout(L_login)
# --- FIN CAMBIO ESTÉTICO ---

# ---------------- PANTALLA PRINCIPAL ----------------

card_main = QFrame()
card_main.setObjectName("card")
card_main.setFixedWidth(720)
card_main_layout = QVBoxLayout(card_main)
card_main_layout.setSpacing(16)
card_main_layout.setContentsMargins(20, 20, 20, 20)

lbl_main = QLabel("")  # will be set after login
lbl_main.setObjectName("title")
lbl_main.setAlignment(Qt.AlignCenter)

btn_jugar = QPushButton("🎮 Jugar")
btn_jugar.setFixedWidth(220)
btn_jugar.setFixedHeight(44)

btn_historial = QPushButton("📜 Historial")
btn_historial.setFixedWidth(220)
btn_historial.setFixedHeight(44)

h_buttons = QHBoxLayout()
h_buttons.addStretch()
h_buttons.addWidget(btn_jugar)
h_buttons.addSpacing(18)
h_buttons.addWidget(btn_historial)
h_buttons.addStretch()

card_main_layout.addWidget(lbl_main)
card_main_layout.addLayout(h_buttons)

L_principal = QVBoxLayout()
L_principal.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
L_principal.addWidget(card_main, alignment=Qt.AlignCenter)
L_principal.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
VentanaPrincipal.setLayout(L_principal)

# ---------------- PANTALLA JUEGO ----------------
card_game = QFrame()
card_game.setObjectName("card")
card_game.setFixedWidth(820)
card_game_layout = QHBoxLayout(card_game)
card_game_layout.setContentsMargins(18, 18, 18, 18)
card_game_layout.setSpacing(18)

# Left column: input + controls
left_col = QVBoxLayout()
lbl_intentos = QLabel("Te quedan 0 intentos")
lbl_intentos.setObjectName("subtitle")
lbl_intentos.setAlignment(Qt.AlignCenter)
lbl_intentos.setFixedHeight(30)

txt_num = QLineEdit()
txt_num.setPlaceholderText("Número de 4 dígitos sin repetir")
txt_num.setFixedHeight(44)
txt_num.setAlignment(Qt.AlignCenter)

btn_ingresar_num = QPushButton("Ingresar")
btn_ingresar_num.setFixedHeight(44)

# botón Volver exclusivo para la ventana de JUEGO (no reutilizado)
btn_volver_juego = QPushButton("Volver")
btn_volver_juego.setFixedWidth(180)
btn_volver_juego.setFixedHeight(40)
btn_volver_juego.setStyleSheet("""
    QPushButton {
        color: black;
        font-size: 16px;
    }
""")


left_col.addWidget(lbl_intentos)
left_col.addSpacing(12)
left_col.addWidget(txt_num)
left_col.addWidget(btn_ingresar_num)
left_col.addSpacing(10)
left_col.addWidget(btn_volver_juego)
left_col.addStretch()

# Right column: registro de intentos
right_col = QVBoxLayout()
lbl_registro = QLabel("Registro:")
lbl_registro.setObjectName("subtitle")
lbl_registro.setAlignment(Qt.AlignCenter)

# create 10 labels for the log (monospace)
registro_labels = []
mono = QFont("Consolas", 11)
for i in range(10):
    l = QLabel("")
    l.setFont(mono)
    l.setAlignment(Qt.AlignLeft)
    registro_labels.append(l)
    right_col.addWidget(l)

right_col.insertWidget(0, lbl_registro)
right_col.addStretch()

card_game_layout.addLayout(left_col, 1)
card_game_layout.addLayout(right_col, 2)

L_game = QVBoxLayout()
L_game.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
L_game.addWidget(card_game, alignment=Qt.AlignCenter)
L_game.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
VentanaJuego.setLayout(L_game)

# ---------------- PANTALLA HISTORIAL ----------------
card_hist = QFrame()
card_hist.setObjectName("card")
card_hist.setFixedWidth(820)
card_hist_layout = QVBoxLayout(card_hist)
card_hist_layout.setContentsMargins(18, 18, 18, 18)
card_hist_layout.setSpacing(12)

lbl_hist = QLabel("HISTORIAL")
lbl_hist.setObjectName("title")
lbl_hist.setAlignment(Qt.AlignCenter)

tabla = QTableWidget()
tabla.setRowCount(0)
tabla.setColumnCount(5)  # Nombre, Fecha, Resultado, Número secreto, Intentos
tabla.setHorizontalHeaderLabels(["Nombre", "Fecha", "Resultado", "Número secreto", "Intentos"])
tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
tabla.setSelectionBehavior(QAbstractItemView.SelectRows)
tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
tabla.verticalHeader().setVisible(False)
tabla.setAlternatingRowColors(True)


btn_volver_hist = QPushButton("Volver")
btn_volver_hist.setFixedWidth(180)
btn_volver_hist.setFixedHeight(40)
btn_volver_hist.setStyleSheet("""
    QPushButton {
        color: black;
        font-size: 16px;
    }
""")

card_hist_layout.addWidget(lbl_hist)
card_hist_layout.addWidget(tabla)
card_hist_layout.addSpacing(8)
card_hist_layout.addWidget(btn_volver_hist)  
L_hist = QVBoxLayout()
L_hist.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
L_hist.addWidget(card_hist, alignment=Qt.AlignCenter)
L_hist.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
VentanaHistorial.setLayout(L_hist)

# ---------------- Variables juego ----------------
# Initialize state variables similar to tu versión
intentos = 10
x_index = 0
lista_reg = [""] * 10
nombre = ""  # will be set on login
codigo = random.sample(range(10), 4)  # secret code

# --- CAMBIO FUNCIONAL: reset/restart game when pressing 'Jugar' ---
def start_new_game():
    global intentos, x_index, lista_reg, codigo
    intentos = 10
    x_index = 0
    lista_reg = [""] * 10
    codigo = random.sample(range(10), 4)
    txt_num.setDisabled(False)
    btn_ingresar_num.setDisabled(False)
    txt_num.clear()
    lbl_intentos.setText(f"Te quedan {intentos} intentos")
    # clear registro labels
    for lbl in registro_labels:
        lbl.setText("")
    # make sure stack and sizes are correct
    stack.setFixedSize(900, 600)
    stack.setCurrentIndex(2)

# --- CAMBIO FUNCIONAL: cargar historial desde archivo al iniciar la app ---
def load_historial():
    if not HISTORIAL_FILE.exists():
        return
    try:
        with HISTORIAL_FILE.open("r", encoding="utf-8") as f:
            for line in f:
                # se espera formato: 'YYYY-MM-DD - Nombre: nombre - Numero secreto: 1234 - Intentos: N - Resultado: Gano/Perdio'
                # hacemos parse simple: tomamos los campos separados por ' - '
                parts = [p.strip() for p in line.split(" - ")]
                if len(parts) >= 5:
                    fecha = parts[0]
                    # extraer nombre: 'Nombre: X' o 'nombre: X'
                    nombre_part = parts[1].split(":", 1)[1].strip() if ":" in parts[1] else ""
                    numsecreto_part = parts[2].split(":", 1)[1].strip() if ":" in parts[2] else ""
                    intentos_part = ""
                    resultado_part = ""
                    # buscar Intentos y Resultado en las partes restantes
                    for p in parts[3:]:
                        if p.lower().startswith("intentos"):
                            intentos_part = p.split(":", 1)[1].strip() if ":" in p else ""
                        if p.lower().startswith("resultado"):
                            resultado_part = p.split(":", 1)[1].strip() if ":" in p else ""
                    fila = tabla.rowCount()
                    tabla.insertRow(fila)
                    tabla.setItem(fila, 0, QTableWidgetItem(nombre_part))
                    tabla.setItem(fila, 1, QTableWidgetItem(fecha))
                    tabla.setItem(fila, 2, QTableWidgetItem(resultado_part))
                    tabla.setItem(fila, 3, QTableWidgetItem(numsecreto_part))
                    tabla.setItem(fila, 4, QTableWidgetItem(intentos_part))
    except Exception as e:
        print("No se pudo cargar historial:", e)

# ---------------- Lógica del juego (igual que tu versión, con integraciones) ----------------
def jugar():
    global intentos, x_index, lista_reg
    entrada = txt_num.text().strip()

    # Validar
    if not entrada.isdigit() or len(entrada) != 4:
        txt_num.clear()
        txt_num.setPlaceholderText("Debes poner 4 dígitos")
        return
    if len(set(entrada)) != 4:
        txt_num.clear()
        txt_num.setPlaceholderText("Los dígitos no deben repetirse")
        return

    famas = 0
    puntos = 0
    listaNum = [int(d) for d in entrada]

    for i in range(4):
        if listaNum[i] == codigo[i]:
            famas += 1
        elif listaNum[i] in codigo:
            puntos += 1

    intentos -= 1
    lbl_intentos.setText(f"Te quedan {intentos} intentos")

    if x_index < len(lista_reg):
        lista_reg[x_index] = f"{x_index+1}) {entrada} → famas = {famas}, puntos = {puntos}"
        # actualizar labels
        for i, txt in enumerate(lista_reg):
            registro_labels[i].setText(txt)
        x_index += 1

    if famas == 4:
        lbl_intentos.setText("¡Ganaste!")
        txt_num.setDisabled(True)
        btn_ingresar_num.setDisabled(True)
        resultado = "Ganó"
    elif intentos == 0:
        lbl_intentos.setText(f"Perdiste, el número era {''.join(map(str, codigo))}")
        txt_num.setDisabled(True)
        btn_ingresar_num.setDisabled(True)
        resultado = "Perdió"
    else:
        resultado = None

    # Si terminó (ganó o perdió) guardo en la tabla y archivo
    if resultado is not None:
        try:
            with HISTORIAL_FILE.open("a", encoding="utf-8") as archivo:
                fila = tabla.rowCount()
                tabla.insertRow(fila)
                tabla.setItem(fila, 0, QTableWidgetItem(nombre))
                tabla.setItem(fila, 1, QTableWidgetItem(hoy))
                tabla.setItem(fila, 2, QTableWidgetItem(resultado))
                tabla.setItem(fila, 3, QTableWidgetItem(''.join(map(str, codigo))))
                tabla.setItem(fila, 4, QTableWidgetItem(str(10 - intentos)))
                archivo.write(f"{hoy} - Nombre: {nombre} - Numero secreto: {''.join(map(str, codigo))} - Intentos: {10 - intentos} - Resultado: {resultado}\\n")
        except Exception as e:
            # No interrumpimos la app por un fallo al guardar, pero lo informamos en consola
            print("Error guardando historial:", e)

    txt_num.clear()

# ---------------- Conexiones ----------------
# Login: validar y cambiar a principal
def ingresar():
    global nombre
    if txt_nombre.text().strip() == "":
        lbl_ingresar.setText("Pon tu nombre para ingresar")
        return
    nombre = txt_nombre.text().strip()
    lbl_main.setText(f"Hola {nombre}, ¿qué quieres hacer?")
    # ajustar tamaño del stack para pantallas grandes
    stack.setFixedSize(900, 600)
    stack.setCurrentIndex(1)

btn_ingresar.clicked.connect(ingresar)
btn_jugar.clicked.connect(start_new_game)
btn_historial.clicked.connect(lambda: (stack.setFixedSize(900,600), stack.setCurrentIndex(3)))
btn_volver_juego.clicked.connect(lambda: stack.setCurrentIndex(1))
btn_volver_hist.clicked.connect(lambda: stack.setCurrentIndex(1))

btn_ingresar_num.clicked.connect(jugar)

# ---------------- Inicialización ----------------
txt_nombre.setFocus()
app.setFont(QFont("Segoe UI", 10))

# Cargo historial previo en la tabla (si existe)
load_historial()

# Ejecutar app
if __name__ == "__main__":
    sys.exit(app.exec())
