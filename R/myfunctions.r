library(SparkR)

# Does the specified table exist in the specified database?
table_exists <- function(table_name, db_name) {
  tableExists(paste(db_name, ".", table_name, sep = ""))
}

# Does the specified column exist in the given DataFrame?
column_exists <- function(dataframe, column_name) {
  column_name %in% colnames(dataframe)
}

# How many rows are there for the specified value in the specified column
# in the given DataFrame?
num_rows_in_column_for_value <- function(dataframe, column_name, column_value) {
  df = filter(dataframe, dataframe[[column_name]] == column_value)

  count(df)
}