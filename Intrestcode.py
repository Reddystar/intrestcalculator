print("Welcome TO Python")
""" This is Program for Simple Interest Calculator """
p = float(input("Enter Prime :"))
r = float(input("Enter IR :"))
t1 = float(input("Enter years   :"))
t2 = float(input("Enter months   :"))
t3 = float(input("Enter days   :"))
i = float((p*r*t1)/100) + float((p*r*(t2)/12)/100) + float((p*r*(t3)/300)/100)
print(" Simple intrest is" ,round(float(i) ,2))
print("Thank You for Using Our Services")
#THIS IS CODE FOR COMPOUND INTREST
c =p*pow(1+r/100, t1)-p + p*pow(1+r/1200, t2)-p + p*pow(1+r/3000, t3)-p

print("compound intrest " , round(c, 2))
print("Total Amount Payable:" ,round(p+c, 2 ))
