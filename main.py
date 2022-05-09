import FUNCIONES as fun

doc, n1, n2, a1, a2, a_n, m_n, d_n, pe, gen, rh = fun.registro()

clave = fun.generaClave(n1, a1, doc)

doc1 = input("Ingrese su Usuario(Documento): \n")
clave1 = input("Ingrese su Clave: \n")

val = fun.inicio_de_sesión(doc, doc1, clave, clave1)
if (val == True):
    print("Acceso aceptado")
else:
    print("Verifique su número de documento y/o contraseña")

a,m,d=fun.calcularEdadPlus(a_n,m_n,d_n)

cita=fun.generarCita(a_n,m_n,d_n)
print("Su cita será en el mes ",m_n," y el día ",d_n)