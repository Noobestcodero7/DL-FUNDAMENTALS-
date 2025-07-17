# Define AND gate function
def and_gate(x1,x2):
    w1,w2,b,theta=0.3,0.3,0.1,0.5 #give the values for w1,w2,b and theta
    a=x1*w1+x2*w2+b #define a
    if a<=theta :
        return 0
    else:
       return 1
   
print("AND gate output")
print(and_gate(0,0))
print(and_gate(1,0))
print(and_gate(0,1))
print(and_gate(1,1))
 
#Define OR gate function
def or_gate(x1,x2):
    w1,w2,b,theta=0.5,0.5,0.1,0.5
    a=x1*w1+x2*w2+b
    if a <= theta:
        return 0
    else:
        return 1
print("OR gate output")    
print(or_gate(0,0))
print(or_gate(1,0))
print(or_gate(0,1))
print(or_gate(1,1))

#Define NAND gate function
def nand_gate(x1,x2):
    w1,w2,b,theta=-0.2,-0.2,-0.2,-0.5
    a=x1*w1+x2*w2+b
    if a <= theta:
        return 0
    else:
        return 1
    
print("NAND gate output")
print(nand_gate(0,0))
print(nand_gate(1,0))
print(nand_gate(0,1))
print(nand_gate(1,1))