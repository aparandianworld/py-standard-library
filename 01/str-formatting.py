from string import Template
import datetime

sample_str = "The quick brown $animal $action the lazy dog on 3rd of December 2025."

template = Template(sample_str)
output_str = template.substitute(animal="fox", action="jumps over")
print(output_str)

# another way with a dict
subs_dict = {"animal": "fox", "action": "jumps over"}

output_str = template.substitute(subs_dict)
print(output_str)


fname = "Aaron"
lname = "Parandian"

print("Hello, my name is {} {}".format(fname, lname))
print("Hello, my name is {0} {1}".format(fname, lname))
print("Hello, my name is {v1} {v2}".format(v1=fname, v2=lname))
print(f"Hello, my name is {fname} {lname}")

product = "MacBook Pro"
price = 999
tax = 0.059
new_year = datetime.datetime(2026, 1, 1)

print(
    f"The {product} price is ${price} with tax {tax:.2f}% the total is ${round(price + (price * tax), 2)} on {new_year:%B %d, %Y}"
)
