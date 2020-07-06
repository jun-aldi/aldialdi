#Create a function that returns true if 
#a given inequality expression is correct and false otherwise.
#example:
#correct_signs("3 < 7 < 11") ➞ True
#correct_signs("13 > 44 > 33 > 1") ➞ False
#correct_signs("1 < 2 < 6 < 9 > 3") ➞ True

def correct_signs(txt):
	return eval(txt)

print (correct_signs("9 < 10 < 11"))

#fungsi eval() berfungsi untuk memparsing (menguraikan) 
#string ekspresi yang dilewatkan ke dalamnya, dan menjalankannya sebagai ekspresi Python murni.
#https://www.pythonindo.com/fungsi-eval/
