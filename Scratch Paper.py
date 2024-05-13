a = {
    'car1': ('high cp', 'low fd', 'safe'),
    'car2': ('med cp', 'med fd', 'safe'),
    'car3': ('low cp', 'high fd', 'safe'),
    'taxi1': ('high cp', 'low fd', 'safe', 'med wt'),
    'taxi2': ('high cp', 'low fd', 'safe', 'high wt'),
    'taxi3': ('high cp', 'low fd', 'safe', 'high wt')
}

# Create a new dictionary with keys starting with 'car'
res = {k: v for k, v in a.items() if k.startswith('taxi1')}

print("\n\n")

print(res)

print("\n\n")

my_dict = {"a": 1, "b": 2, "c": 3}
filtered_dict = {key: value for key, value in my_dict.items() if key.startswith("a")}
print(filtered_dict)