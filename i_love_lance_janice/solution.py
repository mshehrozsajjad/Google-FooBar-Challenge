def answer(s):
	 result = ""
	 for word in s:
	 	 if not word.islower():
	 	 	result = result +word
	 	 else:
    		  new_word = 122- ord(word)+ (97)
    		  result = result + chr(new_word)
	 return result


