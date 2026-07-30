# Data for Q58 and Q59
sales_data <- data.frame(
  Product_ID   = c(101, 102, 103, 104, 105, 106, 107, 108, 109, 110),
  Category     = c("Electronics", "Clothing", "Electronics", "Furniture", 
                   "Clothing", "Electronics", "Furniture", "Furniture", 
                   "Clothing", "Electronics"),
  Region       = c("North", "South", "North", "East", "West", 
                   "South", "North", "West", "East", "South"),
  Sales        = c(1200, 450, 800, 1500, 300, 2100, 950, 1100, 600, 1750),
  Profit       = c(300, 90, 200, 400, 50, 500, 180, 220, 120, 450),
  Customer_ID  = c("C101", "C102", "C103", "C104", "C105", 
                   "C106", "C107", "C108", "C109", "C110")
)

# Q-58
print("Group sales by product Category: ")
total_sales = sales_data |> group_by(Category) |> summarise(sum(Sales))
print(total_sales)

# Q-59
print("Sort data using multiple columns: ")
arrange(sales_data, desc(Profit), Region)

print("Added ranking: ")
mutate(sales_data, Ranked_column = dense_rank(desc(Profit)))

# Data for Q60
customer_data <- data.frame(
  Customer_ID   = c("C101", "C102", "C103", "C104", "C105", "C999", "C888"),
  Customer_Name = c("Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"),
  Segment       = c("Consumer", "Corporate", "Consumer", "Home Office", 
                    "Consumer", "Corporate", "Home Office")
)

# Q-60
print("Merging sales and customer data using left join: ")
left_join(x=customer_data, y=sales_data, by=join_by(Customer_ID))

print("Merging sales and customer data using inner join: ")
inner_join(x=customer_data, y=sales_data, by=join_by(Customer_ID))

# Q-61
setwd("~/IGNOU-MSCDSA/Semester-I/programming-assignments/ignou-mscdsa/Semester-1/MCSL065/R-Programming-Session-17-20")
#employee_records <- data.frame(
#  Name         = c("Ankit", "Priya", "Rahul", "Sneha", "Vikram", "Neha", "Amit"),
#  Department   = c("HR", "IT", "Finance", "IT", "Finance", NA, "HR"),
#  Salary       = c(50000, 75000, 62000, NA, 68000, 55000, -45000), # Note: NA and negative salary
#  Joining_Year = c(2018, 2020, 2015, 2021, 2019, 2022, 2017)
#)

# Save to a CSV file in your current working directory
#write.csv(employee_records, "employees.csv", row.names = FALSE)

# Read CSV
employee_data <- read.csv(file = "employees.csv")

# explore structure and basic statistics
str(employee_data)
summary(employee_data)
head(employee_data,n = 3)

# Find missing or inconsitent data
print("Missing data: ")
colSums(is.na(employee_data))

print("Invalid data: ")
filter(employee_data, Salary < 0 | is.na(Salary))