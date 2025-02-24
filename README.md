# Mini ETL Pipeline

## Project Description
This Mini ETL Project (Extract, Transform, Load) demonstrates how to set up a very simple data pipeline using Python and Docker. It loads a CSV file, processes the data, and stores it in an SQLite database.

## Technologies
- Python 3.9
- Pandas
- SQLite3
- Docker

## Quick Start
### 1. Clone the Repository
```sh
git clone https://github.com/JayQuentin/mini-etl-pipeline.git
cd mini-etl-pipeline
```

### 2. Build and Run the Docker Container
```sh
docker build -t etl-pipeline .
docker run --rm -v $(pwd)/data:/app/data etl-pipeline
```

### 3. Check the SQLite Database
After processing, you can find the SQLite database in `data/database.db`. To inspect the data:
```sh
sqlite3 data/database.db "SELECT * FROM your_table_name LIMIT 5;"
```

## Directory Structure
```
mini-etl-pipeline/
├── data/
│   ├── titanic_test.csv
│   └── database.db
├── app/
│   └── main.py
├── requirements.txt
├── Dockerfile
└── .gitignore
```

## Additional Information
If you have any questions or suggestions for improvements, feel free to create an issue or submit a pull request.

