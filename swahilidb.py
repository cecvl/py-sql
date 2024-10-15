from cs50 import SQL
import pandas as pd;
db = SQL("sqlite:///test.db")

db.execute("CREATE TABLE words (id INT AUTO_INCREMENT PRIMARY KEY,word VARCHAR(255) NOT NULL UNIQUE, meaning TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

db.execute("CREATE TABLE synonyms (id INT AUTO_INCREMENT PRIMARY KEY,word_id INT, synonym VARCHAR(255) , FOREIGN KEY (word_id) REFERENCES words(id) ON DELETE CASCADE)")

db.execute("CREATE TABLE conjugations (id INT AUTO_INCREMENT PRIMARY KEY,word_id INT, conjugation VARCHAR(255) , FOREIGN KEY (word_id) REFERENCES words(id) ON DELETE CASCADE)")

