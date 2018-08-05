import pandas as pd
def readcsv():
	df = pd.read_csv("Records.csv")
	elements=[]
	for i in range(len(df.Id)):
		for j in range(0,5):
			elements.append(df.iloc[i][j])
		elements[0] = str(elements[0])
		elements[2] = str(elements[2])
		elements[4] = str(elements[4])
		stri = elements[0]+ "," +elements[1]+","+elements[2]+" ," +elements[3]+","+  elements[4]+"\n"
		#print(stri)
		fi = open("notconfirmed.csv","a")
		fi.write(stri)
		fi.close()
		elements = []
	stri = "Id,Email,pno,status,calls"
	fi = open("Records.csv","w")
	fi.write(stri)
	fi.close()
readcsv()