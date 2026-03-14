# Data Integration and Data Qualiity

This project contains datasets and some sample adat peocessing pipelines for the
Data Integration and Data Quality session in the Barçca Innovation Hub Post Graduate
in Sports Analytics

Author: Albert Such

## Setting Up

### 1. Create a virtual environment

```bash
python3 -m venv .venv
```

### 2. Activate the virtual environment

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Project Structure

### Datasets

Contains several football (soccer) relateddatasets extracted from [Kaggle](https://kaggle.com) 

- *English Premier League in-game match data*

  Detailed information about English premier League matches, seasons 14/15, 15/16, 16/17 and 17/18 in JSON format. Extracted from https://www.kaggle.com/datasets/shubhmamp/english-premier-league-match-data

- *FIFA Player Stats Dataset Complete Attributes*

  Extracted from https://www.kaggle.com/datasets/utsab5740/fifa-messy-raw-data

- *Football Data from Transfermarkt*

  Data scrapped from [Transfermarkt](https://www.transfermarkt.es/) containing information
  about clubs, games, players and transfers. Extracted from https://www.kaggle.com/datasets/davidcariboo/player-scores/versions/632, also available in https://github.com/dcaribou/transfermarkt-datasets. This dataset gets updated with new information periodically

- *Football Players Data*
  
  Football players data. Contains information about players in general, no specific to a season. Extracted from https://www.kaggle.com/datasets/maso0dahmed/football-players-data. 


- *Football Players Datasets 2015 - 2024*
  
  Football players data. Extracted from https://www.kaggle.com/datasets/abdulmalik1518/football-players-datasets-2015-2024

### Integration
Contains python notebooks for the Data Integration example

- [Player name matching](Integration/01player_name_matching.ipynb)

- [Matching season with valuation dates](Integration/02season_valuation_date_matching.ipynb)

