# Define Data
data <- data.frame(
  Customer_ID = c(1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010),
  Age = c(25, 34, NA, 45, 29, NA, 52, 38, NA, 31),
  Gender = c('Male', 'Female', 'Female', NA, 'Male', 'Female', NA, 'Male', 'Female', 'Male'),
  Income_USD = c(55000, 62000, 48000, 71000, NA, 53000, 89000, NA, 61000, 58000),
  City = c('New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Chicago', NA, 'Miami', 'New York', 'Houston'),
  Purchase_Amount = c(120.5, 250.0, 85.0, NA, 310.0, NA, 450.0, 95.0, 210.0, 175.0)
)

# Q-55
print("Summary of the data:")
print(summary(data))

print("Number of rows:")
print(nrow(data))

print("Number of columns:")
print(ncol(data))

print("Missing data:")
print(colSums(is.na(data)))

# Q-56
library(dplyr)
print("Filter records where Age>30:")
dplyr::filter(data, Age>30)

print("Selecting only City column:")
select(data, City)

print("Adding monthly Income in USD:")
select(data, Income_USD) |> mutate(Monthly_Income_USD = Income_USD/12)

# Q-57
print("Data before removing NA values:")
print(data)
print("Data after removing NA values:")
print(na.omit(data))

print("Converting Numeric values to Numeric data type:")
data$Age <- as.numeric(data$Age)
data$Income_USD <- as.numeric(data$Income_USD)
print(data)

print("Converting Gender and City to Factor:")
data$Gender <- as.factor(data$Gender)
data$City <- as.factor(data$City)
print(data)
