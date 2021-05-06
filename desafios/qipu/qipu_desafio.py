__author__     = 'Eduardo Freire Mangabeira'
__maintainer__ = 'Eduardo Freire Mangabeira'
__email__      = 'edu.mangaba@gmail.com'


def read_entrada(arquivo):
	'''
	read_entrada(arquivo)

	Recebe o arquivo .txt com valores e os retorna numa lista.
	'''
	with open(arquivo, 'r') as entrada:
		valores = entrada.readlines()
	return valores

def split_valor(valor):
	'''
	split_valor(valor)

	Divide um valor no formato 'XXXX,XX' em reais e centavos.
	Retorna duas listas com os digitos do valor separado em reais e centavos.

	Aceita valores sempre com dois dígitos após a vírgula e 
	com até 9 dígitos antes da vírgula.
	'''
	valor = valor.split(',')
	reais, centavos = valor[0], valor[1]

	try:
		int(reais)
		int(centavos)
	except ValueError as e:
		print("Valor inválido, o formato aceito é XXXX, XX")
		print(e)

	if len(reais) > 9:
		raise Exception('Erro: reais devem ter no máximo nove dígitos.')

	while len(centavos) < 2:
		centavos = centavos + '0'

	while len(reais) < 9:
		reais = '0' + reais

	reais_list    = [digito for digito in reais]
	centavos_list = [digito for digito in centavos]

	return reais_list, centavos_list

def converte_valor(reais, centavos):
	'''
	converte_valor(reais, centavos)

	Lê valores em reais e centavos e os escreve por extenso.
	
	Ex: 
	1,00    => um real.
	1000,54 => mil reais e cinquenta e quatro centavos.
	'''
	unidades = {'1':'um', '2':'dois', '3':'três', '4':'quatro', '5':'cinco', 
	'6':'seis', '7':'sete','8':'oito', '9':'nove'}

	dez_     = {'11':'onze', '12':'doze', '13':'treze', '14':'catorze',
	'15':'quinze', '16':'dezesseis', '17':'dezessete', '18':'dezoito', 
	'19':'dezenove'}

	dezenas  = {'10':'dez', '20':'vinte', '30':'trinta', '40':'quarenta', 
	'50':'cinquenta', '60':'sessenta','70':'setenta', '80':'oitenta', 
	'90':'noventa'}

	centenas = {'100':'cem', '200':'duzentos',
	'300':'trezentos', '400':'quatrocentos', '500':'quinhentos', 
	'600':'seiscentos','700':'setecentos', '800':'oitocentos', 
	'900':'novecentos'}

	# centavos
	## dezenas
	if int(centavos[0]) == 1 and int(centavos[1]) > 0:
		centavos = _dez.get(''.join(centavos))

	elif int(centavos[0]) > 0 and int(centavos[1]) == 0:
		centavos = dezenas.get(centavos[0]+'0')

	elif int(centavos[0]) > 0 and int(centavos[1]) > 0:
		centavos = dezenas.get(centavos[0]+'0') + ' e ' + unidades.get(centavos[1])
	## unidades
	elif int(centavos[0]) == 0 and int(centavos[1]) > 0:
		centavos = unidades.get(centavos[1])

	elif int(centavos[0]) == 0 and int(centavos[1]) == 0:
		centavos = 'zero'
	# ---------------------------------------------------
	# reais
	# dividir em trios xxx.xxx.xxx
	# milhões  --->  reais[0, 1, 2]
	# milhares --->  reais[3, 4, 5]
	# centenas --->  reais[6, 7, 8]
	reais_trios = [None, None, None]

	# percorre índices pelo inicio de cada trio.
	trio = 0
	# flag para indicar se um trio começa com 1
	flag = [0, 0, 0]
	for i in (0, 3, 6):
		# cento e ...
		cent, dezen, unid = reais[i], reais[i+1], reais[i+2]
		if int(cent) == 1 and int(dezen) > 0 and int(unid) == 0:
			reais_trios[trio] = 'cento e ' + dezenas.get(dezen+'0')

		elif int(cent) == 1 and int(dezen) == 0 and int(unid) > 0:
			reais_trios[trio] = 'cento e ' + unidades.get(unid)

		elif int(cent) == 1 and int(dezen) > 1 and int(unid) > 0:
			reais_trios[trio] = 'cento e ' + dezenas.get(dezen+'0') + ' e ' + unidades.get(unid)

		elif int(cent) == 1 and int(dezen) == 1 and int(unid) > 0:
			reais_trios[trio] = 'cento e ' + dez_.get(dezen + unid)

		# centenas
		elif int(cent) > 0 and int(dezen) == 0 and int(unid) == 0:
			reais_trios[trio] = centenas.get(cent + '00')

		elif int(cent) > 1 and int(dezen) > 0 and int(unid) == 0:
			reais_trios[trio] = centenas.get(cent+'00') + ' e ' + dezenas.get(dezen+'0')

		elif int(cent) > 1 and int(dezen) == 0 and int(unid) > 0:
			reais_trios[trio] = centenas.get(cent+'00') + ' e ' + unidades.get(unid)


		elif int(cent) > 1 and int(dezen) > 1 and int(unid) > 0:
			reais_trios[trio] = centenas.get(cent+'00') + ' e ' + dezenas.get(dezen+'0') + ' e ' + unidades.get(unid)

		elif int(cent) > 1 and int(dezen) == 1 and int(unid) > 0:
			reais_trios[trio] = centenas.get(cent+'00') + ' e ' + dez_.get(dezen + unid)

		# dezenas
		elif int(cent) == 0 and int(dezen) > 1 and int(unid) > 0:
			reais_trios[trio] = dezenas.get(dezen+'0') + ' e ' + unidades.get(unid)

		elif int(cent) == 0 and int(dezen) > 1 and int(unid) == 0:
			reais_trios[trio] = dezenas.get(dezen+'0')

		elif int(cent) == 0 and int(dezen) == 1 and int(unid) > 0:
			reais_trios[trio] = dez_.get(dezen + unid)

		# unidades
		elif int(cent) == 0 and int(dezen) == 0 and int(unid) > 0:
			reais_trios[trio] = unidades.get(unid)
			if reais_trios[trio] == 1:
				flag[trio] = 1

		trio = trio + 1
	# trios XXX.XXX.XXX
	milhoes, milhares, centenas_ = reais_trios[0], reais_trios[1], reais_trios[2]

	# milhoes
	if milhoes is not None and milhares is None and centenas_ is None:
		if flag[0] == 1:
			reais = f'{milhoes} milhão'
		else:
			reais = f'{milhoes} milhões'

	elif milhoes is not None and milhares is None and centenas_ is not None:
		if flag[0] == 1:
			reais =  f'{milhoes} milhão, {centenas_}'
		else:
			reais = f'{milhoes} milhões, {centenas_}'

	elif milhoes is not None and milhares is not None and centenas_ is None:
		if flag[0] == 1:
			reais =  f'{milhoes} milhão, {milhares} mil'
		else:
			reais = f'{milhoes} milhões, {milhares} mil'

	elif milhoes is not None and milhares is not None and centenas_ is not None:
		if flag[0] == 1:
			reais =  f'{milhoes} milhão, um mil'
		else:
			reais = f'{milhoes} milhões e {milhares} mil'

	# milhares
	elif milhoes is None and milhares is not None and centenas_ is not None:
		if flag[1] == 1:
			reais =  f'mil, {centenas_}'
		else:
			reais = f'{milhares} mil e {centenas_}'

	elif milhoes is None and milhares is not None and centenas_ is None:
		if flag[1] == 1:
			reais =  f'mil'
		else:
			reais = f'{milhares} mil'

	# centenas_
	elif milhoes is None and milhares is None and centenas_ is not None:
		reais = centenas_
	else:
		reais = 'zero'

	# formatação do texto
	if reais in ['um'] and centavos in ['um']:
		valor_convertido = f'{reais} real e {centavos} centavo.'

	if reais in ['um'] and centavos in ['zero']:
		valor_convertido = f'{reais} real'

	elif reais in ['zero'] and centavos in ['zero']:
		valor_convertido = f'zero real'

	elif reais in ['um'] and centavos not in ['zero', 'um']:
		valor_convertido = f'{reais} real e {centavos} centavos.'

	elif reais in ['zero'] and centavos not in ['zero', 'um']:
		valor_convertido = f'{centavos} centavos.'

	elif reais not in ['zero', 'um'] and centavos in ['zero']:
		valor_convertido = f'{reais} reais.'

	else:
		valor_convertido = f'{reais} reais e {centavos} centavos.'

	return valor_convertido


def write_saida(arquivo, valores):
	'''
	write_saida(arquivo, valores)

	Recebe uma lista com valores e os salva por extenso num arquivo .txt.
	'''
	with open(arquivo, 'w') as saida:
		for valor in valores:
			valor = valor.replace('\n','')
			valor_extenso = converte_valor(split_valor(valor)[0], split_valor(valor)[1])
			saida.write(f'{valor} - {valor_extenso} \n')

def main():
	'''
	lê valores em reais(R$) de um arquivo .txt e os escreve novamente e também por extenso em outro .txt.
	'''
	entrada, saida = 'entrada.txt', 'saida.txt'
	try:
		print('Convertendo valores de {arq_entrada} em {arq_saida}... \n')
		write_saida(saida, read_entrada(entrada))
		print('Operação bem sucedida.')
	except:
		print('Aviso: houve um erro ao escrever os valores no novo arquivo.')

if __name__ == '__main__':
	main()
