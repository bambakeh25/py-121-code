product_numbers = ['AS-500','TR-700','TR-800','TR-100','AX-131','AX-232','AL-3400','TR-300']
product_order = [pn for pn in product_numbers if pn.startswith('TR')] + \
[pn for pn in product_numbers if not pn.startswith('TR')]
print(product_order)

processes = [{'command':'docker build -t python101:1.0'},
             'Reboot server',
             'Data cleaning',
             {'command': 'git stash','server':'mid west'}]
process = [p for p in processes if isinstance(p,dict) and p.get('command') == 'git stash'] + \
[p for p in processes if not (isinstance(p,dict) and p.get('command') == 'git stash') ] 
print(process)

import math
class BaseStatistics:
    def __init__(self,base_list):
        base_list.sort()
        self.ordered = base_list
        self.list_len = len(self.ordered)
        
    def calc_mean(self):
        if len(self.ordered) > 0:
            return round(sum(self.ordered)/self.list_len,2)

    def calc_median(self):
        if self.list_len % 2 == 0:
            pos = (self.list_len/2) - 1
            median = (self.ordered[int(pos+1)] + self.ordered[int(pos)])/2
        else:
            median = self.ordered[int(((self.list_len + 1)/2) - 1)] 
        return median
    
    def calc_mode(self):
        mode = None
        temp_mode = {}
        for num in self.ordered:
            if num not in temp_mode:
                temp_mode[num] = 0
            temp_mode[num] += 1
        # print(temp_mode)
        ans_sort = sorted(temp_mode.items(),key = lambda kv: kv[1] , reverse = True)
        # print(ans_sort)

        # Step 1 - Get the max number
        max_num = ans_sort[0][1]

        # Use the value to get all of the keys with that value using list comprehension
        if max_num > 1:
            mode = [num[0] for num in ans_sort if num[1] == max_num]
        return mode
        
    def calc_max(self):
        return max(self.ordered)
    
    def calc_min(self):
        return min(self.ordered)
    
    def calc_range(self):
        return self.calc_max() - self.calc_min()
    
    def calc_stdev(self):
        mean = self.calc_mean()
        variance = sum([(x-mean)**2 for x in self.ordered])/len(self.ordered)
        return math.sqrt(variance)
    
    def calc_skewness(self):
        mean = self.calc_mean()
        skew_part1 = sum([(x-mean)**3 for x in self.ordered])/len(self.ordered)
        return round(skew_part1/(self.calc_stdev()**3),3)

    def calc_adjusted_skewness(self):
        mean = self.calc_mean()
        skew_part1 = sum([(x-mean)**3 for x in self.ordered])/len(self.ordered)
        return round(math.sqrt((self.list_len*(self.list_len-1)))/(self.list_len-2),2) * (skew_part1/(self.calc_stdev()**3))
    
    def calc_excess_kurtosis(self):
        mean = self.calc_mean()
        kurt_part1 = sum([(x-mean)**4 for x in self.ordered])/len(self.ordered)
        return (round(kurt_part1/(self.calc_stdev()**4),3)) - 3

    @staticmethod
    def calc_covariance(list_x,list_y):
        mean_x = sum(list_x)/len(list_x)
        mean_y = sum(list_y)/len(list_y)
        x_1 = [(x-mean_x) for x in list_x]
        y_1 = [(y-mean_y) for y in list_y]
        return sum([x_1[i]*y_1[i] for i in range(len(x_1))])/(len(x_1)-1)

temperatures = [89, 93, 77, 79, 93, 95, 94]
icecream_sales = [20000, 25000, 16000, 18000, 21000, 24000, 23000]

covar = BaseStatistics.calc_covariance(temperatures,icecream_sales)
print(f'The covariance = {covar}')

direction = 'positive' if covar > 0 else 'negative'
print(f'The covariance of temperatures and icecream sales is directionaly {direction}')

from datetime import date as dt
class Employee:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        
    @staticmethod
    def isAdult(age):
        return True if age > 18 else False
        
    @classmethod
    def get_age(cls, name, gender, year):
        '''
        the cls argument (which can be named anything) gives us access to the
        methods to an instance of the class
        '''
        return cls(name, gender, dt.today().year - year)  # This instatiates the class instance
    
    def __str__(self):
        return f'\nEmployee\n Name: {self.name}\n Gender: {self.gender}\n Age: {self.age}'
    
emp1 = Employee('Stephen', 'M', 30)
print(emp1)

emp2 = Employee.get_age('Gloria', 'F', 1995)
print(emp2)
print(Employee.isAdult(25))  # Call the static method
print(Employee.isAdult(16))  # Call the static method

import math
from functools import reduce

class Geometry:
    def __init__(self,shape_type,*sides):
        self.shape_type = shape_type
        self.get_shape_name()
        self.sides = [x for x in sides]
        print(self.sides)
        
    def get_shape_name(self):
        if self.shape_type == 'C':
            res = 'Circle'
        elif self.shape_type == 'T':
            res = 'Triangle'
        elif self.shape_type == 'R':
            res = 'Rectangle'            
        else:
            res = 'NOT DEFINED'
        return res
    
    @staticmethod
    def calc_area(shape_type,*sides):
        if shape_type == 'R':
            res = reduce(lambda x,y: x*y,sides)
        elif shape_type == 'T':
            print(len(sides))
            res = reduce(lambda x,y: x*y,sides)
        return res
    
r1 = Geometry('R',10,12)            
print(r1.get_shape_name())

print('='*35)
r1 = Geometry('X',10)            
print(r1.get_shape_name())

print('='*35)
r1 = Geometry('T',10,2,3)            
print(r1.get_shape_name())

res = Geometry.calc_area('R',10,4)
print(res)

print('='*35)
r1 = Geometry('T',10,2,3)            
print(r1.get_shape_name())
res = Geometry.calc_area('R',10,4)
print(res)

import math
class BaseStatistics:
    def __init__(self,base_list=[]):
        base_list.sort()
        self.ordered = base_list
        self.list_len = len(self.ordered)
        
    def calc_mean(self):
        if len(self.ordered) > 0:
            return round(sum(self.ordered)/self.list_len,2)

    def calc_median(self):
        if self.list_len % 2 == 0:
            pos = (self.list_len/2) - 1
            median = (self.ordered[int(pos+1)] + self.ordered[int(pos)])/2
        else:
            median = self.ordered[int(((self.list_len + 1)/2) - 1)] 
        return median
    
    def calc_mode(self):
        mode = None
        temp_mode = {}
        for num in self.ordered:
            if num not in temp_mode:
                temp_mode[num] = 0
            temp_mode[num] += 1
        # print(temp_mode)
        ans_sort = sorted(temp_mode.items(),key = lambda kv: kv[1] , reverse = True)
        # print(ans_sort)

        # Step 1 - Get the max number
        max_num = ans_sort[0][1]

        # Use the value to get all of the keys with that value using list comprehension
        if max_num > 1:
            mode = [num[0] for num in ans_sort if num[1] == max_num]
        return mode
        
    def calc_max(self):
        return max(self.ordered)
    
    def calc_min(self):
        return min(self.ordered)
    
    def calc_range(self):
        return self.calc_max() - self.calc_min()
    
    def calc_stdev(self):
        mean = self.calc_mean()
        variance = sum([(x-mean)**2 for x in self.ordered])/(len(self.ordered)-1)
        return math.sqrt(variance)
    
    def calc_skewness(self):
        mean = self.calc_mean()
        skew_part1 = sum([(x-mean)**3 for x in self.ordered])/(len(self.ordered)-1)
        return round(skew_part1/(self.calc_stdev()**3),3)

    def calc_adjusted_skewness(self):
        mean = self.calc_mean()
        skew_part1 = sum([(x-mean)**3 for x in self.ordered])/len(self.ordered)
        return round(math.sqrt((self.list_len*(self.list_len-1)))/(self.list_len-2),2) * (skew_part1/(self.calc_stdev()**3))
    
    def calc_excess_kurtosis(self):
        mean = self.calc_mean()
        kurt_part1 = sum([(x-mean)**4 for x in self.ordered])/len(self.ordered)
        return (round(kurt_part1/(self.calc_stdev()**4),3)) - 3

    @staticmethod
    def calc_covariance(list_x,list_y):
        mean_x = sum(list_x)/len(list_x)
        mean_y = sum(list_y)/len(list_y)
        x_1 = [(x-mean_x) for x in list_x]
        y_1 = [(y-mean_y) for y in list_y]
        return sum([x_1[i]*y_1[i] for i in range(len(x_1))])/(len(x_1)-1)

    @classmethod
    def calc_correlation(cls,list_x,list_y):
        '''
        We need to declare this as a class method to have access to the calc_stdev
        methods.  We have access using the cls argument.
        '''
        x = cls(list_x)
        stdev_x = x.calc_stdev()
        # print(f'st dev x = {stdev_x}')
        y = cls(list_y)
        stdev_y = y.calc_stdev()
        # print(f'st dev y = {stdev_y}')
        covar = cls.calc_covariance(list_x,list_y)
        # print(f'*** {covar}')
        return covar/(stdev_x*stdev_y)
        
temperatures = [89, 93, 77, 79, 93, 95, 94]
icecream_sales = [20000, 25000, 16000, 18000, 21000, 24000, 23000]

print('='*35)
t1 = BaseStatistics(temperatures)
stdev = t1.calc_stdev()
print(f'The standard deviation of temperatures = {stdev}')

print('='*35)
c1 = BaseStatistics(icecream_sales)
stdev = c1.calc_stdev()
print(f'The standard deviation of icecream sales = {stdev}')


covar = BaseStatistics.calc_covariance(temperatures,icecream_sales)
print(f'The covariance = {covar}')

direction = 'positive' if covar > 0 else 'negative'
print(f'The covariance of temperatures and icecream sales is directionaly {direction}')

print('='*35)
correl = BaseStatistics.calc_correlation(temperatures,icecream_sales)
print(f'The correlation = {correl}')

signif = 'strong' if correl and abs(correl) >= .7 else 'weak'
print(f'The correlation of temperatures and icecream sales is {signif}')

import random

class Deck_of_Cards:
    def __init__(self):
        self.cards = self.create_deck()
        self.number_of_cards = len(self.cards)
        
    def create_deck(self):
        face_cards = ['Jack','Queen','King','Ace']
        non_face_cards = list(range(2,11))
        suit = ['Spades','Clubs','Hearts','Diamonds']
        cards = [f'{card} of {s}' for card in non_face_cards + face_cards for s in suit]
        return cards
    
    def __str__(self):
        return f'There are {self.number_of_cards} cards in the deck'
            
    def shuffle(self):
        random.shuffle(self.cards)
        
    def cut(self,num_of_cards_to_cut = 0):
        if num_of_cards_to_cut == 0:
            print('You tapped the cards')
        if num_of_cards_to_cut > 0 and num_of_cards_to_cut < self.number_of_cards:
            self.cards = self.cards[num_of_cards_to_cut:] + self.cards[:num_of_cards_to_cut]
    
    def deal(self,cards_to_deal=1):
        if cards_to_deal > self.number_of_cards:
            print('You cannot deal more cards than are in the deck')
        else:
            for i in range(cards_to_deal):
                if self.number_of_cards > 0:
                    card = self.cards[0]
                    print(f'Dealt {card}')
                    # remove the card
                    self.cards.remove(card)
                    self.number_of_cards -= 1
        
new_deal = Deck_of_Cards()
print(new_deal.cards)
new_deal.shuffle()
print(new_deal)
print(new_deal.cards)
new_deal.cut(20)
print(new_deal.cards)
new_deal.deal(10)
print(new_deal.cards)
new_deal.deal(10)
print(new_deal.cards)
new_deal.deal(10)
print(new_deal.cards)
new_deal.deal(10)
print(new_deal.cards)
new_deal.deal(10)
print(new_deal.cards)
new_deal.deal(3)
print(new_deal.cards)

import math
import matplotlib.pyplot as plt



def exercise_1():
    pass


"""
Take the numbers from  100 to 1000
break the categories into groups of 100
In each group place the number of prime numbers
chart as a bar chart
 
        
def isPrime(num):
    prime = False
    if num > 1:
        prime = True
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                prime = False
                break
    return prime

xAxis = range(1,11)
plt.bar(xAxis,primes)
plt.title('Frequency distribution')
plt.xlabel('cluster')
plt.ylabel('primes found')
plt.show()    

import math

x = [1,2,0,5,1,4,-1,2]
maxNumber = -math.inf
for i in x:
    maxNumber = i if i > maxNumber else maxNumber
print('New max number {0}'.format(maxNumber))

