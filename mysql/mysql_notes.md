# MYSQL Notes

To get started you need mysql and mysql workbench
- Workbench is a gui that allows you to view you database
- [Install mysql on Mac](https://dev.mysql.com/doc/refman/8.0/en/osx-installation-pkg.html)
- [Cheat Sheet](https://www.mysqltutorial.org/mysql-cheat-sheet.aspx)

Once installed add mysql to your path
```bash
export PATH=$PATH:/usr/local/mysql/bin
```

To log into mysql from bash
```bash
mysql -u root -p
```

Backing up your database
```bash
mysql -u root -p devicesdb > devicesdb_database_backup.sql
```

You can change your mysql password once logged in
```sql
SET PASSWORD FOR 'root'@'localhost' = PASSWORD('password')
```

## Create, Modify and Delete 

Create a database if it does not exist

```sql
CREATE DATABASE [IF NOT EXISTS] labeveryday_database;
```

Change to the database

```sql
USE labeveryday_database
```

Delete the database if it exists

```sql
DROP DATABASE [IF EXISTS] labeveryday_database;
```

Create a table if it does not exist

```sql
CREATE TABLE [IF NOT EXISTS] table_name(
  column_list
);
```

Add a column to a table

```sql
ALTER TABLE routers ADD [IF NOT EXISTS] serial_number VARCHAR(255) AFTER hostname;
```

Another example of adding a column

```sql
IF NOT EXISTS( SELECT NULL
            FROM INFORMATION_SCHEMA.COLUMNS
           WHERE table_name = 'tablename'
             AND table_schema = 'db_name'
             AND column_name = 'columnname')  THEN

  ALTER TABLE `TableName` ADD `ColumnName` int(1) NOT NULL default '0';

END IF;
```

## Viewing Data in MYSQL

Show SQL version

```sql
select version()
```

view mysql databases
```sql
show databases;
```

view tables

```sql
SHOW tables;
```

view table scheme

```sql
DESCRIBE routers;
```

view 10 entries in the database
```sql
select * from routers limit 10;
```

view total table count;
```sql
select count(*) from routers;
```

view total table count and temporarily rename column
```sql
select count(*) as Total from routers;
```

view two different columns and search criteria
```sql
select count(*) as Total, location as Location from routers GROUP BY location;
```

view two different columns, search criteria and sort
```sql
select count(*) as Total, location as Location from routers GROUP BY location ORDER BY Total;
```

view two different columns, search, criteria, sort and limit
```sql
select count(*) as Total, location as Location from routers GROUP BY location ORDER BY Total desc limit 10;
```

view two different columns, search, criteria, sort and limit
```sql
select count(*) as Total, location as Location from routers GROUP BY location HAVING Total >= 50 Order by Total Desc;
```

### Data Types in mysql

| Data type           | Description                                                           |
| -------------       |:-------------:                                                        |
| CHAR(size)          | A fixed-length string between 1 and 255 characters in length.         |
| VARCHAR(size)       | A variable-length string between 1 and 255 characters in length.      |
| INT                 | A normal-sized integer that can be signed or unsigned.                |
| FLOAT               | A floating-point number that cannot be unsigned.                      |
| DECIMAL             | An unpacked floating-point number that cannot be unsigned.            |
| DATE                | A date in YYYY-MM-DD format.                                          |
| TIME                | Stores the time in a HH:MM:SS format.                                 |
| ENUM                | Stores a list                                                         |
| BOOL                | Zero is considered as false, nonzero values are considered as true.   |
| SET(val1, val2, ..) | A string object that can have 0 or more values, chosen from a list.   |
| TEXT(size)          | Holds a string with a maximum length of 65,535 bytes.                 |
| BLOB                | For BLOBs (Binary Large OBjects). Holds up to 65,535 bytes of data    |
| LONGBLOB            | For BLOBs (Binary Large OBjects). Holds up to 4,294,967,295 bytes     |

___

## Python and Mysql

install mysql-connector
```bash
pip install mysql-connector
```