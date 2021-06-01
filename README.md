# Python CSV Playground

## Purpose

Attempt to read in large data sets from csv files, perform basic analysis and then print results to both the terminal and to a text file.

## [PyBank](PyBank)

[Input](PyBank/Resources/budget_data.csv): a 2 column CSV file with headers (Date, Profit/Losses) describing profits and losses of some unknown entity

[Output](PyBank/Analysis/budget_report.txt): A financial analysis including:

* The total number of months included in the dataset

* The net total amount of "Profit/Losses" over the entire period

* The changes in "Profit/Losses" over the entire period, as well as the average of those changes

* The greatest increase in profits (date and amount) over the entire period

* The greatest decrease in profits (date and amount) over the entire period

## [PyPoll](PyPoll)

[Input](PyPoll/Resources/election_data.csv): A 3 column CSV file with headers (Voter ID, County, Candidate) describing votes in an election

[Output](PyPoll/Analysis/election_results.txt): A summary of the election including:

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote.

### Bonus

* Also break down the votes by county

* Guarantee no voter fraud by confirming voter ids as they are processed
