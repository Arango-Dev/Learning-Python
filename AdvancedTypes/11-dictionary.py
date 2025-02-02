point = {"x": 25, "y": 50}
point["z"] = 45
print(point, point["x"])
if "n" in point:
    print("found:", point["n"])

print(point.get("n"))

del point["z"]

print(point)
