import random as r
import time as t
r1 = '0987654321'
r2 = 'qwertyuiopasdfghjklzxcvbnm1234567890'
r21 = 'QWERTYUIOPASDFGHJKLZXCVBNM1234567890'
r22 = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM987654321'
lis1 = [r2,r21,r22]
r3 = r22+r"#$&_-?!+=)(@':%/*¿~™®©¢¥€£[]{}<>^¡`;÷\|¦¬×§¶°"

txt1 = 'how many password you want: '
txt2 = 'ok and how many length: '
print('🦉 owl password'.upper())
print('+ We help you create a strong password\n+ Create your own password')
#print('_'*20)
while True:
	#t.sleep(0.5)
	print()
	print('_'*20)
	print('\nselect one of option:'.title())
	print('0 - quit\n1 - Number password\n2 - number and letters password\n3 - something like NASA password\n4 - info about creator'.title())
	try:
		t.sleep(0.5)
		u = int(input('---> '))
	
	
		if u == 1:
			print('Number'.upper())
	
	#	try:
			print(f'{txt1}')
			u11 = int(input(''))
			print(f'{txt2}')
			u12 = int(input(''))
		#except ValueError:
		#	print('⚠️ Wrong not correct syntax')
		
			print('Password:')
			print('_'*20)
			for i1 in range(u11):
				print('\n')
				t.sleep(0.5)
				for i2 in range(u12):
					#print(x)
					print(r.choice(r1),end ='')
			
			
		if u == 2:
				print('number and letters password'.upper())
		#	try:
				print(f'{txt1}')
				u21 = int(input(''))
				print(f'{txt2}')
				u22 = int(input(''))
				print('one more thing:\n1 - lower letter\n2 - upper letter\n3 - both\n4 - idk random')
				t.sleep(0.5)
				u23 = int(input('---> '))
		#	except ValueError:
			#	print('⚠️ Wrong not correct syntax')
			
				print('Password:')
				print('_'*20)
				for i1 in range(u21):
					print('\n')
					t.sleep(0.5)
					for i2 in range(u22):
						if u23 == 1:
							print(r.choice(r2),end='')
						if u23 == 2:
							print(r.choice(r21),end='')
						if u23 == 3:
							print(r.choice(r22),end='')
						if u23 == 4:
							print(r.choice(r.choice(lis1)),end='')
					
		if u == 3:
				print('Nasa password'.upper())
		
	#		try:
				print(f'{txt1}')
				u31 = int(input(''))
				print(f'{txt2}')
				print('+ we recommended you to send more than 30')
				u32 = int(input(''))
		#	except ValueError:
		#		print('⚠️ Wrong not correct syntax')
				
				print('Password:')
				print('_'*20)
				for i1 in range(u31):
					print('\n')
					t.sleep(0.5)
					for i2 in range(u32):
						print(r.choice(r3),end='')
				
				
		if u == 4:
				t.sleep(0.3)
				print('_'*20)
				t.sleep(0.4)
				print('\n🦉Owl Password\nThanks for use my program <3\nyou can send your feedback in telegram\n@xyung')
		
		
		if u == 0:
				t.sleep(0.5)
				print('I hope you enjoy\nbye')
				break
	
			
	except ValueError:
		t.sleep(0.2)
		print('⚠️ Wrong just send number ⚠️')
	
	except NameError:
		t.sleep(0.2)
		print('⚠️ Wrong just send number ⚠️')
	
	
