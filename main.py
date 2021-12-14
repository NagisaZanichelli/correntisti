# D'Ippolito Eleonora, Zanichelli Stella  5^F 14/12/21
# Programma correntisti con stampa su file

# Importazione delle funzioni necessarie
import csv
from datetime import datetime

# Lettura dati anagrafici e creazione dizionario utenti

# Apertura file
with open("Anagrafica_conti.csv") as file:
	csv_list = list(csv.reader(file))

# Creazione e riempimento dizionario "utenti"
utenti = []

for utente in csv_list:
	utenti.append({
		"idConto":utente[0],
		"nome":utente[1],
		"cognome":utente[2]
	})

# Lettura dati di saldo e creazione dizionario saldi

# Apertura file
with open("Saldo_conti.csv") as file:
	csv_list = list(csv.reader(file))

# Creazione e riempimento dizionario "saldi"
saldi = []

for conto in csv_list:
	saldi.append({
		"idConto":conto[0],
		"saldo":conto[1],
		"timestamp":conto[2]
	})

# Definizione funzione stampa(lista)
def stampa(lista_utenti):
	 
	#stampa su file
	with open("Anagrafica_conti.csv", "w") as file:
		file.write("id, nome, cognome\n")
		for utente in lista_utenti:
			file.write(str(utente["id"])+", "+utente["nome"]+", "+utente["cognome"]+"\n")
	
	#stampa su terminale
	for utente in utenti:
		print("Nome: "+utente.nome, "Cognome: "+utente.cognome, "idConto: "+utente.id)

#da qui considereremo solo la stampa su file
	
#Definizione funzione stampa_conto(int)
def s_conto(idConto):
  with open("Saldo_conti.csv", "w") as file:
    file.write("idConto, saldo, timestamp\n")
    for saldo in saldi:
      file.write(str(saldo["idConto"])+", "+saldo["saldo"]+", "+saldo["timestamp"]+"\n")

# Definizione classe Correntista
class Correntista:
	def __init__(self, nome, cognome, idConto):
	    self.nome=nome
	    self.cognome=cognome
	    self.idConto=idConto

# Definizione funzione nuovo_utente()
def nuovo_utente():
	nome=input("Inserire nome: ")
	cognome=input("Inserire cognome: ")
	idConto=len(saldi)
	c=Correntista(nome, cognome, idConto)
	utenti.append({
		"idConto":c.idConto,
		"Nome":c.nome,
		"Cognome":c.cognome
	})
	saldo_iniziale=input("Inserire saldo iniziale: ")
	saldi.append({
		"idConto":c.idConto,
		"saldo":saldo_iniziale,
		"timestamp":datetime.now()		
	})

# Definizione funzione aggiungi_soldi(int, float)
def aggiungi_soldi(idConto, importo):
	for i in saldi:
		if i.idConto==idConto:
			conto=i
			break
	conto.saldo+=importo

# Definizione funzione rimuovi_soldi(int, float)
def rimuovi_saldo(idConto, importo):
	for i in saldi:
		if i.idConto==idConto:
			conto=i
			break
	if conto.saldo>importo:
		conto.saldo-=importo
		
# Menu su terminale

print("Seleziona l'azione da compiere")
print()
print(" 1. Crea nuovo utente")
print(" 2. Stampa tutti gli utenti")
print(" 3. Stampa un conto")
print(" 4. Versare un importo ad un conto")
print(" 5. Rimuovi un importo da un conto")
print()
azione = int(input())
print()

# Programma in funzione dell'azione scelta dall'utente
if azione == 1:
	nuovo_utente()

elif azione == 2:
	stampa(lista_utenti)

elif azione == 3:
	id = int(input("Inserire id del conto da stampare: "))
	s_conto(id)

elif azione == 4:
	id = int(input("Inserire id del conto a cui versare l'importo: "))
	importo = int(input("Inserire l'importo da versare: "))
	aggiungi_soldi(id, importo)


elif azione == 5:
	id = int(input("Inserire id del conto a cui rimuovere l'importo: "))
	importo = int(input("Inserire l'importo da rimuovere: "))
	rimuovi_soldi(id, importo)


else:
	print("inserimento errato")
