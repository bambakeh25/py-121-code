"""
Write a function that computes the compound interest of an intial investment, using principle rate and time
Formula for compound interest: A = P(1 + R/100) t
Where, A is amount P is principle amount R is the rate and T is the time span.
Part 2: Convert function to a method of a class i.e. (class Finances, calc_compound_interest)
""" 

def compound_interest(P,R,t):
	return P * (1 + R/100) * t	

class Finances2:
	def __init__(self,assets):
		self.assets = assets 

	@staticmethod
	def calc_compound_interest(P, R, t):
		return P * (1 + R/100) * t 

class Finances:
    def __init__( self, prin, rate, time ):
        self.principle = prin
        self.rate = rate
        self.time = time
        
    def calc_compound_interest(self):
        amount = self.principle*(1 + (self.rate/100)) * self.time
        return amount
a1 = Finances2(100, .10, 50)
a1.calc_compound_interest()
                       
	
if __name__ == '__main__':
	finances = Finances([1,12,4,25,21])
	print(finances.calc_compound_interest(1000, 20, 5))
