import pandas as pd

student_id = list(range(1, 21))
names = ["Student" + str(i) for i in range(1, 21)]
ages = [16] * 20
subjects = ["Math"] * 20
scores = [80] * 20

data = {
    "ID": student_id,
    "Name": names,
    "Age": ages,
    "Subject": subjects,
    "Score": scores
}

df = pd.DataFrame(data)

print(df)

df.to_csv("students.csv", index=False)
