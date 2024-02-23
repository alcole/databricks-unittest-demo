# Databricks notebook source
# MAGIC %scala
# MAGIC import org.apache.spark.sql.DataFrame
# MAGIC import org.apache.spark.sql.functions.col
# MAGIC
# MAGIC // Does the specified table exist in the specified database?
# MAGIC def tableExists(tableName: String, dbName: String) : Boolean = {
# MAGIC   return spark.catalog.tableExists(dbName + "." + tableName)
# MAGIC }
# MAGIC
# MAGIC // Does the specified column exist in the given DataFrame?
# MAGIC def columnExists(dataFrame: DataFrame, columnName: String) : Boolean = {
# MAGIC   val nameOfColumn = null
# MAGIC
# MAGIC   for(nameOfColumn <- dataFrame.columns) {
# MAGIC     if (nameOfColumn == columnName) {
# MAGIC       return true
# MAGIC     }
# MAGIC   }
# MAGIC
# MAGIC   return false
# MAGIC }
# MAGIC
# MAGIC // How many rows are there for the specified value in the specified column
# MAGIC // in the given DataFrame?
# MAGIC def numRowsInColumnForValue(dataFrame: DataFrame, columnName: String, columnValue: String) : Long = {
# MAGIC   val df = dataFrame.filter(col(columnName) === columnValue)
# MAGIC
# MAGIC   return df.count()
# MAGIC }
