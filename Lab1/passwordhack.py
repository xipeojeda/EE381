import numpy

def password_hack(N, k, m):
	countSuccess = 0
	
	n = 26 ** 4 #total number of passwords that can be created
	for i in range (0,N):
		password = numpy.random.randint(0,n)
		hackedPasswords = numpy.random.randint(0,n,k * m)
		if password in hackedPasswords:
			countSuccess += 1
	
	print('Password: ', password)
	print('Hacked Password Lists: ', hackedPasswords,'\nk = ', k, '\nm = ',m)
	print('Probability of at least one of the words matches the password: ', countSuccess/N, '\n')

#testing below
print(password_hack(1000, 1, 80000))
#using  m=80,000  ;  k=7
print(password_hack(1000, 7, 80000))
#find an m that makes the probability approximately equal to p = 0.5
print(password_hack(1000, 1, 315000))




###class explanation 
#4 lowercase letters --> 26 ^ 4 = total number of passwords = n
#hacker is creating a list of random passwords
#H = [h1, h2,....,hm]