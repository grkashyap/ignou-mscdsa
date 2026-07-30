setwd("~/IGNOU-MSCDSA/Semester-I/programming-assignments/ignou-mscdsa/Semester-1/MCSL065/R-Programming-Session-17-20")

# Q-52
csv_file_path <- "./PRODUCT.csv"
csv_file_data <- read.csv(file = csv_file_path)

cat("Data from csv file:\n")
str(csv_file_data)

cat("\nSummary of the data:\n")
print(summary(csv_file_data))

# Q-53
xls_file_path <- "company_data.xlsx"
xls_file_data <- readxl::read_excel(path = xls_file_path, sheet = "Employees")
print("Data from xls file:\n")
print(xls_file_data)

# Q-54
library(jsonlite)
json_file_path <- "PRODUCT.json"
json_file_data <- fromJSON(json_file_path)
print("Data from JSON file: \n")
print(json_file_data)
