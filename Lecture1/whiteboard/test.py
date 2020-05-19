stuff = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}

# loop through stuff
# check the value of each (kv pair)
# if val == int, add together

arr = []

for x, y in stuff.items():
    if isinstance(y, int):
        arr.append(y)

print(sum(arr))