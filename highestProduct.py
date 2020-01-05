import numpy as np



def highestProduct(list):

    product = 0
    productList = []
    list.sort()

    if(len(list) <= 3 and len(list) > 0):
        product = np.prod(list) #use numpy.prod() to multiply all the remaining integers in the list

    elif(len(list) <= 0):
        print("Emtpy list. Please provide a list with integers")

    elif(len(list) > 3):

        #the sorted list will have the highest numbers at the end, so here we put the last three in a new list and use prod()
        productList.append(list[-1])
        productList.append(list[-2])
        productList.append(list[-3])
        product = np.prod(productList)


    return product




#-------------------------------------------
def main():


    #Here are four different cases and lists, to try out and validate the function.
    liste1 = [1, 10, 2, 6, 5, 3]
    liste2 = [1]
    liste3 = []
    liste4 = [5,67,2,5,3,8,1,0,-64,50,15]

    prod = highestProduct(liste1)

    print("Highest Product: " + str(prod))



main()