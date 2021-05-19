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


grades = [84, 86, 80, 78, 90, 92, 94, 91, 89, 90]

# step 1
mean_grades = sum(grades)/len(grades)

# step 2
# a - long way
# x - xbar
step_2 = []
for grade in grades:
    step_2.append(grade - mean_grades)
print('='*40)
print(step_2)

# step 3
print('='*40)
step_3 = [x**2 for x in step_2]    
print(step_3)

print('='*40)
# step 4
step_4 = sum(step_3)

# step 5
step_5 = step_4/len(step_3)
print(f'The variance is {step_5}')

grades = [84, 86, 80, 78, 90, 92, 94, 91, 89, 90]
mean = sum(grades)/len(grades)
variance = sum([(x-mean)**2 for x in grades])/len(grades)
print(f'The variance is {variance}')

# The standard deviation is the square root of the variance.
import math
grades = [84, 86, 80, 78, 90, 92, 94, 91, 89, 90]
mean = sum(grades)/len(grades)
variance = sum([(x-mean)**2 for x in grades])/len(grades)
stdev = math.sqrt(variance)
print(f'The standard deviation is {stdev}')

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
        mean = sum(self.ordered)/len(self.ordered)
        variance = sum([(x-mean)**2 for x in self.ordered])/len(self.ordered)
        return math.sqrt(variance)
        
        
with open('c:\\projects\\code immersives\\pandas\\grades.txt','r') as fh:
    line = fh.readline()
    print(line)
    cntr = 0
    grades = []
    while line:
        # print(line)
        if cntr > 0:
            # skipped the header
            grade = line.strip('\n')
            grades.append(float(grade))
        line = fh.readline()
        cntr += 1
    print(grades)
    
g1 = BaseStatistics(grades)
mean = g1.calc_mean()
print(f'The mean = {mean}')
stdev = g1.calc_stdev()
print(f'The standard deviation is {stdev}')

lb_1 = mean-stdev 
up_1 = mean+stdev 
lb_2 = mean-(2*stdev)
up_2 = mean+(2*stdev)
lb_3 = mean-(3*stdev)
up_3 = mean+(3*stdev)
print(f'68% of the values lie within 1 SD of the mean {lb_1} and {up_1}')
print(f'95% of the values lie within 2 SDs of the mean {lb_2} and {up_2}')
print(f'99% of the values lie within 3 SDs of the mean {lb_3} and {up_3}')
#
# How many value lie between the value
std_1 = (sum([1 for x in grades if x > lb_1 and x < up_1])/len(grades))*100
std_2 = (sum([1 for x in grades if x > lb_2 and x < up_2])/len(grades))*100
std_3 = (sum([1 for x in grades if x > lb_3 and x < up_3])/len(grades))*100
print(f'{std_1}% lie within 1 standard deviation')
print(f'{std_2}% lie within 2 standard deviations')
print(f'{std_3}% lie within 3 standard deviations')



import math
class BaseStatistics:
    def __init__(self,base_list, fixed_amt = 0):   # Change made on constructor
        base_list.sort()
        self.ordered = [x+fixed_amt for x in base_list]
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
    
grades = [78, 80, 67, 77, 76, 78, 82, 74, 77, 70]
g1 = BaseStatistics(grades)
mean = g1.calc_mean()
print(f'The mean = {mean}')
stdev = g1.calc_stdev()
print(f'The standard deviation is {stdev:.2f}')  # Notice the decimal formating

# Now change the grades by 10
fixed_amt = 10
g1 = BaseStatistics(grades,fixed_amt)
mean = g1.calc_mean()
print(f'The mean = {mean}')
stdev = g1.calc_stdev()
print(f'The standard deviation is {stdev:.2f}')  # Notice the decimal formating

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
    
grades = [78, 80, 67, 77, 76, 78, 82, 74, 77, 70]
g1 = BaseStatistics(grades)
mean = g1.calc_mean()
print(f'The mean = {mean}')
stdev = g1.calc_stdev()
print(f'The standard deviation is {stdev:.2f}')  # Notice the decimal formating

# Now change the grades by multiplying by 3
factor = 3
g1 = BaseStatistics(grades,factor)
mean = g1.calc_mean()
print(f'The mean = {mean}')
stdev = g1.calc_stdev()
print(f'The standard deviation is {stdev:.2f}')  # Notice the decimal formating

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

def match_sequence(seq):
    matching = []
    for ch in seq:
        if ch == 'A':
            matching.append('C')
        elif ch == 'C':
            matching.append('A')            
        elif ch == 'T':
            matching.append('G')
        elif ch == 'G':
            matching.append('T')
    return ''.join(matching)

protein_strand = 'ACACGTGTCAGTTGTGCAGTACACGTACGTCAGTCAACTGTGACCAGTTGGTCAGT'+ \
    'CAACCAACGTCAGTCAACTGACCACAGTGTCATGACACGTACGT'

# Question 1
seq = 'AGTC'
found = protein_strand.count(seq)
print(f'The gene {seq} was found {found} time(s)')

# Question 2 - Find the opposite
match_seq = match_sequence('CAACTGGT')
print(match_seq)
# now find the sequence
cnt = protein_strand.count(match_seq)
print(f'The matching sequence was found {cnt} time(s)') 
if cnt > 0:
    pos = protein_strand.index(match_seq)
    # remove the piece
    piece1 = protein_strand[:pos]
    print(f'piece 1 - {piece1}')
    piece2 = protein_strand[pos+len(match_seq):]
    print(f'piece 2 - {piece2}')
    
# Question 3 - put in groups of 4
groups = [protein_strand[x*4:(x+1)*4] for x in range(int(len(protein_strand)/4))]
print(groups)
uniq_group = list(set(groups))
print(uniq_group)
pair_count = {}
for pair in groups:
    if pair not in pair_count:
        pair_count[pair] = 0
    pair_count[pair] += 1
print(pair_count)
# Now sort the group
genes = sorted(pair_count.items(), key = lambda kv:kv[1], reverse = True)
print(genes)
# get the max number
max_num = genes[0][1]
# extract everything where the value is the max_num
print([key for key,val in pair_count.items() if val == max_num])

# method 1
for i in range(2000,2752):
    if i % 7 == 0 and not i % 5 == 0:
        print(i, end=',')
print()
print('='*35)
# method 2 - list comprehension
res = [ x for x in range(2000,2752) if x % 7 == 0 and not x % 5 == 0]
print(res)

