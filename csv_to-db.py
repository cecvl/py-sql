import sqlite3
import pandas as pd

# Define the function to move csv data to SQLite
def csv_to_sqlite(csv_file, db_file):
    # Connect to the SQLite database (create it if it doesn't exist)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()


    # Commit the changes
    # conn.commit()

    # Load the CSV file using pandas
    df = pd.read_csv(csv_file)

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

        # Get the word_id of the inserted word
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
            conjugation_list = conjugation.split('|')  # conjugations aren't separated by '|'?
            for conj in conjugation_list:
                cursor.execute('''
                    INSERT INTO conjugations (word_id, conjugation) VALUES (?, ?)
                ''', (word_id, conj.strip()))

        # Commit after each row is processed
        conn.commit()

    # Close the connection
    conn.close()

    print(f"Data from {csv_file} has been successfully inserted into {db_file}.")

# Example usage
csv_file_path = 'swahili.csv'
db_file_path = 'test.db'

csv_to_sqlite(csv_file_path, db_file_path)
