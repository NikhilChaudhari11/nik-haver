#Delete specific string from a text file.
input_dic_name = input('Dictionary Name: ')
input_file_name = input('File Name: ')
output_file_name = input('Output File Name: ')

input_dic = open(input_dic_name,'r')
dic_file = input_dic.read()
input_dic.close

input_file = open(input_file_name,'r')
file_data = input_file.read()
input_file.close


final_file = open(output_file_name,'w')

input_list = dic_file.split()

for line in input_list:
	new_file = file_data.replace(line,"")
	file_data = new_file

final_file.write(new_file)

final_file.close
