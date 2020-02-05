# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data= pd.read_csv(path)
data.rename(columns={"Total":"Total_Medals"}, inplace=True)

data.head(10)


# --------------
#Code starts here

data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')
data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event'])

better_event = data['Better_Event'].value_counts().idxmax()

# better_event= 


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
last_row_index=top_countries.index.max()
top_countries.drop(index=last_row_index,inplace=True)

def top_ten(df,column_name):
    country_list = list(df.nlargest(10,column_name)['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')

set_top_10 = set(top_10)
set_top_10_summer = set(top_10_summer)
set_top_10_winter = set(top_10_winter)

common = list(set_top_10.intersection(set_top_10_summer.intersection(set_top_10_winter)))




# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

def plotGraph(df,column_name):
    objects = df['Country_Name']
    y_pos = np.arange(len(objects))
    performance = df[column_name]

    plt.barh(y_pos, performance, align='center', alpha=0.5)
    plt.yticks(y_pos, objects)
    plt.xlabel('Total Medals')
    plt.title('Country Name Vs Medals in Respective Events')
    plt.show()

plotGraph(summer_df,'Total_Summer')
plotGraph(winter_df,'Total_Winter')
plotGraph(top_df,'Total_Medals')


# --------------

#Code starts here

# FOR SUMMER_DF
summer_df['Golden_Ratio'] = (summer_df['Gold_Summer']/summer_df['Total_Summer'])
summer_max_ratio = max(summer_df['Golden_Ratio'])
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax()]['Country_Name']

# FOR WINTER DF
winter_df['Golden_Ratio'] = (winter_df['Gold_Winter']/winter_df['Total_Winter'])
winter_max_ratio = max(winter_df['Golden_Ratio'])
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax()]['Country_Name']

# FOR TOP DF
top_df['Golden_Ratio'] = (top_df['Gold_Total']/top_df['Total_Medals'])
top_max_ratio = max(top_df['Golden_Ratio'])
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax()]['Country_Name']


# --------------
#Code starts here
data_1 = data.drop(index=data.index.max())

# Total Point Column Creation
data_1['Total_Points'] = (data_1['Gold_Total']*3) + (data_1['Silver_Total']*2) + (data_1['Bronze_Total']*1)

# Calculate Max Points
most_points= max(data_1['Total_Points'])

# Get Best Country
best_country = data_1.loc[data_1['Total_Points'].idxmax()]['Country_Name']


# --------------
#Code starts here

best_country = data_1.loc[data_1['Total_Points'].idxmax()]['Country_Name']
best = data[data['Country_Name']==best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar()
plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation=45)


