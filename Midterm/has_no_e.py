def has_no_e(in_string):
	for letter in in_string:
		if letter == 'e':
			return False
	return True


print()
test_str = "t*st string without that charact*r"
print(test_str)
print(has_no_e(test_str))
print()
test_str2 = "test string with that character"
print(test_str2)
print(has_no_e(test_str2))
print()
print("===================================================================")
print("          \\\\ gadsby_stripped.txt 'e' character check //          ||")
print("           ===========================================           ||")
print("                                                                 ||")
print("      	      Prints 'TRUE' if line contains no 'e'              ||")
print("               Prints 'FALSE' if line contains 'e'               ||")
print("                                                                 ||")
print("          Also prints number of lines with and w/o               ||")
print("               'e' at the bottom of all output.                  ||")
print("                                                                 ||")
print("NOTE:  We are considering lines to be strings delimited by       ||")
print("       whatever python's newline character is and not lines      ||")
print("       as they might appear in a text editor.                    ||")
print("===================================================================")

print()







line_number = 1 
occurrences_of_e = 0
occurrences_without_e = 0

for line in open('gadsby_stripped.txt'):
	print("Line Number [" + str(line_number) + "]: " + str(has_no_e(line)))
	if(has_no_e(line) == False):
		occurrences_of_e += 1
	elif(has_no_e(line) == True):
		occurrences_without_e += 1

	line_number += 1

print()
print("LINES WITHOUT 'e' =  " + str(occurrences_without_e))
print("LINES WITH 'e' =  " + str(occurrences_of_e))


# Working
