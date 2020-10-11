
n,d,r=input().split(" ")
n=int(n)
d=int(d)
r=int(r)
l=[]

while n != 0 and d != 0 and r!= 0:
	a = input().split(" ")
	b = input().split(" ")
	a.sort()
	b.sort(reverse=True) 
	t=0
	for i in range(n):
		soma = int(a[i]) + int(b[i])
		maximo = max(soma - d , 0)
		t+= maximo * r
	l.append(t)
	n,d,r=input().split(" ")
	n=int(n)
	d=int(d)
	r=int(r)
	

for i in range(len(l)):
	print(l[i])	
