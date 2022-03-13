import matplotlib.pyplot as plt

mes = [1,2,3,4,5,6]
Marcus  = [600,380,400,600,900,1000]
Vinicius = [600,450,600,900,500,600]
Bernardo = [500,500,600,500,700,1000]

plt.plot(mes,Marcus,label='Vendedor Marcus');
plt.plot(mes,Vinicius,label='Vendedor Vinicius');
plt.plot(mes,Bernardo,label='Vendedor Bernardo');
plt.legend();
plt.xlabel('Meses Vendas 2022');
plt.ylabel ('Vendedores');
plt.savefig('Gráfico_1')
plt.show ()