###################################################################################################################################################################
######################################################################## DATA QUALITY #############################################################################
###################################################################################################################################################################

###################################################################################################################################################################
######################################################################## Data inspection ##########################################################################
"""
The first thing to do before exploring a dataset is to take an interest in the metadata, if there are any, and the information we have on the data:

- Where does this data come from? 
- How was this data collected?
- What types of files do we have? 
- - What sizes? 
- What are the characteristics present?

Manually collected datasets often contain errors or approximations. Faced with such data, it is necessary to clean them up, 
and to keep in mind that they are not always representative of reality.

Here, for example, it is stated that not all sales have been digitized. We are therefore missing some of the data.

"""

## Display the information of the DataFrame
# print( "Customers info :\n")
# customers.info()

"""
It is recommended to check that the types of variables associated with each column agree with what these columns represent.

Here is a table of correspondence of the data types of pandas with those of python and numpy:

dtype pandas	    type python	        type numpy	                            usage
object	            str or mixed	    str or mixed	                        Text or a mixture of numeric and non-numeric values
int64	            int	int_            (8/16/32/64), uint_ (8/16/32/64)	    Integers
float64	            float	            float_ (16/32/64)	                    Decimal numbers
bool	            bool	            bool	                                True / False
datetime64	        datetime	        datetime64 [ns]	                        Dates and time values
timedelta [ns]	    NA	                NA	                                    Difference between two dates
category	        NA	                NA	                                    Finite list of textual data


"""

########################################### Data standardization - ensure that each variable is of the correct type ###############################################

## Transform the 'Postal code' column into character strings (type: str) using the .astype () method.
# customers['Postal code'] = customers['Postal code'].astype(str)

"""
Some variables have a defined syntax / format / interval and it is necessary to ensure that these properties are respected.
"""

## Check that the postal codes all correspond to a 5-digit numeric code, between 01000 and 96000.
#count_correct_postal_codes = 0
#count_total = len(customers['Postal code'])

# for pos, value in enumerate(customers['Postal code']):
#    if len(str(value)) == 5 and str(value).isnumeric() and '01000' < str(value) < '96000':
#        count_correct_postal_codes += 1 
#    else:
#        count_correct_postal_codes += 0

# print(f"{count_correct_postal_codes} of {count_total} postal codes have the correct format.")

########################################### Data standardization - ensure consistency of data format ##############################################################
"""
To ensure the quality of the data, it is also necessary to check the consistency of the latter. 
When it is collected by different people, over long periods of time, it often happens that the data is not written in the same way.

The objective of this step is to ensure that each line follows the same rules, and that 2 lines which contain the same information cannot be written 
in 2 different ways.
"""

## Standardize the telephone numbers.
# for (index, numero) in enumerate(customers["Phone number"]):
#    if numero[0]=='+':
#        customers.loc[index, 'Phone number']='0' + customers.loc[index, 'Phone number'][4:]

## Capitalize the columns 'Name' and 'City' of customers. Hint: try using .apply.
# customers['Name'] = customers['Name'].apply(lambda x : x.upper())  

# customers['City'] = customers['City'].apply(lambda x : x.upper())

## Print the unique values of the column City. Ensure the data is valid by correcting the incorrect city names:
# print(customers['City'].unique())

    # We realize that "RENES" and "PERPINAN" are misspelled, and that "PARIS LA DÉFENSE" is duplicated with "PARIS".
#customers.replace({'RENES' : 'RENNES', 
#                 'PERPINAN' : 'PERPIGNAN',
#                 'PARIS LA DÉFENSE' : 'PARIS'},
#                inplace = True)

"""
When analyzing data, it is also very important to ensure the uniqueness of certain variables. 
In particular with the text variables, which may have been filled in in different ways to designate the same person / entity.

Example: The variable 'Country' 'of a dataset could contain both the values "GB", "United Kingdom" and "UK" which nevertheless designate the same country, 
this which could lead to erroneous analyzes subsequently.
"""

########################################### Data standardization - manage duplicates ##############################################################################
"""
Duplicates are also a source of errors and can sometimes distort the analyzes carried out on the data which contains them. With some exceptions, 
it is generally preferable to delete fully copied rows to ensure good validity of the data.
"""

## Displays the number of duplicates
# print("Number of duplicates:", customers.duplicated().sum())

## Delete duplicates
# customers = customers.drop_duplicates()

########################################### Data standardization - manage dates ###################################################################################
"""
Dates are an often problematic type of format, and you should always ensure consistency between different dated variables before using a dataset. 
They must be: of the same type, in the same format and correspond to real dates. For this, we often use the pandas function to_datetime. Here is an example of 
how to use it:

pd.to_datetime('2030-26-10',
               format='%Y-%d-%m')

>>> Timestamp('2030-10-26 00:00:00')     
In the previous example, we convert the date '2030-26-10' into a datatime object. The parameter format is used to specify the format of the input date 
(in this case '2030-26-10'). To introduce how to write the format of a date, here are some commonly used formats:

    ('YYYY-MM-DD', format='%Y-%d-%m')  
    ('YYYY/MM/DD', format='%Y/%d/%m')
    ('YY/MM/DD', format='%y/%d/%m')

Here, we use %Y, %m and %d to specify the year, month and day respectively. Notice that for the third example, since the year only has the last two digits, 
we use %y.

    When converting a date that uses %y, the output always has a year strictly greater than 1968. For example, take the following dates of 
    format %y/%m/%d: 68/10/01 and 69/10/01. They will be converted to 2068/10/01 and 1969/10/01 respectively.

It may also happen that you have a date and time together. You can include this format using %H, %M and %S for hours, minutes and seconds. 
This can be seen in the following example:

    pd.to_datetime('2018-10-26 12:00:00',
                    format='%Y-%m-%d %H:%M:%S')

>>> Timestamp('2018-10-26 12:00:00')
You can use this function on arrays, Series and DataFrames. Here we covered the basics, but this function can do much more. 
View the documentation or help() for more parameters and examples of use. Likewise, other alternatives like the datetime library can be used.

"""

## In the Sales_2017 dataframe, what types are the variables 'Delivery date' and 'Order date' ?
# Sales_2017["Order date"].dtype # => 0 = object
# Sales_2017["Delivery date"].dtype # => 0 = object

## Transform these two variables so that they are of type datetime and in the format: "%Y-%m-%d"
# Sales_2017["Order date"] = pd.to_datetime(Sales_2017["Order date"], format = "%m/%d/%y")
# Sales_2017["Delivery date"] = pd.to_datetime(Sales_2017["Delivery date"], format = "%Y-%m-%d")

##################################################################################################################################################################
######################################################################## Missing values ##########################################################################

"""
In statistics, we speak of missing data or missing values when no value has been entered for a given variable, for a given observation.

Missing values are common and can have a significant effect on the visualization, analysis, performance of predictions, or any other use of the data that 
contains them.

The proper management of missing data is therefore fundamental to ensure the completeness of a data set as well as its precision when it comes to replacing them.

Here are some of the main reasons why a dataset may have missing data:

    - The user forgot to fill in a field.
    - Data was lost during manual transfer from an old database.
    - There was a programming error.
    - The user has chosen not to fill in a field related to his beliefs about how the results would be used or interpreted.
    - Sometimes these are just random errors; other times it is a systematic problem.

It is important to understand these different types of missing data from a statistical point of view. The type of missing data will influence how you 
replace missing values.

"""

############################################# Identifications of missing values ###################################################################################
"""
The table display shows that some data is missing (NaN). These standard missing values are the ones that pandas automatically detect.

When a table imported with pandas contains empty boxes, they are automatically detected and replaced by NaN. The same goes for boxes containing NA,N/A or 
n/a in the file.

In order to easily detect missing values and on any type of array, all you have to do is use the isna() and notna() functions, which also have their equivalents 
in methods for DataFrames and Series.

The first returns True for each missing element and False otherwise. The second returns the opposite.
"""

## Display the total number of missing values per column of Products, using the sum() method.
# products.isna().sum()
# or products.notna().sum()
    
##For each product in the table (therefore each row), display whether the variable 'Category' is present or not.
# products["Category"].isna()

"""
This gives a summary of the completeness of the different columns. The use of isna() is recommended, because in Python, 2 two NaN are not equal when comparing. 
Indeed, unlike two None which can be compared, the operation:

np.nan == np.nan
returns False.

So the comparison between an element of the Data Frame and a None or a np.nan cannot be used to check the presence or not of missing values.
"""


"""
Surprisingly, in addition to the 3 classic types of sales channel, we observe the "?" and "na" modalities, which obviously also designate missing values.

These different types of missing values can come from different tools/languages or have been entered manually.

To be recognized directly by pandas when reading a file, it is possible to add them to a list and then insert this list to the function used to read the file. 
This can be achieved using the parameter na_values.
"""

## Read the file "Sales2019.xlsx" again, specifying that the " ", "?" and "na" must be treated as missing values using the na_values argument.
# Sales = pd.read_excel("Sales2019.xlsx", na_values = [" ", "?", "na"])
# pd.isna(Sales).sum()

"""
The " ", "?" and "na" have been replaced by missing values and are therefore now correctly identified by pandas.

However, sometimes certain tools / people use other means to indicate the missing values, in particular for the numeric variables, by indicating them by -1, 
999 or even 0 in some cases.
"""

## Display the mathematical description of the variable 'Quantity'.
# Sales["Quantity"].describe()

"""
The maximum number of quantity is indeed 12, but the minimum is equal to -1, which does not make sense for a quantity of products sold.

Orders whose quantity is -1 are therefore orders whose quantity is not indicated, for various reasons, and should be considered as a missing value.
"""

## Replace all the values of 'Quantity' outside the interval [5,12] by np.nan (note: we could have replaced only the value -1 by missing values, 
## but you see how to do it with an interval).
# Sales.loc[(Sales["Quantity"] < 5) | (Sales["Quantity"] > 12), "Quantity"] = np.nan

# or
# Sales.Quantity.replace(-1, np.nan, inplace=True) # do not forget: inplace=True

"""
Calculations with missing data:
    All the calculation or statistical methods seen in the previous modules take into account the missing values.

    For example, during a sum, missing values are considered zero. For a product, the missing values ​ are considered equal to 1.

    The sum of an empty or completely filled series or column of NA is therefore 0.
    The product of an empty or completely filled series or column of NA is therefore 1.

"""


################################################# Replacement of missing values ###################################################################################
"""
All the missing values of our DataFrames are now well identified. To carry out the analyzes, models or other uses which will be made of them, it is essential to 
replace them appropriately.

The fillna() method allows you to replace missing values with other values, in several ways:

To replace all the NAs of a Series or a DataFrame with the same value, all you have to do is indicate this value in the method.
Example:

    df.fillna (0) # to replace all NAs with 0

The method parameter allows to use the previous non-missing values (method = 'pad') or following (method ='bfill') to replace the missing values of a Series.
Example:

    df.fillna (method = 'pad') # each NA will be replaced by the last non-NA value in its column

It is also possible to use a dictionary or a series, whose labels (for dictionaries) or index (for series) correspond to the columns of the DataFrame that 
you want to fill:
Examples:

    df.fillna ({'col_1': val_1, 'col_2': 'val_2'}) # Replace the NAs of column 'col_1' by val_1 and those of column 'col_2' by 'val_2'.

    df.fillna (df.mean ()) # Replace the NAs of each column by the average of the column (ok because the column names match)

    
    The method fillna has the parameter inplace=False by default. To store the new DataFrame with the replaced values, store it in a variable 
    (e.g. df = df.fillna(0)) or set inplace=True (e.g.  df.fillna(0, inplace=True)).
"""

## Replace missing values of 'Product_Name' in a logical way.
# Products.Product_Name.fillna('Product '+Products.Index.astype(str), inplace=True)

## Replace the missing value of the variable 'Category' by the most frequent value.
# Products.Category.fillna(Products.Category.mode()[0], inplace=True)

"""
For the 'Quantity' column of Sales, we notice that 7 lines are now np.nan. For this type of variable, it is very difficult to predict with the naked eye 
what to replace missing values. We can therefore use algorithms to do it automatically.

One of these missing value completion algorithms is called KnnImputer. This algorithm, known as 'K Nearest Neighbors', assumes that data with close values 
on columns other than the one where the data is missing will also have close values on the column where the data is missing.

To determine by which value to replace a NaN, it will therefore look at the values of the k nearest neighbors and take the average.
"""

## Import the function KNNImputer from sklearn.impute. Instantiate an imputer object of the KNNImputer class with the parameter n_neighbors = 4.
# from sklearn.impute import KNNImputer

#imputer = KNNImputer(n_neighbors = 4)

## Create a DataFrame val_num containing all the numeric variables of Sales.
#val_num = Sales.drop(["Order number", "Channel", "Order Date", "Delivery Date"], axis=1)

## Replace missing values of val_num with the k-nearest neighbors method. Categorical variables have been removed because this method only works if all the 
# columns are numeric.

"""
    Example of use: imputer.fit_transform(df)returns an array, where the missing values of df are replaced. 

    In this operation, the column names are lost but the out preserves the order of the columns and rows. You can use this fact to create, if needed, 
    a new pandas DataFrame using pd.DataFrame.
"""
    
#val_num =imputer.fit_transform(val_num)
#val_num = pd.DataFrame(val_num)

#val_num["Quantity"]=val_num[2]

# Display the values taken by the variable 'Quantity' in Sales and in val_num.
#print(Sales["Quantity"].unique())
#print(val_num["Quantity"].unique())

"""
Sometimes the values that are missing are crucial to understand / use the data, so it is not possible to replace them, and in many cases it is even 
recommended to remove the affected rows. When a column contains a large majority of missing values, it may be useful to delete it as well.
"""

## Delete, using dropna(), the lines for which the Customer Id is missing. Hint: use the parameter subset.
#Sales.dropna(subset = ["Customer Id"], axis = 0, inplace = True)

## Using the fillna method, replace missing values in the 'Channel' column with the following non-missing values. 
## (method) => forward: ffill, backwards: bfill
# Sales["Channel"].fillna(method='ffill', inplace = True)

###################################################################################################################################################################
######################################################################## Text processing ##########################################################################

"""
We are going to use a keyword approach to try to detect, for example, which accidents involve trucks or not. We will have to create a function that will 
allow us to detect if the word 'truck' is present in the accident description or not. To do this, we will proceed step by step.

Python handles strings like lists of characters. Thus, we can access an element of a String using square brackets and concatenate String with the + operator, 
as for lists.

    'abcde'[3] 
    >>>'d'

However, unlike lists, it is possible to test the inclusion of one String in another directly with the in operator
Execute the following cell.

    print("['b','c'] in ['a','b','c','d'] returns", ['b', 'c'] in ['a','b','c','d'])
    print("'bc' in 'abcd' returns", 'bc' in 'abcd')

        ['b','c'] in ['a','b','c','d'] returns False
        'bc' in 'abcd' returns True
"""

## Create a function word_detection() that takes as argument a list of strings and a sentence, and returns True if at least one of them is in the sentence and 
## False otherwise.

def word_detection(liste, phrase):
    for i in liste:
        if i in phrase:
            return True
    return False

"""
This function could allow us to detect when the word truck is in the description. However, this method only looks if a string is present or not in a String, 
but not that a word is contained in a sentence. For example:

    'truck' in 'I was struck by it'
    >>> True

By using this function, we risk overestimating the number of accidents caused by trucks.

One technique for detecting the presence of 'truck' and not 'struck' is to place spaces before and after 'truck' to make sure it is not contained in another 
larger word.
"""

## Create a word_detection2() function that takes a list of words and a sentence as arguments, and returns True if any of the words are contained in the sentence, 
## using the method shown above.

def word_detection2(liste, phrase):
    for word in liste:
        if " " + word + " " in phrase:
            return True
    return False

"""
However, a correctly written sentence starts with a capital letter and ends with a period (not with spaces). So if the word 'truck' is at the beginning or 
at the end of the sentence, it will not be detected by the previous function because it will not be surrounded by 2 spaces. The same thing happens if it is next 
to a comma, a semicolon or a colon.

To solve this problem, we will make a list of strings that should be checked to ensure the presence or absence of a word in a sentence. 
For example, if the word to be detected is 'word', the following strings should be detected:

    [' word ', ' word,', ' word:', ' word;', ' word.', 'Word ', 'Word,', 'Word:', 'Word;', 'Word.']
"""
    
## Using the .capitalize() method which adds a capital letter to the beginning of a String, create a possib function which takes as argument a word, 
## and returns the list of strings to be detected.

def possib(words):
   return [word.capitalize() for word in words]


## Using the possib() and word_detection() functions together, look for the following words in their associated sentences.
liste = 'be'
phrase = "Don't be afraid to go outside the box"

word_detection(liste = possib(word = 'be'), 
               phrase="Don't be afraid to go outside the box")

liste = 'be'
phrase = "You are the best"

word_detection(liste = possib(word = 'be'), 
               phrase="You are the best")


## Use the function possib() to count the number of lines that contain the word 'truck' or 'trucks'.

#count_rows = 0
#variation_of_word_truck = possib('truck') + possib('trucks')

#for line in accidents["Description"]:
#    for word in variation_of_word_truck:
#        if word in line:
#            count_rows += 1
#            break

#print(count_rows)


## Determine the proportion of accidents involving one or more trucks.

