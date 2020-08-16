# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. 
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских 
# букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().



def int_func(text):
	text = text.split()
	return ' '.join([word.title() for word in text])

#ручной вариант title()
ord_Z = ord('Z')
ord_A = ord('A')

def capitalize_word(word):
	first_ord = ord(word[0])
	if not (ord_A <= first_ord <= ord_Z):
		word = chr(first_ord - 32) + word[1:]
	return word

#принимаем и обрабатываем строку с помощью написанной ранее функции
text = input('Введите строку, слова в которой разделены пробелами: ')
for word in text.split():
	if ord(list(word)[0]) not in range(ord('a'),ord('z')):
		ok = False
		break
	else:
		ok = True

if ok == True:
	print(f'Исходая строка с капитализацией слов: {int_func(text)}')
else:
	print('Каждое слово должно состоять из латинских букв в нижнем регистре')



