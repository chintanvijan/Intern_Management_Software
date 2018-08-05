import pandas as pd
#i=0
def upd(i):
	elements=[]
	df = pd.read_csv("notconfirmed.csv")
	for j in range(0,5):
		elements.append(df.iloc[i][j])
	elements[0]=str(elements[0])
	elements[2]=str(elements[2])
	elements[4]=str(elements[4])
	return elements
def next(i):
	i = i+1
	return i
	#t=upd(i)
	#return t
def prev(i):
	i=i-1
	return i
	#upd(i)
def sub(i,j,n):
	elements=[]
	df = pd.read_csv("notconfirmed.csv")
	if i==0 and j==1:
		t1=df.iloc[n][4]+1
	if i==1:
		t1=df.iloc[n][4]+1
		t2="confirmed"
		elements.append(df.iloc[n][0])
		elements.append(df.iloc[n][1])
		elements.append(df.iloc[n][2])
		elements.append(t2)
		elements.append(t1)
		elements[0]=str(elements[0])
		elements[2]=str(elements[2])
		elements[4]=str(elements[4])
		stri = elements[0] + "," + elements[1] + "," + elements[2] +"," +elements[3] + "," + elements[4] +"\n"
		fi = open("confirmed.csv","a")
		fi.write(stri)
		fi.close()
		elements = []
		df.drop(n)
		fi = open("notconfirmed.csv","w")
		stri = "Id,Email,pno,status,calls"
		fi.write(stri)

		fi.close()

















