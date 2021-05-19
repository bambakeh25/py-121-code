sales = {'JAN': 150, 'FEB':200, 'MAR': 175,
        'APR': 75, 'MAY': 80, 'JUN': 300,
        'JUL': 250, 'AUG':130, 'SEP': 195,
        'OCT': 75, 'NOV': 120, 'DEC': 400}
# 1
months = [mon for mon,val in sales.items() if val >= 150]
print(months)
print('='*35)

# 2
months = [(mon,val) for mon,val in sales.items() if val >= 300]
print(months)
print('='*35)

# 3
short_month = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
months = [ f'{short_month[x]},{short_month[x+1]},{short_month[x+2]}' 
          for x in range(9) if sales[short_month[x]] + sales[short_month[x+1]] + sales[short_month[x+2]]< 500]
print(months)
print('='*35)

# 4
short_month = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
months = [ f'{short_month[x]},{short_month[x+1]},{short_month[x+2]}: {sales[short_month[x]] + sales[short_month[x+1]] + sales[short_month[x+2]]}' 
          for x in range(9) if sales[short_month[x]] + sales[short_month[x+1]] + sales[short_month[x+2]]< 500]
print(months)
print('='*35)

stock_price = [23.5, 24.1, 22.7, 24.2, 25.2, 28.4, 27.8, 26.5, 27.5, 28.2]
mean = sum(stock_price)/len(stock_price)
print(f'The mean stock price is {mean:.2f}')

print('='*35)
num_over_25 = sum([1 for price in stock_price if price > 25])
print(f'The stock price was over 25, {num_over_25} time(s)')

print('='*35)
ror = [round(((stock_price[i]-stock_price[i-1])/stock_price[i-1])*100,2) for i in range(1,len(stock_price)) ]
print(f'The daily rate of return, {ror}')

print('='*35)
ror_cnt = sum([1 for i in ror if abs(i) > 3 ])
print(f'The daily rate of return was up or down, {ror_cnt} time(s)')

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
    
grades = [68.0, 90.0, 69.0, 86.0, 78.0, 97.0, 95.0, 83.0, 84.0, 74.0, 84.0, 71.0, 79.0, 82.0, 79.0, 69.0, 99.0, 93.0, 
 77.0, 77.0, 75.0, 83.0, 86.0, 89.0, 76.0, 88.0, 65.0, 65.0, 78.0, 77.0, 82.0, 97.0, 87.0, 83.0, 67.0, 83.0, 
 67.0, 77.0, 79.0, 79.0, 68.0, 69.0, 89.0, 79.0, 66.0, 85.0, 93.0, 74.0, 70.0, 83.0, 90.0, 75.0, 94.0, 77.0, 
 92.0, 84.0, 93.0, 83.0, 79.0, 87.0, 62.0, 85.0, 99.0, 76.0, 96.0, 89.0, 66.0, 85.0, 70.0, 83.0, 77.0, 96.0, 
 92.0, 76.0, 95.0, 84.0, 74.0, 83.0, 83.0, 89.0, 81.0, 91.0, 83.0, 74.0, 93.0, 73.0, 73.0, 84.0, 84.0, 83.0, 
 91.0, 68.0, 88.0, 72.0, 84.0, 93.0, 86.0, 83.0, 83.0, 77.0]

g1 = BaseStatistics(grades)
mean = g1.calc_mean()
print(f'The mean = {mean}')
skew = g1.calc_skewness()
print(f'The skewness is {skew}')
print('='*35)
adj_skew = g1.calc_adjusted_skewness()
print(f'The adjusted skewness is {adj_skew}')
print('='*35)
kurtosis = g1.calc_adjusted_skewness()
print(f'The kurtosis is {kurtosis}')

import matplotlib.pyplot as plt

grades = [68.0, 90.0, 69.0, 86.0, 78.0, 97.0, 95.0, 83.0, 84.0, 74.0, 84.0, 71.0, 79.0, 82.0, 79.0, 69.0, 99.0, 93.0, 
 77.0, 77.0, 75.0, 83.0, 86.0, 89.0, 76.0, 88.0, 65.0, 65.0, 78.0, 77.0, 82.0, 97.0, 87.0, 83.0, 67.0, 83.0, 
 67.0, 77.0, 79.0, 79.0, 68.0, 69.0, 89.0, 79.0, 66.0, 85.0, 93.0, 74.0, 70.0, 83.0, 90.0, 75.0, 94.0, 77.0, 
 92.0, 84.0, 93.0, 83.0, 79.0, 87.0, 62.0, 85.0, 99.0, 76.0, 96.0, 89.0, 66.0, 85.0, 70.0, 83.0, 77.0, 96.0, 
 92.0, 76.0, 95.0, 84.0, 74.0, 83.0, 83.0, 89.0, 81.0, 91.0, 83.0, 74.0, 93.0, 73.0, 73.0, 84.0, 84.0, 83.0, 
 91.0, 68.0, 88.0, 72.0, 84.0, 93.0, 86.0, 83.0, 83.0, 77.0]
xAxis = range(1,len(grades)+1)
plt.bar(xAxis,grades)
plt.title('student grades')
plt.xlabel('exam')
plt.ylabel('score')
plt.show()

import math
#create quartiles
interval = math.ceil(20/4)
quartiles = {1:[],2:[],3:[],4:[]}
val = 0
for k,v in quartiles.items():
        quartiles[k] = [val+(interval*int(k-1)),val + interval*int(k)]
print(quartiles)

import math
#create quartiles
interval = math.ceil((150-100)/10)
deciles = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[]}
val = 0
for k,v in deciles.items():
        deciles[k] = [val+(interval*int(k-1)),val + interval*int(k)]
print(deciles)

import matplotlib.pyplot as plt
import math

grades = [68.0, 90.0, 69.0, 86.0, 78.0, 97.0, 95.0, 83.0, 84.0, 74.0, 84.0, 71.0, 79.0, 82.0, 79.0, 69.0, 99.0, 93.0, 
 77.0, 77.0, 75.0, 83.0, 86.0, 89.0, 76.0, 88.0, 65.0, 65.0, 78.0, 77.0, 82.0, 97.0, 87.0, 83.0, 67.0, 83.0, 
 67.0, 77.0, 79.0, 79.0, 68.0, 69.0, 89.0, 79.0, 66.0, 85.0, 93.0, 74.0, 70.0, 83.0, 90.0, 75.0, 94.0, 77.0, 
 92.0, 84.0, 93.0, 83.0, 79.0, 87.0, 62.0, 85.0, 99.0, 76.0, 96.0, 89.0, 66.0, 85.0, 70.0, 83.0, 77.0, 96.0, 
 92.0, 76.0, 95.0, 84.0, 74.0, 83.0, 83.0, 89.0, 81.0, 91.0, 83.0, 74.0, 93.0, 73.0, 73.0, 84.0, 84.0, 83.0, 
 91.0, 68.0, 88.0, 72.0, 84.0, 93.0, 86.0, 83.0, 83.0, 77.0]

#create boundaries
interval = math.ceil((max(grades)-min(grades))/10)
deciles = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[]}
val = 0
min_grade = min(grades)
grade_dist = []
for k,v in deciles.items():
        beg = min_grade+(interval*int(k-1))
        end = min_grade + interval*int(k)
        deciles[k] = [beg,end]
        sum_int = sum([1 for x in grades if x>= beg and x< end])
        grade_dist.append(sum_int)
print(deciles)
print(grade_dist)
xAxis = range(1,11)
plt.bar(xAxis,grade_dist)
plt.title('Frequency distribution')
plt.xlabel('exam')
plt.ylabel('score')
plt.show()

import matplotlib.pyplot as plt
import math

grades = [68.0, 90.0, 69.0, 86.0, 78.0, 97.0, 95.0, 83.0, 84.0, 74.0, 84.0, 71.0, 79.0, 82.0, 79.0, 69.0, 99.0, 93.0, 
 77.0, 77.0, 75.0, 83.0, 86.0, 89.0, 76.0, 88.0, 65.0, 65.0, 78.0, 77.0, 82.0, 97.0, 87.0, 83.0, 67.0, 83.0, 
 67.0, 77.0, 79.0, 79.0, 68.0, 69.0, 89.0, 79.0, 66.0, 85.0, 93.0, 74.0, 70.0, 83.0, 90.0, 75.0, 94.0, 77.0, 
 92.0, 84.0, 93.0, 83.0, 79.0, 87.0, 62.0, 85.0, 99.0, 76.0, 96.0, 89.0, 66.0, 85.0, 70.0, 83.0, 77.0, 96.0, 
 92.0, 76.0, 95.0, 84.0, 74.0, 83.0, 83.0, 89.0, 81.0, 91.0, 83.0, 74.0, 93.0, 73.0, 73.0, 84.0, 84.0, 83.0, 
 91.0, 68.0, 88.0, 72.0, 84.0, 93.0, 86.0, 83.0, 83.0, 77.0]

#create boundaries
interval = math.ceil((max(grades)-min(grades))/10)
deciles = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[]}
val = 0
min_grade = min(grades)
grade_dist = []
for k,v in deciles.items():
        beg = min_grade+(interval*int(k-1))
        end = min_grade + interval*int(k)
        deciles[k] = [beg,end]
        sum_int = sum([1 for x in grades if x< end])
        grade_dist.append(sum_int)
print(deciles)
print(grade_dist)
xAxis = range(1,11)
plt.bar(xAxis,grade_dist)
plt.title('Frequency distribution')
plt.xlabel('exam')
plt.ylabel('score')
plt.show()

sat_scores = [540, 590, 560, 720, 680, 570, 590, 600, 580, 610]
sat_scores.sort()
print(sat_scores)
score_len = len(sat_scores)
if score_len % 2 == 0:
    # Even
    pos = int(score_len/2)
    median = (sat_scores[pos-1]+sat_scores[pos])/2
else:
    # odd - middle
    pos = int((score_len-1)/2)
    median = sat_scores[pos]
print(f'Median = {median}')
# Calculate how many student are below the median
pct_below_median = (sum([1 for x in sat_scores if x < median])/score_len) * 100
print(f'{pct_below_median}% Below the median')
# Calculate how many student are above the median
pct_above_median = (sum([1 for x in sat_scores if x >= median])/score_len) * 100
print(f'{pct_above_median}% Above the median')



