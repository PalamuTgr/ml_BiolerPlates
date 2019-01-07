import matplotlib.pyplot as plt
cnt_srs = df['target'].value_counts()
labels = df['target'].unique()

fig1, ax1 = plt.subplots()
ax1.pie(cnt_srs, labels=labels, autopct='%1.1f%%', startangle=90)

#draw circle
centre_circle = plt.Circle((0,0),0.70,fc='white')

fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')  
plt.tight_layout()
plt.show()
