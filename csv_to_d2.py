import sqlite3
import pandas as pd

# Define the function to move a specific number of rows from CSV data to SQLite
def csv_to_sqlite(csv_file, db_file, row_limit=None):
    # Connect to the SQLite database (create it if it doesn't exist)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create the tables if they don't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL UNIQUE,
            meaning TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS synonyms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word_id INTEGER,
            synonym TEXT,
            FOREIGN KEY (word_id) REFERENCES words(id) ON DELETE CASCADE
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conjugations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word_id INTEGER,
            conjugation TEXT,
            FOREIGN KEY (word_id) REFERENCES words(id) ON DELETE CASCADE
        );
    ''')

    # Commit the changes
    conn.commit()

    # Load the CSV file using pandas
    df = pd.read_csv(csv_file)

    # Limit the number of rows to be processed (if specified)
    if row_limit:
        df = df.head(row_limit)

    # Iterate through each row of the CSV and insert data into the database
    for index, row in df.iterrows():
        word = row['Word']
        meaning = row['Meaning']
        synonyms = row['Synonyms'] if pd.notnull(row['Synonyms']) else None
        conjugation = row['Conjugation'] if pd.notnull(row['Conjugation']) else None

        # Insert the word into the `words` table, using INSERT OR IGNORE to avoid duplicates
        cursor.execute('''
            INSERT OR IGNORE INTO words (word, meaning) VALUES (?, ?)
        ''', (word, meaning))

        # Fetch the word_id of the last inserted word
        word_id = cursor.lastrowid

        # If word already exists, retrieve its ID
        if word_id == 0:
            cursor.execute('''
                SELECT id FROM words WHERE word = ?
            ''', (word,))
            word_id = cursor.fetchone()[0]

        # Insert synonyms if available
        if synonyms:
            synonym_list = synonyms.split('|')  # Assuming synonyms are separated by '|'
            for synonym in synonym_list:
                cursor.execute('''
                    INSERT INTO synonyms (word_id, synonym) VALUES (?, ?)
                ''', (word_id, synonym.strip()))

        # Insert conjugations if available
        if conjugation:
            conjugation_list = conjugation.split('|')  # Assuming conjugations are separated by '|'
            for conj in conjugation_list:
                cursor.execute('''
                    INSERT INTO conjugations (word_id, conjugation) VALUES (?, ?)
                ''', (word_id, conj.strip()))

        # Commit after each row is processed
        conn.commit()

    # Close the connection
    conn.close()

    print(f"Data from {csv_file} has been successfully inserted into {db_file} (processed {len(df)} rows).")

# Example usage
csv_file_path = 'swahili.csv'
db_file_path = 'test4.db'

# Specify the row limit
row_limit = 16643  # Yes, I copied that amount of rows, what do you think we're here for?

csv_to_sqlite(csv_file_path, db_file_path, row_limit)
