
#%% IMPORTING MODULES
import random
from functools import reduce
import matplotlib.pyplot as plt

#%% GENERATING RANDOM NUMBERS
listOfNumbers = [random.randint(1, 10) for i in range(100)]
print("listOfNumbers: ", listOfNumbers)

#%% MAPPING FUNCTION
mapped_data = list(map(lambda x: x**2, listOfNumbers))
print("mapped data:", mapped_data)
# %% REDUCE FUNCTION

result = reduce(lambda x, y: x + y, mapped_data)

print( "mapped data:", mapped_data)
print("reduced result:", result)

#%% TOKENS USING MAP AND REDUCE

text = """IA Technology refers to the use of artificial intelligence (AI) and automation technologies together 
to create intelligent business processes. It combines machine learning, natural language processing, 
robotic process automation, and cognitive automation to streamline operations, 
enhance decision-making, and improve efficiency across various industries """


dict= {}

for word in text.split():
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1
print("final dict:",dict)
# %%
