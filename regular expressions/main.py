import itertools
import re

# Define the regular expressions
regex1 = "(a|b)(c|d)E+G?"
regex2 = "P(Q|R|S)T(UV|W|X)*Z+"
regex3 = "1(0|1)*2(3|4)536"


# Function to generate combinations for a given regex pattern
def generate_combinations(regex, limit=5):
    # Extract the variable parts of the regex
    parts = re.findall(r'\((.*?)\)', regex)
    parts = [part.split('|') for part in parts]

    # Generate all combinations with a limit on repetitions for '+' and '*'
    for combination in itertools.product(*parts):
        result = regex
        for i, part in enumerate(combination):
            result = re.sub(r'\(.*?\)', part, result, count=1)
        result = re.sub(r'\+', lambda x: x.group(0)[0] * limit, result)
        result = re.sub(r'\*', lambda x: x.group(0)[0] * limit, result)
        result = re.sub(r'\?', lambda x: x.group(0)[0] if i % 2 == 0 else '', result)
        yield result


# Generate and print combinations for each regex pattern
for i, regex in enumerate([regex1, regex2, regex3], start=1):
    print(f"Combinations for regex {i}:")
    for combo in generate_combinations(regex):
        print(combo)
