import re

txt="Hello, welcome to the world of Python. Python is great for data science."
match = re.search('Python', txt)
if match:
    print("Match found:", match.group())
    print("Start index:", match.start())
    print("End index:", match.end())

#Find all occurrences of 'Python'
matches = re.findall('Python', txt, re.IGNORECASE)     
print("All matches:", matches)
print("Number of matches:", len(matches))
#Replace 'Python' with 'programming'
new_txt = re.sub('Python', 'programming', txt)
print("Modified text:", new_txt)
