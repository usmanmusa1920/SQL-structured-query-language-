"""
  Database table most often contains one or more tables. Each tle is identify by a name (e.g students or staffs). Tabless contains records (row) with data.

  
"""
import sqlite3
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute(
  "CREATE TABLE `logs` ("
    " `id` INTEGER(11) NOT NULL AUTO_INCREMENT,"
    " `text` varchar(250) NOT NULL,"
    " `user` varchar(250) NOT NULL,"
    " `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    " PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)