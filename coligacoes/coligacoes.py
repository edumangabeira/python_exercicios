'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By 

option = webdriver.ChromeOptions()
option.add_argument(' — incognito') # entra em modo anônimo
driver = webdriver.Chrome("/home/edu/coligacoes/chromedriver", chrome_options = option)
driver.implicitly_wait(10) # aguarda 10 segundos antes de acessar qqr elemento
url = driver.get("https://public.flourish.studio/visualisation/119451/?utm_source=showcase&utm_campaign=visualisation/119451")

#elements = driver.find_elements_by_class_name('party_text')
# lista = [element.get_atribbute("innerHTML") for element in elements if(element.get_atribbute("class") == "party_text")]
i = 1
while True:
	try:
		str_i = str(i)
		element = driver.find_elements_by_xpath("//*[@id='table']/tr[%s]/td[1]/span[2]", srt_i)
		print(element.text)
		i = i+1
	except:
		break

	
	{
	lists = driver.find_elements_by_class_name('u-linkComplex-target')

    bot_screen_name = ""
    for listitem in lists:
        if (listitem.get_attribute("class") == "u-linkComplex-target"):
            bot_screen_name = listitem.get_attribute("innerHTML")
            
            break
    return bot_screen_name
	}

congress_14 ='before_text' #table > tr:nth-child(12) > td.party > span.party_text
congress_18 ='after_text' '//*[@id="table"]/tr[11]/td[1]/span[2]'
#'//*[@id="table"]/tr[20]/td[1]/span[2]'
congress_diff = "diff_text"
# print(lista)

time.sleep(15)
driver.quit()

'''
import csv
import os

def file_block(fp, number_of_blocks, block):

	# ---snip by Nicolau Werneck 

    '''
    A generator that splits a file into blocks and iterates
    over the lines of one of the blocks.
 
    '''
    assert 0 <= block and block < number_of_blocks
    assert 0 < number_of_blocks
 
    fp.seek(0,2)
    file_size = fp.tell()
 
    ini = file_size * block / number_of_blocks
    end = file_size * (1 + block) / number_of_blocks
 
    if ini <= 0:
        fp.seek(0)
    else:
        fp.seek(ini-1)
        fp.readline()
 
    while fp.tell() < end:
        yield fp.readline()
 
if __name__ == '__main__':

	number_of_chunks = 4
	arq_txt = "v_confuso.txt"
	arq_csv = "senado.csv"
    	
	with open(arq_txt, "r") as arq_1:
		'''arq1_lines = arq_1.readlines()
		arq1_lines = [line.replace(' ', '') for line in arq1_lines]
		'''
		with open(arq_csv, "w") as arq_2:
			writer = csv.writer(arq_2)
			writer.writerow(['Party','2018 Elections', '2014 Elections', 'Balance'])
			for chunk_number in range(number_of_chunks):
				for row in file_block(arq_1, number_of_chunks, chunk_number):
					writer.writerow(row)
