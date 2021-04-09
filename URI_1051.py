# a=float(input())
# if(0<a<=2000):
#     print("Isento")
# elif(2000<a<=3000):
#     t= (a-2000)
#     tx= (t*8)/100
#     print("R$ %.2f"%tx)
# elif(3000<a<=4500):
#     t= (a-2000)
#     t1=t-1000
#     tx1=(1000*8)/100
#     tx2= (t1*18)/100
#     print("R$ %.2f"%(tx1+tx2))
# else:
#     t= (a-2000)
#     t1= t-1000
#     tx1= (1000*8)/100
#     t2=t1-1500
#     tx2=(1500*18)/100
#     tx= (t2*28)/100
#     print("R$ %.2f" %(tx+tx1+tx2))
#




s = float(input())
if s <= 2000.00:
    print("Isento")
elif s >= 2000.01 and s <= 3000.00:
    a = s - 2000
    print("R$ %.2f" % ((a * 8)/100))
elif s >= 3000.01 and s <= 4500.00:
    a = (s - 2000)
    a1 = a - 1000
    ax1 = (1000 * 8)/100
    ax2 = (a1 * 18)/100
    print("R$ %.2f" % (ax1 + ax2))
elif s >= 4500.00:
    a = (s - 2000)
    a1 = a - 1000
    ax1 = (1000 * 8)/100
    a2 = a1 - 1500
    ax2 = (1500 * 18)/100
    ax = (a2 * 28)/100
    print("R$ %.2f" % (ax1 + ax2 + ax))
