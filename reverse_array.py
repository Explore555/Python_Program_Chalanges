                            #Reverse an Array

# a=[1,2,3,4,5,6,7,8,9,10,11,13]

#>>>>>>>>>>>>>>>>>>>> using reverse() function <<<<<<<<<<<<<<<

# a.reverse()
# print(a)

#>>>>>>>>>>>>>>>>>>>>> using reversed() function <<<<<<<<<<<<<

# print(list(reversed(a)))


#>>>>>>>>>>>>>>>>>>>> my Won reverse algorithm <<<<<<<<<<<<<<<<<<<<

# l=len(a)//2
# r=-1
# for i in range(l):
#             # Swaping is used 
#     a[i],a[r]=a[r],a[i]
#     # a[i]=a[i]+a[r]                       
#     # a[r]=a[i]-a[r]
#     # a[i]=a[i]-a[r]
#     r=r-1
# print(a)


