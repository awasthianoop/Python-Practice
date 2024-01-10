from matplotlib import pyplot as plt
x=[1,2,3]
y=[7,4,1]
x1=[4,5,6]
y2=[4,6,9]
#plt.plot(x,y,"c",label="2019")
#plt.plot(x1,y2,"g",label="2023")
#plt.title("testing graph")
#plt.ylabel("no of companies")
#plt.xlabel("vacancies")
#plt.legend()


#players=["messi","ronaldo","suarez","falcao"]
#goals=[702,648,536,368]
#plt.barh(players,goals,color ="red")

contribution=[52,20,12,2,12]
players1=["messi","ronaldo","maradona","stvechenko","pele"]
plt.pie(contribution,labels=players1,startangle=90)
plt.show()

