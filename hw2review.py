chemistry_grades = {'Hester': ['88','99','89','90','80','88','93','94','91','80'] , 'Walter': ['83','92','83','76','75','85','93','92','90','91'] , 'George': ['86','90','86','84','78','84','93','94','81','90'] , 'Susan': ['81','94','80','79','74','94','93','92','94','98'] , 'Kathy': ['78','89','70','99','81','85','93','97','96','92'] }
"""
1 - Calculate the mean and standard deviation of each exam?
2 - Calculate each students gpa?
3 - Which exam had the biggest range?
4 - Which exam had the lowest mean? Add 10 points to the test score of each student
on that exam and recalulate the mean and standard deviation
"""
import math
class BaseStatistics:
    def __init__(self,base_list, factor = 1):   # Change made on constructor ******
        base_list.sort()
        self.ordered = [x*factor for x in base_list]
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
        mean = sum(self.ordered)/len(self.ordered)
        variance = sum([(x-mean)**2 for x in self.ordered])/len(self.ordered)
        return math.sqrt(variance)
#===========================================================================
chemistry_grades = {'Hester': ['88','99','89','90','80','88','93','94','91','80'] ,
                    'Walter': ['83','92','83','76','75','85','93','92','90','91'] ,
                    'George': ['86','90','86','84','78','84','93','94','81','90'] ,
                    'Susan':  ['81','94','80','79','74','94','93','92','94','98'] ,
                    'Kathy':  ['78','89','70','99','81','85','93','97','96','92'] }

# question 1 - reorder the data structure into exams
# There are 10 exams
max_range = 0
max_exam = 0
lowest_mean = 1000
lowest_mean_exam = 0
recalc_grades = []
for i in range(10):
    grades = []
    for k,v in chemistry_grades.items():
        print(f'Exam {i+1} grades {v[i]}')
        grades.append(int(v[i]))
    # calcuate the mean
    g1 = BaseStatistics(grades)
    mean = g1.calc_mean()
    print(f'The mean of exam {i+1} = {mean}')
    stdev = g1.calc_stdev()
    print(f'The standard deviation of exam {i+1} is {stdev:.2f}') 
    g_range = g1.calc_range()
    print(f'The range of exam {i+1} is {g_range:.2f}') 
    print('='*35)
    if g_range > max_range:
        max_range = g_range
        max_exam = i+1
        
    if mean < lowest_mean:
        lowest_mean = mean
        lowest_mean_exam = i+1
        recalc_grades = grades

print(f'The largest range was {max_range} for exam {max_exam}')
# recalc for the lowest mean with a 10 point boost
print(f'The lowest mean was {lowest_mean} for exam {lowest_mean_exam}')
boost_grades = [x+10 for x in recalc_grades]
g1 = BaseStatistics(boost_grades)
mean = g1.calc_mean()
print(f'The RECALCULATED mean of exam {lowest_mean_exam} = {mean}')
stdev = g1.calc_stdev()
print(f'The RECALCULATED standard deviation of exam {lowest_mean_exam} is {stdev:.2f}') 
print('='*35)
# Calculate each students gpa
for k,v in chemistry_grades.items():
    grades = [int(x) for x in v]
    # calcuate the mean
    g1 = BaseStatistics(grades)
    mean = g1.calc_mean()
    print(f'The mean for {k} = {mean}')



"""
Calculate the mean, median, mode and standard deviation of the following data set:
"""
summer_temps = {'2020-04-01': 72,83, '2020-04-02': 64,72, '2020-04-03': 66,69, '2020-04-04': 70,88, '2020-04-05': 75,79, '2020-04-06': 71,80, '2020-04-07': 68,74, '2020-04-08': 69,76, '2020-04-09': 62,80, '2020-04-10': 71,84, '2020-04-11': 70,88, '2020-04-12': 65,73, '2020-04-13': 67,85, '2020-04-14': 76,89, '2020-04-15': 74,88, }
"""
The first temperature represents the daily low and the 2nd represents
the daily high.
Calculate the following statistics:
1 - The mean, mode, median daily low
2 - The mean, mode, median daily high
3 - What is the daily temperature difference every day?
4 - What is the mean daily temperate difference every day?
implement using OOP (classes, objects)
"""

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
    
summer_temps = {'2020-04-01': [72,83],
                '2020-04-02': [64,72],
                '2020-04-03': [66,69],
                '2020-04-04': [70,88],
                '2020-04-05': [75,79],
                '2020-04-06': [71,80],
                '2020-04-07': [68,74],
                '2020-04-08': [69,76],
                '2020-04-09': [62,80],
                '2020-04-10': [71,84],
                '2020-04-11': [70,88],
                '2020-04-12': [65,73],
                '2020-04-13': [67,85],
                '2020-04-14': [76,89],
                '2020-04-15': [74,88],
               }
# 1 - The mean, mode, median daily low
temps = []
for key,temp in summer_temps.items():
    temps.append(temp[0])
t_low = BaseStatistics(temps)
mean = t_low.calc_mean()
print(f'The mean = {mean}')
median = t_low.calc_median()
print(f'The median = {median}')
mode = t_low.calc_mode()
print(f'The mode = {mode}')
print('='*35)
# *********** List comprehension
temps = [values[0] for key,values in summer_temps.items()]
t_low = BaseStatistics(temps)
mean = t_low.calc_mean()
print(f'The mean = {mean}')

# 2 - The mean, mode, median daily high
print('='*35)
# *********** List comprehension
high_temps = [values[1] for key,values in summer_temps.items()]
t_high= BaseStatistics(high_temps)
mean = t_high.calc_mean()
print(f'The mean = {mean}')
median = t_high.calc_median()
print(f'The median = {median}')
mode = t_high.calc_mode()
print(f'The mode = {mode}')
print('='*35)

# 3 - What is the daily temperature difference every day?
temp_diff = [values[1]-values[0] for key,values in summer_temps.items()]
print(temp_diff)
# 4 - What is the mean daily temperate difference every day?
t_diff = BaseStatistics(temp_diff)
mean = t_diff.calc_mean()
print(f'The mean = {mean}')







