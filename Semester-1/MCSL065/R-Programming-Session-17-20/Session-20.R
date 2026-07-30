# Read data for Q-62
library(ggplot2)
setwd("~/IGNOU-MSCDSA/Semester-I/programming-assignments/ignou-mscdsa/Semester-1/MCSL065/R-Programming-Session-17-20")
employee_data <- read.csv(file = "employees.csv")

# Q-62
employee_data$Department[is.na(employee_data$Department)] <- "Unassigned"
ggplot(employee_data, aes(x=Department, fill = Department)) + geom_bar() + labs(title="Employee Count by Department", x="Department", y="Number of Employees")

# Q-63
product_data <- read.csv(file = "PRODUCT.csv")
ggplot(product_data, aes(x=Month, y=Total_Sales_USD, colour = Category, group = Category)) + geom_line() + labs(title = "Monthly sales by Category", x="Month", y="Total Sales")

# Q-64
ggplot(product_data, aes(x=Units_Sold, y=Net_Profit_USD)) + geom_point(color = "blue") + geom_smooth(method = "lm") + labs(title = "Scatter Plot - Sales vs Profit", x="Total Sales", y="Profit in USD")

# Q-65
# 1. Generate dataset
set.seed(101)
sim_data <- data.frame(Value = rnorm(1000, mean = 50, sd = 10))

# 2. Build plot layer by layer using '+'
ggplot(sim_data, aes(x = Value)) +
  geom_histogram(aes(y = after_stat(density)), bins = 30, fill = "gray80", color = "gray40", alpha = 0.7) +
  stat_function(
    fun = dnorm, 
    args = list(mean = mean(sim_data$Value), sd = sd(sim_data$Value)),
    color = "blue", 
    linewidth = 1.2
  ) +
  labs(
    title = "Histogram with Normal Distribution Curve",
    x = "Value",
    y = "Density"
  ) +
  theme_classic()

