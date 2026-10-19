class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        pila=[]
        for i in range(len(tokens)):
            if tokens[i] not in ("+", "-", "/", "*"):
                
                pila.append(int(tokens[i]))
            else:
                op2 = int(pila.pop())
                op1 = int(pila.pop())
                if tokens[i] == "+":
                    pila.append(op1+op2)
                elif tokens[i] == "-":
                    pila.append(op1-op2)
                elif tokens[i] == "*":
                    pila.append(op1*op2)
                elif tokens[i] == "/":
                    pila.append(int(op1/op2))
        return pila[0]