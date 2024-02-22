import json

stringA = '[{"geeks": 2},"for", 4, "geeks",3]'

# Type check

res = json.loads(stringA)
# Result
print("The converted list : \n",type(res))