from faker import Faker
import pandas as pd
from random import randrange

fake = Faker()
output = [{
        "name": fake.name(),
        "address": fake.address(),
        "city": fake.city(),
        "state": fake.state(),
        "email": fake.email(),
        "age": 10 + randrange(70)
    } for _ in range(100)]
df = pd.DataFrame(output)
print(df)

import matplotlib.pyplot as plt

df.hist(column="age", bins=10)
plt.show()