# Databricks notebook source
# MAGIC %r
# MAGIC library(SparkR)
# MAGIC source("myfunctions.r")
# MAGIC
# MAGIC table_name   <- "diamonds"
# MAGIC db_name      <- "default"
# MAGIC column_name  <- "clarity"
# MAGIC column_value <- "VVS2"
# MAGIC
# MAGIC # If the table exists in the specified database...
# MAGIC if (table_exists(table_name, db_name)) {
# MAGIC
# MAGIC   df = sql(paste("SELECT * FROM ", db_name, ".", table_name, sep = ""))
# MAGIC
# MAGIC   # And the specified column exists in that table...
# MAGIC   if (column_exists(df, column_name)) {
# MAGIC     # Then report the number of rows for the specified value in that column.
# MAGIC     num_rows = num_rows_in_column_for_value(df, column_name, column_value)
# MAGIC
# MAGIC     print(paste("There are ", num_rows, " rows in table '", table_name, "' where '", column_name, "' equals '", column_value, "'.", sep = "")) 
# MAGIC   } else {
# MAGIC     print(paste("Column '", column_name, "' does not exist in table '", table_name, "' in schema (database) '", db_name, "'.", sep = ""))
# MAGIC   }
# MAGIC
# MAGIC } else {
# MAGIC   print(paste("Table '", table_name, "' does not exist in schema (database) '", db_name, "'.", sep = ""))
# MAGIC }
