# MYSQL Notes

To get started you need mysql and mysql workbench
- Workbench is a gui that allows you to view you database
- `Install mysql on Mac` https://dev.mysql.com/doc/refman/8.0/en/osx-installation-pkg.html
- `Cheat Sheet` https://www.mysqltutorial.org/mysql-cheat-sheet.aspx

Once installed add mysql to your path
```
export PATH=$PATH:/usr/local/mysql/bin
```

To log into mysql from bash
```
mysql -u root -p
```

Backing up your database
```
mysql -u root -p devicesdb > devicesdb_database_backup.sql
```

You can change your mysql password once logged in
```
SET PASSWORD FOR 'root'@'localhost' = PASSWORD('password')
```

## Viewing Data in MYSQL
view tables
```
show tables;
```

view table scheme
```
describe routers;
```

view 10 entries in the database
```
select * from routers limit 10;
```

view total table count;
```
select count(*) from routers;
```

view total table count and temporarily rename column
```
select count(*) as Total from routers;
```

view two different columns and search criteria
```
select count(*) as Total, location as Location from routers GROUP BY location;
```

view two different columns, search criteria and sort
```
select count(*) as Total, location as Location from routers GROUP BY location ORDER BY Total;
```

view two different columns, search, criteria, sort and limit
```
select count(*) as Total, location as Location from routers GROUP BY location ORDER BY Total desc limit 10;
```

view two different columns, search, criteria, sort and limit
```
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
```
pip install mysql-connector
```