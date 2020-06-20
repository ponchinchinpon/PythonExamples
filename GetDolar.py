from urllib.request import urlopen
from termcolor import colored



def imprimir(cadena):
    a = cadena.split('$')
    b = a[1].split('<')
    c = b[0]
    d = c.split(' ')
    print(colored(d[1], 'red'))



with urlopen('https://www.dolarhoy.com/cotizaciondolarblue') as response:
	story_words = []

	for line in response:
		linea = line.decode('utf-8')        
		if '<span class="pull-right">' in linea: imprimir(linea)






	    
