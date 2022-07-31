# pkpass2csv

1. copy your .pkpass files into the 'pkpass' folder.
2. run secondTry.py
3. pass.json files will be in the 'passes' folder
4. keys.csv in 'keys' folder is able to consistently decode pkpass files from these airlines:
--American Airlines, Delta, Frontier, JSX, SW, United, Alaska
--pulling this info: airline name, flight number, departure location and time, arrival location and time, passenger name, class, operated by, confirmation number, and ticket number. (some fields available to some airlines, not all)
5. decoded pkpass files are pushed to a file called outputFile.csv


////////////
Working on adding:
-multiselect/open pkpass files
-run each through unzipper()
-run each through keyd()
-create new function saveAs()
-run each through saveAs()

-error handling;
--if airline is not on keys.csv, error message and send copy of pass.csv to info@oziburt.com



