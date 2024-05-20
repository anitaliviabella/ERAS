import pandas as pd

# Step 1: Read the CSV file into a DataFrame
df = pd.read_csv('topic_modeling/topics/1989_topics.csv')

# Step 2: Convert the DataFrame to an HTML table
html_table = df.to_html()

# Step 3: Save the HTML table to an HTML file
with open('1989_topics.html', 'w') as file:
    file.write(html_table)

######

# Step 1: Read the CSV file into a DataFrame
df2 = pd.read_csv('topic_modeling/topics/taylorswift_topics.csv')

# Step 2: Convert the DataFrame to an HTML table
html_table = df2.to_html()

# Step 3: Save the HTML table to an HTML file
with open('debut_topics.html', 'w') as file:
    file.write(html_table)

#######
# Step 1: Read the CSV file into a DataFrame
df3 = pd.read_csv('topic_modeling/topics/fearless_topics.csv')

# Step 2: Convert the DataFrame to an HTML table
html_table = df3.to_html()

# Step 3: Save the HTML table to an HTML file
with open('fearless_topics.html', 'w') as file:
    file.write(html_table)


#####
# Step 1: Read the CSV file into a DataFrame
df4 = pd.read_csv('topic_modeling/topics/speaknow_topics.csv')

# Step 2: Convert the DataFrame to an HTML table
html_table = df4.to_html()

# Step 3: Save the HTML table to an HTML file
with open('speaknow_topics.html', 'w') as file:
    file.write(html_table)

####
# Step 1: Read the CSV file into a DataFrame
df5 = pd.read_csv('topic_modeling/topics/red_topics.csv')

# Step 2: Convert the DataFrame to an HTML table
html_table = df5.to_html()

# Step 3: Save the HTML table to an HTML file
with open('red_topics.html', 'w') as file:
    file.write(html_table)


####
# Step 1: Read the CSV file into a DataFrame
df6 = pd.read_csv('topic_modeling/topics/reputation_topics.csv')

# Step 2: Convert the DataFrame to an HTML table
html_table = df6.to_html()

# Step 3: Save the HTML table to an HTML file
with open('reputation_topics.html', 'w') as file:
    file.write(html_table)

####
# Step 1: Read the CSV file into a DataFrame
df7 = pd.read_csv('topic_modeling/topics/lover_topics.csv')

# Step 2: Convert the DataFrame to an HTML table
html_table = df7.to_html()

# Step 3: Save the HTML table to an HTML file
with open('lover_topics.html', 'w') as file:
    file.write(html_table)

####
# Step 1: Read the CSV file into a DataFrame
df8 = pd.read_csv('topic_modeling/topics/folklore_topics.csv')

# Step 2: Convert the DataFrame to an HTML table
html_table = df8.to_html()

# Step 3: Save the HTML table to an HTML file
with open('folklore_topics.html', 'w') as file:
    file.write(html_table)

####
# Step 1: Read the CSV file into a DataFrame
df9 = pd.read_csv('topic_modeling/topics/evermore_topics.csv')

# Step 2: Convert the DataFrame to an HTML table
html_table = df9.to_html()

# Step 3: Save the HTML table to an HTML file
with open('evermore_topics.html', 'w') as file:
    file.write(html_table)

####
# Step 1: Read the CSV file into a DataFrame
df10 = pd.read_csv('topic_modeling/topics/midnights_topics.csv')

# Step 2: Convert the DataFrame to an HTML table
html_table = df10.to_html()

# Step 3: Save the HTML table to an HTML file
with open('midnights.html', 'w') as file:
    file.write(html_table)

####
# Step 1: Read the CSV file into a DataFrame
df11 = pd.read_csv('topic_modeling/topics/ttps_topics.csv')

# Step 2: Convert the DataFrame to an HTML table
html_table = df11.to_html()

# Step 3: Save the HTML table to an HTML file
with open('ttps.html', 'w') as file:
    file.write(html_table)
