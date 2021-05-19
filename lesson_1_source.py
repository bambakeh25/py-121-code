





scores = [91,88,83,84,92,95,88,91,88,86]

# Algorithm for Median

# check the length of list
# sort the list 
    # if length of list is odd 
        # calculate median of odd list 
    # if length of list is even 
        # calculate median of even list 

len(scores) 

# print(scores)
scores.sort()

print(scores)

# what is the median?
    # len of list (which is odd)

# calculating for odd 
if len(scores) % 2 == 1:
    # find the middle index 
    index = int(len(scores)/2)
    oMedian = scores[index]
    print(oMedian)
    
# calculating for even 
if len(scores) % 2 == 0: 
    indexLeft = int((len(scores)/2) - 1)
    indexRight = indexLeft + 1
    eMedian = (scores[indexLeft] + scores[indexRight]) / 2
    print(eMedian)



class BaseStatistics(object):
# Function Definitions 
    def __init__(self,base_list):
        base_list.sort()
        self.ordered = base_list
        self.amt_of_items = len(base_list)

    def calc_mean(self):
        return sum(self.ordered)/self.amt_of_items
        
    def calc_median(self):
        # finding the median of an odd length list
        if self.amt_of_items % 2 == 1: # checking for odd
            index = int(self.amt_of_items/2) # index of middle element in odd list
            median = self.ordered[index]
        else: # getting midpoint of list that is even
            indexLeft  = int(self.amt_of_items/2) - 1 
            indexRight = indexLeft + 1
            median = (self.ordered[indexLeft] + self.ordered[indexRight]) / 2
        return median

    def __str__(self):
        return f"base list: {self.ordered}"

    def __repr__(self):
        return f"base list as repr: {self.ordered}"

# Does mean need to be sorted?
    # answer is no... but we'll need it for median

# Sorting the list
"""
summer_temps = [78, 77, 74, 80, 72]
summer_temps.sort()

print("ODD: ", summer_temps)
print("EVEN: ", fire_flies_per_yard)

stMean = calc_mean(summer_temps)
print("stMean: ", stMean)

fire_flies_per_yard = [22,34,37,14,11,10]
fire_flies_per_yard.sort()

ffMean = calc_mean(fire_flies_per_yard)
print("ffMean: ",ffMean)

# Median calculation of lists
stMedian = calc_median(summer_temps)
print("StMedain: ",stMedian)

ffMedian = calc_median(fire_flies_per_yard)
print("ffMedian: ", ffMedian)

# sorting the list 
"""
#using a class 
summer_temps = [78, 77, 74, 80, 72]
base_stats_obj = BaseStatistics(summer_temps)
base_stats_obj.calc_mean()
base_stats_obj.calc_median()
print(base_stats_obj)
base_stats_obj


   

from pprint import pprint
data = [72,77,79,82,84,77,89, 89]

def create_dictionary(lst):
    new_dict = {}
    for entry in lst:
        if entry not in new_dict:
            new_dict[entry] = 0 
        new_dict[entry] += 1
    return new_dict

def calculate_mode(lst):
    #check if there is no mode
    if len(set(lst)) == len(lst):
        return "there is no mode"
    #mode_dict = {} #another syntax: dict() 
    mode_dict = create_dictionary(lst)

    print(mode_dict)
    max_mode_value = max(mode_dict.values())
    all_modes = [k for k,v in mode_dict.items() if v == max_mode_value]
    return all_modes
#print(list)
all_modes = calculate_mode(data)
#print(set(data))
#set is made of distinct elements 
#if the length of the set (distinct elements ) is different than
#the length of the list, all the values are unique
print(all_modes)






a_dict = {72: 1, 77: 2, 79: 1, 82: 1, 84: 1, 89: 2}
sorted_dict = sorted(a_dict.items(),key=lambda item:item[0],reverse=True)
print(sorted_dict)



#( grades + x) / len(exams + 1) = 90
grades = [88,86,89, 92, 94]

avg = sum(grades) / len(grades)

#find the sum

avg = 90 
#pemdas 
missing_grade = (avg * (len(grades) + 1)) - sum(grades)
print(missing_grade)





grades = [88,86,89, 92, 94]
grades.sort()
print(grades[0])
print(min(grades))



grades = [88,86,89, 92, 94]
grades.sort()
print(grades[-1])
print(max(grades))
print(grades[len(grades) - 1])



grades = [88,86,89, 92, 94]
grades.sort()
range = grades[-1] - grades[0]
print(range)

test_scores = {"regular exam":[.12, [88, 84, 89, 92, 90]],
                "midterm":[.10, [87, 84] ],
                "final exam":[.20, [94]] }
pprint(test_scores) 


class BaseStatistics(object):
# Function Definitions 
    def __init__(self,base_list):
        base_list.sort()
        self.ordered = base_list
        self.amt_of_items = len(base_list)
        self.mode = [] 

    def calc_min(self):
        return self.ordered[0]

    def calc_max(self):
        return self.ordered[-1]

    def calc_range(self):
        return max(self.ordered) - min(self.ordered)
    
    def calc_mean(self):
        return sum(self.ordered)/self.amt_of_items

    def calc_mode(self):
        #create a dict, move through list, keep track counts 
        #
        mode = None
        temp_mode = {}
        for num in self.ordered:
            if num not in temp_mode:
                temp_mode[num] = 0
            temp_mode[num] += 1
        # print(temp_mode)
        ans_sort = sorted(temp_mode.items(),key = lambda kv: kv[1] , reverse = True)   #-> [(1,3), (2,2) ...]
        #highest count 
        highest_count = ans_sort[0]
        if highest_count > 1:
            mode = [mode for fst,snd in ans_sort if highest_count == snd ]
        
        return mode
        
    def calc_median(self):
        # finding the median of an odd length list
        if self.amt_of_items % 2 == 1: # checking for odd
            index = int(self.amt_of_items/2) # index of middle element in odd list
            median = self.ordered[index]
        else: # getting midpoint of list that is even
            indexLeft  = int(self.amt_of_items/2) - 1 
            indexRight = indexLeft + 1
            median = (self.ordered[indexLeft] + self.ordered[indexRight]) / 2
        return median

    def __str__(self):
        return f"base list: {self.ordered} mode: {self.mode}"

    def __repr__(self):
        return f"base list as repr: {self.ordered}"

#using a class 
summer_temps = [78, 77, 74, 80, 72, 80]
base_stats_obj = BaseStatistics(summer_temps)
base_stats_obj.calc_mean()
base_stats_obj.calc_median()
base_stats_obj.calc_mode()
print(base_stats_obj)





