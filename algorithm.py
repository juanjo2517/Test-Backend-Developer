

# def can_be_splitted(array):
#     if len(array) == 0:
#         return 0

def find_position_point(array):
    
    len_array = len(array)

    # Variable para calcular la suma de toda la matriz - Suma de la izquierda
    left_sum = 0
   
    # Ciclo para sumar matriz
    for i in range(0, len_array):
        
        # Agregar iterador actual a la suma
        left_sum += array[i]
   
        # Calcular la suma de la derecha
        right_sum = 0

        for a in range(i+1, len_array):
            right_sum += array[a]
   
        # split poindex
        if left_sum == right_sum:
            return i+1
      
   
    # Si no es posible dividir las partes
    return -1
  
# Prints two parts after finding split pousing
# findSplitPoint()
def can_be_spliited(array) :
    
    len_array = len(array)

    if len_array == 0:
        return 0

    postion = find_position_point(array)
   
    if postion == -1 or postion == len_array:
        return postion
    
    for i in range(0, len_array) :
        if(postion == i) :
            return 1


array = [1 , 3 , 3 , 3 , 10]

print(can_be_spliited(array))
