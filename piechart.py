import matplotlib.pyplot as plt

# # Line Graph with markers
# # years = [1950,1955,1960,1965,1970,1975,1980,1985,1990,1995,
# #          2000,2005,2010,2015,2020]
# #
# # pops = [2.5,2.7,3,3.3,3.6,4,4.4,4.8,5.3,5.7,
# #         6.1,6.5,6.9,7.3,7.7]
# #
# # deaths = [1.2, 1.7, 1.8, 2.2, 2.5, 2.7, 2.9, 3, 3.1, 3.3,
# #           3.5, 3.8, 4.0, 4.3, 4.6]
# #
# # lines = plt.plot(years, pops, years, deaths)
# # plt.grid(True)
# #
# # plt.setp(lines, color=(1,.4,.4), marker="o")
# # plt.show()
# #
# Pie Chart
#
# labels = "Python", "C++", "Ruby", "Java", "PHP", "Perl"
# sizes =[33,52,12,17,62,48]
# separated = (.1,.2,.3,0,0,0)
#
# plt.pie(sizes, labels=labels, autopct="%1.1f%%", explode=separated)
# plt.axis("equal")
# plt.show()

# Pandas
import pandas as pd

#traditional method
# data= [{
#     'name': 'Nick',
#     'jan_ir': '124',
#     'feb_ir': '100',
#     'march_ir': '165',
# },]

#Pandas method
raw_data = {'names': ['Nick', 'Panda', 'S', 'Ari', 'Valos'],
            'jan_ir': [143,122,101,106,365],
            'feb_ir': [122,132,144,98,62],
            'march_ir': [65,88,12,32,65]}

df = pd.DataFrame(raw_data, columns=['names', 'jan_ir', 'feb_ir', 'march_ir'])

df['total_ir'] = df['jan_ir'] + df['feb_ir'] + df['march_ir']

#Pandas pie chart
color =[(1,.4,.4), (1,.6,1), (.5,.3,1), (.3,1,.5), (.7,.7,.2)]
plt.pie(df['total_ir'],
        labels=df['names'],
        colors=color,
        autopct='%1.1f%%')

plt.axis('equal')
plt.show()
