# Databricks notebook source
# MAGIC %sql
# MAGIC USE CATALOG main;
# MAGIC USE SCHEMA default;
# MAGIC
# MAGIC CREATE OR REPLACE FUNCTION table_exists(catalog_name STRING,
# MAGIC                                         db_name      STRING,
# MAGIC                                         table_name   STRING)
# MAGIC   RETURNS BOOLEAN
# MAGIC   RETURN if(
# MAGIC     (SELECT count(*) FROM system.information_schema.tables
# MAGIC      WHERE table_catalog = table_exists.catalog_name
# MAGIC        AND table_schema  = table_exists.db_name
# MAGIC        AND table_name    = table_exists.table_name) > 0,
# MAGIC     true,
# MAGIC     false
# MAGIC   );
# MAGIC
# MAGIC CREATE OR REPLACE FUNCTION column_exists(catalog_name STRING,
# MAGIC                                          db_name      STRING,
# MAGIC                                          table_name   STRING,
# MAGIC                                          column_name  STRING)
# MAGIC   RETURNS BOOLEAN
# MAGIC   RETURN if(
# MAGIC     (SELECT count(*) FROM system.information_schema.columns
# MAGIC      WHERE table_catalog = column_exists.catalog_name
# MAGIC        AND table_schema  = column_exists.db_name
# MAGIC        AND table_name    = column_exists.table_name
# MAGIC        AND column_name   = column_exists.column_name) > 0,
# MAGIC     true,
# MAGIC     false
# MAGIC   );
# MAGIC
# MAGIC CREATE OR REPLACE FUNCTION num_rows_for_clarity_in_diamonds(clarity_value STRING)
# MAGIC   RETURNS BIGINT
# MAGIC   RETURN SELECT count(*)
# MAGIC          FROM main.default.diamonds
# MAGIC          WHERE clarity = clarity_value

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT CASE
# MAGIC -- If the table exists in the specified catalog and schema...
# MAGIC WHEN
# MAGIC   table_exists("main", "default", "diamonds")
# MAGIC THEN
# MAGIC   -- And the specified column exists in that table...
# MAGIC   (SELECT CASE
# MAGIC    WHEN
# MAGIC      column_exists("main", "default", "diamonds", "clarity")
# MAGIC    THEN
# MAGIC      -- Then report the number of rows for the specified value in that column.
# MAGIC      printf("There are %d rows in table 'main.default.diamonds' where 'clarity' equals 'VVS2'.",
# MAGIC             num_rows_for_clarity_in_diamonds("VVS2"))
# MAGIC    ELSE
# MAGIC      printf("Column 'clarity' does not exist in table 'main.default.diamonds'.")
# MAGIC    END)
# MAGIC ELSE
# MAGIC   printf("Table 'main.default.diamonds' does not exist.")
# MAGIC END
