# RetailEdge ETL Pipeline

A modular Python-based ETL pipeline built for RetailEdge Inc. to automate
the processing of customer, order, and returns data.

## Project Structure

- extract/ — Raw CSV ingestion and schema checking
- transform/ — Data cleaning, enrichment and filtering
- load/ — Saves processed data to data/processed/
- config/ — Environment variables and constants
- utils/ — Shared helper functions
- tests/ — Unit tests using pytest
- .github/ — GitHub Actions CI/CD workflow
- main.py — Pipeline runner

## Setup Instructions

1. Clone the repository
2. Create and activate virtual environment: python -m venv venv && source venv/bin/activate
3. Install dependencies: pip install -r requirements.txt
4. Add raw data files to data/raw/
5. Run the pipeline: python main.py

## Running Tests

pytest tests/ -v

## CI/CD

GitHub Actions automatically runs all tests on every push to dev and main.

## Team

Built by: Lola A
