import streamlit as st
from faker import Faker
import pandas as pd
from random import randrange

st.title("My App")

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
st.dataframe(df)
#print(df)

import matplotlib.pyplot as plt

#bins = st.sidebar.slider("Bins:", value=10, min_value=3, max_value=20, step=1)
df.hist(column="age", bins=10)
st.pyplot(plt)
#plt.show()