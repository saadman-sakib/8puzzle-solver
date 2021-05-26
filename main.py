from solver import Solver

a = [[3,None,2],
	 [4,1,8],
	 [6,5,7]]


gem = Solver(a)
gem.pretty_print(a)
gem.solve()