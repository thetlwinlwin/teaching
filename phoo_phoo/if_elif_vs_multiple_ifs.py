status = ["gold", "student"]

if "gold" in status:
    print("Apply 20% discount")
if "silver" in status:
    print("Apply 10% discount")
if "student" in status:
    print("Apply 5% discount")

print('done')

if "silver" in status:
    print("Apply 10% discount")
elif "student" in status:
    print("Apply 5% discount")
elif "gold" in status:
    print("Apply 20% discount")
