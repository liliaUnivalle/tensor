import csv, operator, random
from decimal import Decimal
import numpy as np

class Cargador:
	
	def __init__(self):
		self.test = []
		self.train = []
		self.clasificador()


	def ramdomEspetial(self,lista):
		lista1 = lista[0]
		lista2 = lista[1]

		listaFinal1 = []
		listaFinal2 = []

		tam= len(lista1) -1
		nums = range(0, tam)
		random.shuffle(nums)
		for i in nums:
			listaFinal1.append(lista1[i])
			listaFinal2.append(lista2[i])

		listaFinal = [listaFinal1,listaFinal2]
		return listaFinal


	def lector(self,archivo):
		with open(archivo) as csvarchivo:
			entry = csv.reader(csvarchivo, delimiter=';')
			seismos = []
			datas = []
			for reg in entry:
				if reg[3] != "None":
					posicion = [0] * 95
					seismo = []
					seismo.append(reg[0][0:4])
					seismo.append(reg[0][5:7])
					seismo.append(reg[0][8:10])
					seismo.append(reg[0][11:13])
					seismo.append(reg[0][14:16])
					lon=reg[1].split(',')
					lat=reg[2].split(',')
					seismo.append(lon[0])
					try:
						seismo.append(lon[1])
					except Exception as e:
						pass
					
					seismo.append(lat[0])

					try:
						seismo.append(lat[1])
					except Exception as e:
						pass
				
					num =  Decimal(reg[3].replace(",",".")) * 10
					p=int(num)
					posicion[p] = 1
					datas.append(posicion)
					seismos.append(seismo)
			result = [seismos,datas]
			return result

	def recolector(self):
		sismos1 = self.lector('2706Choco.csv')
		sismos2= self.lector('3141Valle.csv')
		sismos3 = sismos1[0]+sismos2[0]
		sismos4 = sismos1[1]+sismos2[1]

		sismos5= np.asarray(sismos3,dtype=int)
		sismos6= np.asarray(sismos4,dtype=int)
		sismos = [sismos5,sismos6]
		return sismos

	def clasificador(self):
		tot = self.recolector()
		total = self.ramdomEspetial(tot)

		test1 = total[0][:900]
		test2 = total[1][:900]
		self.test = [test1,test2]
		train1 = total[0][900:]
		train2 = total[1][900:]
		self.train = [train1,train2]

	def randomTest(self, len):
		return self.test[0][:len], self.test[1][:len]
	def trainDatas(self):
		return self.train[0]
	def trainLabels(self):
		return self.train[1]

