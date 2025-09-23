def show(n):
    if(n==0):
        
        return
    print(n)
    show(n-1)
    print("end",n)
    

show(5)

# show(5): print(5)
#     show(4): print(4)
#         show(3): print(3)
#             show(2): print(2)
#                 show(1): print(1)
#                     show(0): return   ← base case hit
#                 print("end")
#             print("end")
#         print("end")
#     print("end")
# print("end")
