#This function is only for the exact recurring once's
def maxRepeating(str,num):
    temp = str
    n = len( str )
    #a = []
    cur_count = 1
    for i in range( n ):
        if (i < n - 1 and str[i] == str[i + 1]):
            cur_count += 1
        else:
            if num == cur_count:
                res = str[i]
                #a.append(res) #to get striped once
                maxima = cur_count
                res = res*maxima
            cur_count = 1
            temp = temp.strip( res )

    return temp

ent = input('Enter the String:')
number = int(input('Enter Number:'))
print(maxRepeating(ent,number))