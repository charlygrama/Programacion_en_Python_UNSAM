# def a_func():
#     if 'a' or 'e' in 'casa':
#         return True
#     else:
#         return False
# a = a_func()
# print(a)
#%%    

# # cadena ='casa'
# # a = a_func(cadena)
# # print(a)
        
# #%%
# for i in range(9):
#     print(i)    
# #%%
# for i,c in enumerate('pavada'):
#     if i != (i//2)*2:
#         print(c, end='')


#%%
# def a_func(a,b):
#     c = a+b
# c = 3
# c=a_func(2,3)
# print(c)
#%%
# def func():
#     a+=1
# a=1
# a=func(a)
# a=a+1
# print(a)

#%%
# n=5
# lista = [1] * n
# for i in range (n):
#     if i +1 < n and lista[i+1]==1:
#         lista[i]+=lista[i+1]
# lista[4]=2

#%%
# r= [x* y for x in range(-10,10)if x>0 and x%2==1 for y in [1,0,-1] if y!=0]
#%%
# suma =0
# for i in range(n):
#     for j in range (n):
#         suma+=mat[i][j]
#%%
# i=0
# suma=0
# while i<=10:
#     suma+=i
# print(suma)
#%%
n=5
lista = [1] * n
for i in range (1,n):
    lista[i] = lista[i-1] +lista[i] +lista[i+1]         

#%%