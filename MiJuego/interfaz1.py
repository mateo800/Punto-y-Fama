import sys
import random
from datetime import date
from PySide6.QtWidgets import (
    QApplication,  # app principal
    QWidget,       # ventana base
    QLabel,        # etiqueta de texto o imagen
    QPushButton,   # botón
    QLineEdit,     # campo de texto (una línea)
    QVBoxLayout,   # layout vertical
    QHBoxLayout,   # layout horizontal
    QStackedWidget,
    QTableWidget, # tabla
    QHeaderView,
    QTableWidgetItem, # modificaciones de tabla
    QAbstractItemView # para objetos abstractos
)
from PySide6.QtCore import Qt
codigo = random.sample(range(10), 4)
hoy = date.today()
hoy = str(hoy)
app = QApplication(sys.argv)

#creo todas las pestañas *******************************************************************************************************************

VentanaLogin = QWidget()
VentanaPrincipal = QWidget()
VentanaJuego = QWidget()
VentanaHistorial = QWidget()

VentanaLogin.setFixedSize(300,300)
VentanaLogin.setWindowTitle("LOGIN")
VentanaLogin.setStyleSheet("background-color: lightblue")

VentanaPrincipal.setFixedSize(800,500)
VentanaPrincipal.setWindowTitle("PRINCIPAL")
VentanaPrincipal.setStyleSheet("background-color: lightblue")

VentanaJuego.setFixedSize(800,500)
VentanaJuego.setWindowTitle("JUEGO")
VentanaJuego.setStyleSheet("background-color: lightblue")

VentanaHistorial.setFixedSize(800,500)
VentanaHistorial.setWindowTitle("HISTORIAL")
VentanaHistorial.setStyleSheet("background-color: lightblue")

stack = QStackedWidget()
stack.addWidget(VentanaLogin) # indice 0
stack.addWidget(VentanaPrincipal)   # índice 1
stack.addWidget(VentanaJuego)       # índice 2
stack.addWidget(VentanaHistorial)   # índice 3
stack.setFixedSize(300, 300)
stack.show()

# pestaña del login *******************************************************************************************************************


L_login1 = QVBoxLayout()

E_1 = QLabel("BIENVENIDO")
E_1.setStyleSheet("font-size:18px")
E_1.setAlignment(Qt.AlignCenter)


E_ingresar = QLabel("Ingresa tu nombre")
E_ingresar.setStyleSheet("font-size:18px")
E_ingresar.setAlignment(Qt.AlignCenter)

txt_nombre = QLineEdit()
txt_nombre.setStyleSheet("background-color: lightgray; font-size:18px")
txt_nombre.setFixedHeight(40)
txt_nombre.setAlignment(Qt.AlignTop)


Btn_ingresar = QPushButton("Ingresar")
Btn_ingresar.setStyleSheet("background-color: white; font-size:18px")
Btn_ingresar.setFixedHeight(40)

L_login1.addWidget(E_1)
L_login1.addWidget(E_ingresar)
L_login1.addWidget(txt_nombre)
L_login1.addWidget(Btn_ingresar)

VentanaLogin.setLayout(L_login1)

nombre = ""
def ingresar():
    if txt_nombre.text() == "":
        E_ingresar.setText("Pon tu nombre para ingresar")
    else:
        global nombre
        nombre = txt_nombre.text()
        E_2.setText(f"Hola {nombre} que quieres hacer")
        stack.setFixedSize(800, 500)
        stack.setCurrentIndex(1)
Btn_ingresar.clicked.connect(ingresar)



# ventana principal *******************************************************************************************************************
L_principal1 = QVBoxLayout()


Btn_jugar = QPushButton("Jugar")
Btn_jugar.setStyleSheet("background-color: white; font-size:18px")
Btn_jugar.setFixedHeight(40)
Btn_jugar.setFixedWidth(200)

Btn_historial = QPushButton("Historial")
Btn_historial.setStyleSheet("background-color: white; font-size:18px")
Btn_historial.setFixedHeight(40)
Btn_historial.setFixedWidth(200)

E_2 = QLabel(f'Hola {nombre} que quieres hacer')
E_2.setStyleSheet("font-size:18px")
E_2.setAlignment(Qt.AlignCenter)






L_principal1.addWidget(E_2)
L_principal1.addWidget(Btn_jugar)
L_principal1.addWidget(Btn_historial)



VentanaPrincipal.setLayout(L_principal1)

Btn_jugar.clicked.connect(lambda: stack.setCurrentIndex(2))
Btn_historial.clicked.connect(lambda: stack.setCurrentIndex(3))

#ventana del juego *******************************************************************************************************************
l_juego1 = QVBoxLayout()
l_juego2 = QHBoxLayout()
l_juego3 = QVBoxLayout()
l_juego4 = QVBoxLayout()
l_juego5 = QVBoxLayout()

lista = ["","","","","","","","","",""]

E_intentos = QLabel('Te quedan 0 intentos')
E_intentos.setStyleSheet("font-size:14px")
E_intentos.setAlignment(Qt.AlignCenter)
E_intentos.setFixedWidth(400)
E_intentos.setFixedHeight(40)

E_ganar = QLabel('Te quedan 0 intentos')
E_ganar.setStyleSheet("font-size:14px")
E_ganar.setAlignment(Qt.AlignCenter)
E_ganar.setFixedWidth(400)
E_ganar.setFixedHeight(40)

E_5 = QLabel('Registro:')
E_5.setStyleSheet("font-size:14px")
E_5.setAlignment(Qt.AlignCenter)
E_5.setFixedWidth(400)
E_5.setFixedHeight(40)


E_num1 = QLabel(lista[0])
E_num1.setStyleSheet("font-size:14px")
E_num1.setAlignment(Qt.AlignCenter)

E_num2 = QLabel(lista[1])
E_num2.setStyleSheet("font-size:14px")
E_num2.setAlignment(Qt.AlignCenter)

E_num3 = QLabel(lista[2])
E_num3.setStyleSheet("font-size:14px")
E_num3.setAlignment(Qt.AlignCenter)

E_num4 = QLabel(lista[3])
E_num4.setStyleSheet("font-size:14px")
E_num4.setAlignment(Qt.AlignCenter)

E_num5 = QLabel(lista[4])
E_num5.setStyleSheet("font-size:14px")
E_num5.setAlignment(Qt.AlignCenter)

E_num6 = QLabel(lista[5])
E_num6.setStyleSheet("font-size:14px")
E_num6.setAlignment(Qt.AlignCenter)

E_num7 = QLabel(lista[6])
E_num7.setStyleSheet("font-size:14px")
E_num7.setAlignment(Qt.AlignCenter)

E_num8 = QLabel(lista[7])
E_num8.setStyleSheet("font-size:14px")
E_num8.setAlignment(Qt.AlignCenter)

E_num9 = QLabel(lista[8])
E_num9.setStyleSheet("font-size:14px")
E_num9.setAlignment(Qt.AlignCenter)

E_num10 = QLabel(lista[9])
E_num10.setStyleSheet("font-size:14px")
E_num10.setAlignment(Qt.AlignCenter)

def recorrer():
    E_num1.setText(str((lista[0])))
    E_num2.setText((lista[1]))
    E_num3.setText((lista[2]))
    E_num4.setText((lista[3]))
    E_num5.setText((lista[4]))
    E_num6.setText((lista[5]))
    E_num7.setText((lista[6]))
    E_num8.setText((lista[7]))
    E_num9.setText((lista[8]))
    E_num10.setText((lista[9]))


txt_num = QLineEdit()
txt_num.setStyleSheet("background-color: lightgray; font-size:18px")
txt_num.setFixedHeight(40)
txt_num.setPlaceholderText('Numero de 4 digitos sin repetir')
txt_num.setAlignment(Qt.AlignmentFlag.AlignTop)

Btn_corregir = QPushButton("Ingresar")
Btn_corregir.setStyleSheet("background-color: white; font-size:18px")
Btn_corregir.setFixedHeight(40)

Btn_volver = QPushButton("Volver")
Btn_volver.setStyleSheet("background-color: white; font-size:18px")
Btn_volver.setFixedHeight(40)
Btn_volver.setFixedWidth(200)



intentos = 10
num = 0
x = 0
puntos = 0
famas = 0
estado = ""
E_intentos.setText(f"Te quedan {intentos} intentos")
listaNum= []
def jugar():
    global intentos, x, famas, puntos, estado
    entrada = txt_num.text()

    # Validar que sean dígitos o que ponga un numero distinto de 4 digitos
    if not entrada.isdigit() or len(entrada) != 4:
        txt_num.clear()
        txt_num.setPlaceholderText("Debes poner 4 dígitos")

    # Validar que no se repitan, elimina los caracteres duplicados, asi que sino da 4 es porque alguno se repitio
    if len(set(entrada)) != 4:
        txt_num.clear()
        txt_num.setPlaceholderText("Los dígitos no deben repetirse")

    famas = 0
    puntos = 0
    listaNum = [int(d) for d in entrada]

    for i in range(4):
        if listaNum[i] == codigo[i]:
            famas += 1
        elif listaNum[i] in codigo:
            puntos += 1

    intentos -= 1
    E_intentos.setText(f"Te quedan {intentos} intentos")

    if x < len(lista):
        lista[x] = f"{x+1}) {entrada} → famas = {famas}, puntos = {puntos}"
        recorrer()
        x += 1

    if famas == 4:
        E_intentos.setText("¡Ganaste")
        txt_num.setDisabled(True) # desactiva el cajon
        Btn_corregir.setDisabled(True)

    # Verificar derrota
    elif intentos == 0:
        E_intentos.setText(f"Perdiste, el número era {''.join(map(str, codigo))}") # el join uno la lista en un solo string, y el map convierte cada entero en texto
        txt_num.setDisabled(True)
        Btn_corregir.setDisabled(True)

    if famas == 4 or intentos == 0:
        with open('historialJuego.txt','a') as archivo:
            if famas == 4:
                fila = tabla.rowCount() # creo una fila
                tabla.insertRow(fila) # inserto la fila
                tabla.setItem(fila, 0, QTableWidgetItem(nombre)) 
                tabla.setItem(fila, 1, QTableWidgetItem(hoy)) 
                tabla.setItem(fila, 2, QTableWidgetItem("Ganó"))
                tabla.setItem(fila, 3, QTableWidgetItem(''.join(map(str, codigo))))
                tabla.setItem(fila, 4, QTableWidgetItem(str(10 - intentos)))

                archivo.write(f'{hoy} - Nombre: {nombre} - Numero secreto: {''.join(map(str, codigo))} - Intentos: {10 - intentos} - Resultado: Gano\n')

            else:

                fila = tabla.rowCount() # creo una fila
                tabla.insertRow(fila) # inserto la fila
                tabla.setItem(fila, 0, QTableWidgetItem(nombre)) 
                tabla.setItem(fila, 1, QTableWidgetItem(hoy)) 
                tabla.setItem(fila, 2, QTableWidgetItem("Perdio"))
                tabla.setItem(fila, 3, QTableWidgetItem(''.join(map(str, codigo))))
                tabla.setItem(fila, 4, QTableWidgetItem(str(10 - intentos)))

                archivo.write(f'{hoy} - nombre: {nombre} - Numero secreto: {''.join(map(str, codigo))} - Resultado: Perdio\n')
    txt_num.clear()

Btn_corregir.clicked.connect(jugar)
l_juego3.addWidget(txt_num)
l_juego3.addWidget(Btn_corregir)

l_juego4.addWidget(E_intentos)
l_juego4.addWidget(E_5)
l_juego4.addWidget(E_num1)
l_juego4.addWidget(E_num2)
l_juego4.addWidget(E_num3)
l_juego4.addWidget(E_num4)
l_juego4.addWidget(E_num5)
l_juego4.addWidget(E_num6)
l_juego4.addWidget(E_num7)
l_juego4.addWidget(E_num8)
l_juego4.addWidget(E_num9)
l_juego4.addWidget(E_num10)

l_juego2.addLayout(l_juego3)
l_juego2.addLayout(l_juego4)
l_juego1.addLayout(l_juego2)
l_juego1.addLayout(l_juego5)
l_juego5.addWidget(Btn_volver)

VentanaJuego.setLayout(l_juego1)

Btn_volver.clicked.connect(lambda: stack.setCurrentIndex(1))


#ventana del historial *******************************************************************************************************************
l_historial1 = QVBoxLayout() 

E_3 = QLabel(f'HISTORIAL')
E_3.setStyleSheet("font-size:18px")
E_3.setAlignment(Qt.AlignCenter)

tabla = QTableWidget()
tabla.setRowCount(0)     # Empieza sin filas
tabla.setColumnCount(4)  # columnas  
tabla.setHorizontalHeaderLabels(["Nombre","Fecha", "Resultado", "Número secreto", "Intentos"]) # nombres de ls titulos
tabla.setEditTriggers(QAbstractItemView.NoEditTriggers) # para que la tabla no sea editable


Btn_volver2 = QPushButton("Volver")
Btn_volver2.setStyleSheet("background-color: white; font-size:18px")
Btn_volver2.setFixedHeight(40)
Btn_volver2.setFixedWidth(200)

l_historial1.addWidget(E_3)
l_historial1.addWidget(tabla)
l_historial1.addWidget(Btn_volver2)
VentanaHistorial.setLayout(l_historial1)

Btn_volver2.clicked.connect(lambda: stack.setCurrentIndex(1))


# ejecuto la app *******************************************************************************************************************
app.exec()

