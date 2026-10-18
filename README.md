--- Step 1: Data Load Ho Raha Hy ---
Shuru mein Rows: 8631, Columns: 17

--- Step 2: Data Ka Audit ---
Missing values har column mein:
  Invoice ID                    0
  Branch                        0
  City                          0
  Customer type                64
  Gender                        0
  Product line                  0
  Unit price                    0
  Quantity                      0
  Tax 5%                        0
  Total                         0
  Date                         17
  Time                          0
  Payment                       0
  cogs                          0
  gross margin percentage       0
  gross income                  0
  Rating                       88
dtype: int64

Exact duplicate rows ki tadad: 30
Duplicate Invoice IDs ki tadad: 55
Gender columns ki unique values: <StringArray>
['Female', 'Male', ' Female', 'MALE ', 'male', 'female']
Length: 6, dtype: str
Payment columns ki unique values: <StringArray>
['Ewallet', 'Credit card', 'Cash', 'cash', ' Credit card', 'ewallet ',
 'EWALLET']
Length: 7, dtype: str

--- Step 3: Exact Duplicate Rows Ko Delete Karna ---
Rows bache: 8601

--- Step 4: Duplicate Invoice IDs Theek Karna ---
Rows bache: 8576

--- Step 5: Text Columns Ko Standardise Karna ---
Text cleaning mukammal!

--- Step 6: Negative Quantities Ko Positive Karna ---
Quantities theek ho gayin!

--- Step 7: Mixed Dates Ko Format Karna ---
Dates parse ho gayin!

--- Step 8: Total Calculations Check Karna ---
Totals verify aur correct ho gaye!

--- Step 9: Bache Hue Missing Data Ko Handle Karna ---
Final Rows bache: 8514

--- Step 10: Complete Audit Trail Summary ---
Shuru (Initial) -> Rows Mojood Hain: 8576
After Step 9 (Clean Missing) -> Rows Mojood Hain: 8514
--------------------------------------------------

--- Brief Sawal 1: Adding Time Columns ---
Time columns successfully add ho gaye hain!

--- Brief Sawal 2: Bucket the Trading Day ---
Transactions per hour down the shifts:
  * Morning 10-13: 717.33 transactions/hour
  * Afternoon 13-17: 738.25 transactions/hour
  * Evening 17-21: 852.25 transactions/hour

--- Brief Sawal 3 & 4: Compare Against Target & Summary ---
    Branch Quarter      Revenue     Variance  % of Target    Hit
0        A  2023Q1  102248.7795    2248.7795   102.248779   True
1        A  2023Q2   90064.1595   -9935.8405    90.064160  False
2        A  2023Q3   90878.3400   -9121.6600    90.878340  False
3        A  2023Q4  129821.3280   29821.3280   129.821328   True
4        A  2024Q1  112450.6425   12450.6425   112.450643   True
5        A  2024Q2   98243.2815   -1756.7185    98.243281  False
6        A  2024Q3   89175.6705  -10824.3295    89.175670  False
7        A  2024Q4  117506.8125   17506.8125   117.506812   True
8        B  2023Q1   96366.0075   -3633.9925    96.366008  False
9        B  2023Q2   91993.3245   -8006.6755    91.993324  False
10       B  2023Q3   84757.8900  -15242.1100    84.757890  False
11       B  2023Q4  109628.6940    9628.6940   109.628694   True
12       B  2024Q1   83503.1505  -16496.8495    83.503151  False
13       B  2024Q2   79174.1370  -20825.8630    79.174137  False
14       B  2024Q3   83812.8375  -16187.1625    83.812837  False
15       B  2024Q4  116106.4800   16106.4800   116.106480   True
16       C  2023Q1  100406.1030     406.1030   100.406103   True
17       C  2023Q2   82013.9775  -17986.0225    82.013977  False
18       C  2023Q3   88932.0285  -11067.9715    88.932029   True
19       C  2023Q4  125174.3430   25174.3430   125.174343   True
20       C  2024Q1  104136.5535    4136.5535   104.136553   True
21       C  2024Q2   92297.5725   -7702.4275    92.297572  False
22       C  2024Q3   93115.8375   -6884.1625    93.115837  False
23       C  2024Q4  140298.6900   40298.6900   140.298690   True

 Cleaned data 'cleaned_supermarket_sales.csv' ke naam se save ho gaya hy!
