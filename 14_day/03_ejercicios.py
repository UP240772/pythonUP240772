#Ordenar países por nombre, por capital, por población
import countries as paises
def obtenerNombre(pais):
    return pais["name"]
def obtenerCapital(pais):
    return pais["capital"]
def obtenerPoblacion(pais):
    return pais["population"]
def ordenarPorNombre(paises):
    return sorted(paises, key=obtenerNombre)
def ordenarPorCapital(paises):
    return sorted(paises, key=obtenerCapital)
def ordenarPorPoblacion(paises, reverse=False):
    return sorted(paises, key=obtenerPoblacion, reverse=reverse)
paisesLista = paises.paises  
ordenadoPorNombre = ordenarPorNombre(paisesLista)
print("\nOrdenado por nombre:")
for pais in ordenadoPorNombre:
    print(pais["name"])
ordenadoPorCapital = ordenarPorCapital(paisesLista)
print("\nOrdenado por capital:")
for pais in ordenadoPorCapital:
    print(pais["capital"])
ordenadoPorPoblacion = ordenarPorPoblacion(paisesLista, reverse=True)
print("\nOrdenado por población (de mayor a menor):")
for pais in ordenadoPorPoblacion:
    print(f"{pais['name']} - {pais['population']}")

#Clasifique los diez idiomas más hablados por ubicación.
from collections import Counter

def contarTop10Idiomas():
    idiomas = []
    for pais in paises.paises:  
        if "languages" in pais:  
            idiomas.extend(pais["languages"]) 
    top10Idiomas = Counter(idiomas).most_common(10)
    return top10Idiomas
def mostrarTop10Idiomas():
    top10Idiomas = contarTop10Idiomas()
    print("Los 10 idiomas más hablados globalmente son:")
    for idioma, count in top10Idiomas:
        print(f"{idioma}: {count}")
mostrarTop10Idiomas()

#Clasifique los diez países más poblados.
def clasificarPaisesMasPoblados():
    paisesOrdenados = sorted(paises.paises, key=lambda pais: pais["population"], reverse=True)
    return paisesOrdenados[:10]
def mostrarTop10PaisesMasPoblados():
    top10Paises = clasificarPaisesMasPoblados()
    print("Los 10 países más poblados son:")
    for pais in top10Paises:
        print(f"{pais['name']}: {pais['population']}")
mostrarTop10PaisesMasPoblados()

print("revisado")