from datetime import datetime 
def registro():
    documento = input("Ingrese su Número de Documento: \n")
    nombre1 = input("Ingrese su Primer Nombre: \n")
    nombre2 = input("Ingrese su Segundo Nombre: \n")
    apellido1 = input("Ingrese Primer Apellido: \n")
    apellido2 = input("Ingrese Segundo Apellido: \n")
    año_nac = int(input("Ingrese Año de Nacimiento: \n"))
    mes_nac = int(input("Ingrese Mes de Nacimiento:\n"))
    dia_nac = int(input("Ingrese Día de Nacimiento: \n"))
    peso = int(input("Ingrese su peso en Kilogramos: \n"))
    genero = input("Ingrese su genero M/F: \n")
    genero_upper: genero.upper(genero)
    rh = (input("Ingrese su RH (AB+,AB-,A+,A-,B+,B-,O+,O-): \n"))
    rh_upper: rh.upper(rh)
  
    return documento, nombre1, nombre2, apellido1, apellido2, año_nac, mes_nac, dia_nac, peso, genero, rh


def generaClave(nom1, ape1, doc):
    clave = ""
    clave = nom1[:2] + ape1[:2] + doc

    return clave


def inicio_de_sesión(docAlm, docIng, claveAlm, claveIng):
    a = False
    if (docAlm == docIng and claveAlm == claveIng):
        a = True

    return a


def primo(doc):
    p = False
    num = doc[-2:]
    num = int(num)

    if (num > 1 and num < 8):
        if (num == 2 or num == 3 or num == 5 or num == 7):
            p = True
    else:
        if (num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0):
            p = True

        return p

    return p

def calcularEdadPlus (a_nac,m_nac,d_nac):
  hoy=datetime.now()
  añoA=int(hoy.year)
  mesA=int(hoy.month)
  diaA=int(hoy.day)
  
  if d_nac>diaA:
    diaA+=30
    mesA-=1
    dias=diaA-d_nac
  else:
    dias=diaA-d_nac
  if m_nac>mesA:
    mesA+=12
    añoA-=1
    meses=mesA-m_nac
  else:
    meses=mesA-m_nac
  años=añoA-a_nac

  return años,meses,dias

def generarCita(genero,edad,rh,peso,primo):
  if 