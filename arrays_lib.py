import array as ar
#creating homogeneous integer array
int_array = ar.array('i',[4,6,9])
print(int_array[1])

#converting a list into arrays
l = [5,2,3,8,23,45,76,98,21]
l_array = ar.array('i', l)
print(l_array[4])