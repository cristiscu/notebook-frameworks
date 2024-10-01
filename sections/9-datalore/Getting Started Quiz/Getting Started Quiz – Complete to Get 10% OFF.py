# -*- coding: utf-8 -*-

# -- Editor --

discount_value = 10

# ## Getting Started Quiz – Complete to Get {{discount_value}}% OFF Your Datalore Cloud Subscription
# 
# Hello and welcome to Datalore!
# Datalore is a collaborative data science platform developed by JetBrains.
# Get started right away by running the Python code cell above, then execute this cell, and see how you can **print variables within your Markdown cells**.
# 
# 🧩 **Excited to complete the quiz and help your team save on a Datalore Cloud subscription?**
# 
# Solve these 8 puzzles and get a discount code to use at checkout: datalore.jetbrains.com/pricing/
# 
# 🚨 **Don't delay completing this tutorial, as certain features will be available only during your 14-day Datalore Cloud trial!**
# 
# Here are the quick links to each puzzle:
# 
# - [1st 🧩](#Watch-this-2-minute-Datalore-overview-and-get-your-first-piece-of-the-puzzle-🧩)
# - [2nd 🧩](#Check-dataset-statistics-and-reveal-the-second-piece-of-the-puzzle-🧩)
# - [3rd 🧩](#Connect-a-database,-run-your-first-SQL-query,-and-reveal-the-third-piece-of-the-puzzle-🧩)
# - [4th 🧩](#Explore-the-possibilities-of-Datalore-AI-🧩)
# - [5th 🧩](#Learn-how-to-manage-the-environment-and-explore-installed-packages-to-get-your-fifth-piece-of-the-puzzle🧩)
# - [6th 🧩 - This one is very easy!](#Learn-about-Datalore's-collaborative-features-and-find-the-sixth-piece-of-the-puzzle-🧩-–-This-one-is-easy!)
# - [7th 🧩](#Great-job-so-far-on-progressing-through-the-quiz!)
# - [8th 🧩](#Last-but-not-least,-learn-to-schedule-notebook-and-report-updates-and-explore-computation-options)


# This tutorial is a great place to learn about the essential Datalore features. For more information, you can:
# - Visit our [Documentation](https://www.jetbrains.com/help/datalore/datalore-quickstart.html), which includes guides on specific features.
# - Subscribe to the [Datalore's blog](https://blog.jetbrains.com/datalore/) to receive emails about feature announcements and Datalore tutorials!


# ## Watch this 2-minute Datalore overview and get your first piece of the puzzle 🧩
# 
# Get a quick overview of a complete analysis workflow in Datalore. Follow along as we optimize an investment portfolio and share results with stakeholders.
# 
# <div align="center"><video width="800" height="450" controls>
# 
# <source src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos-2024/Master+Datalore+In+2+Minutes+%E2%80%93+Quick+Datalore+Overview.mov" type="video/mp4">
# 
# </video></div>
# 
# 
# **Now that you've watched the video, let’s see if you can reveal the first digits in the discount code 🧩:**
# 
# How many letters are there in the database type that Alena connected to the notebook in her video? Count the letters and enter the number in the cell below:


## Input the first piece of the puzzle within the ""

part_1 = "10"

# ## Check dataset statistics and reveal the second piece of the puzzle 🧩
# 
# 1. Run the cell below to download and print a dataset. If instead of the *print(data)* command you just specify the variable name *data* at the end of the cell, Datalore will display it as an interactive table.
# 2. Go to the *Statistics* tab and identify the column that contains outliers.
# 3. Get the first letters of both words in the column name. This is the second piece of the puzzle.


import pandas as pd

data = pd.read_csv("https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/cleaned_financial_data.csv")
data.to_csv("dataset.csv")
data

## Input the second piece of the puzzle within the ""

part_2 = ""

# ## Watch a Datalore editor overview to discover other productivity-boosting features
# 
# Learn how to:
# - Create and import Python, SQL, R, and Scala notebooks.
# - Add new code cells, Markdown, and interactive controls.
# - Get access to attached data, the environment manager, computation settings, the table of contents, the variable viewer, and the notebook file system.
# 
# <div align="center"><video width="800" height="450" controls>
# 
# <source src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos-2024/Datalore+Notebooks+Overview.mov" type="video/mp4">
# 
# </video></div>


# 💡 This tutorial is split into several **worksheets**. Navigate through the tabs at the top of the editor or use the table of contents on the left-hand sidebar.
# 
# Please navigate to the ***Data*** tab to continue this tutorial.
# 
# <div><img src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos-2024/header.png" width = 900 border="2" style="border-color: #d3d3d3; margin-top: 1%;"/></div>


# -- Data --

# ## Connect a database, run your first SQL query, and reveal the third piece of the puzzle 🧩
# 
# Whether you work with CSV files, S3 buckets, or SQL databases, Datalore offers you easy ways to access and query your data from multiple sources in one notebook. Watch the overview of data integrations and connect your first database to run a SQL query.
# 
# 
# <div align="center"><video width="800" height="450" controls>
# 
# <source src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos-2024/Datalore+Data+Integrations+Overview.mov">
# 
# </video></div>
# 
# Follow these steps:
# 1. Open *Attached data* and create a new PostgreSQL database connection
# 2. Choose *Connection type: URL only* and input the following credentials::
#     - User: datalore
#     - Password: datalore
#     - URL: jdbc:postgresql://demo-database.private.datalore.io:5432/datalore
#  
# 3. Add a new SQL cell, browse the database schema, and then, from the yahoo_data table, query all the rows where "Ticker" = 'META'. The SQL query result is automatically saved to a pandas dataframe that we will use further in our notebook.
# 4. Apply the following filters **by using interactive table options**:
#     1. Filter by *Open* > 280
#    <div><img src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos-2024/filter_table.png" width = 400 border="2" style="border-color: #d3d3d3; margin-top: 1%;"/></div>
#     2. Sort ascending by Open
# 5. Get the first letter of the month in the first row in the table – this is your third piece of the puzzle.


## Input the third piece of the puzzle within the ""
part_3 = ""

# Now, please navigate to the ***Datalore AI*** tab to continue this tutorial.


# -- Datalore AI --

# ## Explore the possibilities of Datalore AI 🧩
# 
# Datalore AI currently offers 3 major features:
# 
# - The ability to generate and edit Python, SQL, R, and Scala code, as well as Markdown text.
# - *Datalore Autopilot*, which suggests next steps for your analysis.
# - A *Fix error* feature to help you debug your code.
# 
# Watch this short overview of the AI features and then reveal your fourth piece of the puzzle!
# 
# <div align="center"><video width="800" height="450" controls>
# 
# <source src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos-2024/Datalore+AI+Assistant+Overview.mov">
# 
# </video></div>
# 
# Steps to follow:
# 1. Open Datalore Autopilot.
# 3. Go to the cell settings and choose to include outputs in the prompt. This will ensure that the code generated is of higher quality.
# 4. Click on the 💡 icon to explore the available AI suggestions.
# 5. Copy and input the following custom prompt and then click the send icon: 
#    
# ***Visualize 'Open' and 'Adj Close' for df_1 using the Plotly package.***
# 
# 5. Explore the resulting plot. 
# 6. Write the first digit of the highest Adj close price as the solution to the fourth piece of the puzzle.


## Input the fourth piece of the puzzle within the ""

part_4 = ""

# Please navigate to the ***Environment*** tab to continue this tutorial.


# -- Environment --

# ## Learn how to manage the environment and explore installed packages to get your fifth piece of the puzzle🧩
# 
# Watch a short overview video and then complete the task below.
# 
# <div align="center"><video width="800" height="450" controls>
# 
# <source src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos-2024/Datalore+Environment+Manager+Overview.mov">
# 
# </video></div>
# 
# Steps:
# 1. Go to *Environment | Packages | Installed*.
# 2. Check whether the *scikit-learn* package is pre-installed. If it is, enter a *Y* symbol as the fifth piece of the discount code puzzle. Otherwise, enter an *N*.


## Input the fifth piece of the puzzle within the ""
part_5 = ""

# Please navigate to the ***Sharing tab*** to continue this tutorial.


# -- Sharing --

# ## Learn about Datalore's collaborative features and find the sixth piece of the puzzle 🧩 – This one is easy!
# 
# <div align="center"><video width="800" height="450" controls>
# 
# <source src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos-2024/Datalore+Collaboration+Overview.mov">
# 
# </video></div>
# 
# **What is the name of Datalore's internal versioning tool? The last letter of the name will give you your next piece of the puzzle 🧩.**


## Input the sixth piece of the puzzle within the ""
part_6 = ""

# Please navigate to the ***Reporting*** tab to continue this tutorial.


# -- Reporting --

# ## Great job so far on progressing through the quiz!
# 
# **You have two more worksheets to go and two more parts of the puzzle to solve!**
# 
# Datalore helps turn your Jupyter notebooks into beautiful reports. Add interactive controls, arrange notebook cells on the canvas, and publish your report with one click. Share your work with stakeholders by link and schedule automatic report updates.
# 
# Watch the tutorial below and complete the task.
# 
# <div align="center"><video width="800" height="450" controls>
# 
# <source src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos-2024/Datalore+Reporting+Overview.mov">
# 
# </video></div>
# 
# **Task 🧩:**
# 1. Click the *Build report* button in the upper right-hand corner.
# 2. Play with arranging the cells on the canvas.
# 3. Click *Publish report* and see the *Report type* options.
# 4. What is the second option? The first letter of the option is the seventh piece of the puzzle. 🧩.


# 💡 **Pro tip:** You can leave cell **comments** on both notebooks and reports.
# 
# When somebody leaves a comment in your published report, you will see it reflected in the corresponding notebook cell. Tag people by mentioning their email addresses, reply to their comments, and resolve the threads. Once you get a comment, you'll be notified via email. If you want to disable comment notifications, go to *Account settings | Notifications* by clicking on your avatar.


## Input the seventh piece of the puzzle within the ""

part_7 = ""

# Please navigate to the ***Scheduling and Computation*** tab to continue this tutorial.


# -- Scheduling and Computation --

# ## Last but not least, learn to schedule notebook and report updates and explore computation options
# 
# In our last tutorial, you will learn everything about the Computation tab of the left-hand sidebar.
# 
# <div align="center"><video width="800" height="450" controls>
# 
# <source src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos-2024/Datalore+Scheduling+and+Computation+Overview.mov">
# 
# </video></div>
# 
# Your last task 🧩 ? Open the notebook and click *Run all*. Then check the eighth piece of the puzzle in the cell below.


part_7_str = "Congratulations on making it to the end! It’s time to move on to the last worksheet.\nThe last piece of the puzzle is: "
part_8 = str(part_7_str.__len__())
print(part_7_str + part_8)

# -- Results --

# ## Now that you have the full puzzle, let's print it out!
# 
# Then try applying the code at checkout:  datalore.jetbrains.com/pricing/


discount_code = part_1 + part_2 + part_3 + part_4 + part_5 + part_6 + part_7 + part_8
print(discount_code)

# ## If you want to learn more, subscribe to our [blog](https://blog.jetbrains.com/datalore/) updates!


# ## Have questions or need support?
# 
# Our team would love to hear about your experience using Datalore. Feel free to share your feedback with us and report any issues you’ve run into via ***Help | Feedback & Support***.
# 
# <div><img src="https://datalore-samples.s3.eu-west-1.amazonaws.com/getting-started/videos-2024/Help.png" width = 400 border="2" style="border-color: #d3d3d3; margin-top: 1%;"/></div>


