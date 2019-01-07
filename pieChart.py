import matplotlib.pyplot as plt
%matplotlib inline

## target count ##
cnt_srs = df['target'].value_counts()
labels = df['target'].unique()
explode = (0.00, 0.15)


fig1, ax1 = plt.subplots()
ax1.pie(cnt_srs, labels = labels,explode = explode, autopct='%1.1f%%',
        shadow=True, startangle=90)
# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')  
plt.tight_layout()
plt.show()
