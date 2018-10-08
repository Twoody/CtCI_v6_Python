'''
	Tanner 20180919

	Write a function to add two simple mathematical expressions
	which are of the form:
		Ax^a + Bx^b + ...
	That is, the expression is a sequence of terms, where each
	term is simply a contant times an exponent.
	Do not do string parsing, and use w/e data structure desired.


	Thoughts:
		I am unsure of what a mathematical expression is, and
		what we are suppose to be passing as variables and adding...

		What is being asked here???

'''

global x
x = 10

class Expression:
	def __init__(self, const, exp): #constant, expression
		self.const = const
		self.exp	  = exp
	def getsum(self):
		return self.const * x**self.exp
	def printExpr(self):
		s = "\t(" + str(self.const) + ')'
		s += "(" + str(x) + "^" + str(self.exp) + ')'
		print(s)

def addExpressions(exprArray):
	ret = 0
	for expr in exprArray:
		ret += expr.getsum()
	return ret

def printExpressions(exprArray):
	for expr in exprArray:
		expr.printExpr()

def main():
	#Book says to answer this with classes...
	expr1 = Expression(1,1)
	expr2 = Expression(2,2)
	expr3 = Expression(3,3)
	exprArray = [expr1, expr2, expr3]
	total = addExpressions(exprArray)

	printExpressions(exprArray)
	print( '\t' + str(total))


if __name__ == "__main__":
	main()
