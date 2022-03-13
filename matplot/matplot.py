import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [350,400,600,500,350]
plt.scatter(x=x, y=y, color='blue');
plt.plot(x,y, color ="green");
plt.title('Vendas 2021');
plt.xlabel('Mês');
plt.ylabel('Receita R$');
plt.savefig('Fig_1');
plt.show()