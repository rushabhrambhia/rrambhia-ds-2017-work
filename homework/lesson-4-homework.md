# Lesson 4 Homework - Chipotle.tsv 

**Question 1:**
Look at the head and the tail of chipotle.tsv in the data subdirectory of this repo. Think for a minute about how the data is structured. What do you think each column means? What do you think each row means? Tell me! (If you're unsure, look at more of the file contents.)

**Solution**

_I used ```head``` and ```tail``` commands to preview the file. Below are the commands and their respective outputs._

_Each column represents a information regarding an order_
_Each row represents a different or unique item being ordered along with its quantity, ingredient choices and price_

|Column Name|Description|
|---|---|
order_id|Id of an order
quantity|Quantity of item being ordered
item name|Name of the item
choice_description|Choices made by customer for that item
item_price|Price of that item

Head command:```head chipotle.tsv ```

Output
```
order_id	quantity	item_name	choice_description	item_price
1	1	Chips and Fresh Tomato Salsa	NULL	$2.39 
1	1	Izze	[Clementine]	$3.39 
1	1	Nantucket Nectar	[Apple]	$3.39 
1	1	Chips and Tomatillo-Green Chili Salsa	NULL	$2.39 
2	2	Chicken Bowl	[Tomatillo-Red Chili Salsa (Hot), [Black Beans, Rice, Cheese, Sour Cream]]	$16.98 
3	1	Chicken Bowl	[Fresh Tomato Salsa (Mild), [Rice, Cheese, Sour Cream, Guacamole, Lettuce]]	$10.98 
3	1	Side of Chips	NULL	$1.69 
4	1	Steak Burrito	[Tomatillo Red Chili Salsa, [Fajita Vegetables, Black Beans, Pinto Beans, Cheese, Sour Cream, Guacamole, Lettuce]]	$11.75 
4	1	Steak Soft Tacos	[Tomatillo Green Chili Salsa, [Pinto Beans, Cheese, Sour Cream, Lettuce]]	$9.25 
```

Tail command:```tail chipotle.tsv ```

Output

```
1831	1	Carnitas Bowl	[Fresh Tomato Salsa, [Fajita Vegetables, Rice, Black Beans, Cheese, Sour Cream, Lettuce]]	$9.25 
1831	1	Chips	NULL	$2.15 
1831	1	Bottled Water	NULL	$1.50 
1832	1	Chicken Soft Tacos	[Fresh Tomato Salsa, [Rice, Cheese, Sour Cream]]	$8.75 
1832	1	Chips and Guacamole	NULL	$4.45 
1833	1	Steak Burrito	[Fresh Tomato Salsa, [Rice, Black Beans, Sour Cream, Cheese, Lettuce, Guacamole]]	$11.75 
1833	1	Steak Burrito	[Fresh Tomato Salsa, [Rice, Sour Cream, Cheese, Lettuce, Guacamole]]	$11.75 
1834	1	Chicken Salad Bowl	[Fresh Tomato Salsa, [Fajita Vegetables, Pinto Beans, Guacamole, Lettuce]]	$11.25 
1834	1	Chicken Salad Bowl	[Fresh Tomato Salsa, [Fajita Vegetables, Lettuce]]	$8.75 
1834	1	Chicken Salad Bowl	[Fresh Tomato Salsa, [Fajita Vegetables, Pinto Beans, Lettuce]]	$8.75 
```
---------

**Question 2:**
How many orders do there appear to be?

**Solution**

1834

---------

**Question 3:**
How many lines are in this file?

**Solution**

4623 lines. I used the word count command as follows

```
wc -l chipotle.tsv
```

Output
```
4623 chipotle.tsv
```

---------

**Question 4:**
Which burrito is more popular, steak or chicken?

**Solution**
Chicken Burrito is more popular. I used combination of text processing commands as follows:

Command
```
cut -f3 chipotle.tsv | sort | grep "Burrito" | uniq -c | sort
```

Output

```
      6 Burrito
     59 Carnitas Burrito
     91 Barbacoa Burrito
     95 Veggie Burrito
    368 Steak Burrito
    553 Chicken Burrito
```

---------

**Question 5:**
Do chicken burritos more often have black beans or pinto beans?

**Solution**
Chicken burritos have **black beans** more often than pinto beans. I used cut and grep commands to count lines with patterns that matched "Chicken Burrito" and then looked for lines that matched "Black Beans" and "Pinto Beans" with the below results:

Command for Pinto Beans

```
cut -f3,4 chipotle.tsv | grep "Chicken Burrito" | grep "Pinto Beans" | wc -l 
105
```

Command for Black Beans

```
cut -f3,4 chipotle.tsv | grep "Chicken Burrito" | grep "Black Beans" | wc -l 
282
```

---------

**Question 6:**
Make a list of all of the CSV or TSV files in the [our class repo] (https://github.com/ga-students/DS-SEA-3). repo (using a single command).

**Solution**

Command with Output

```
find ./DS-SEA-06/ -name *.?sv
./DS-SEA-06/data/airlines.csv
./DS-SEA-06/data/Airline_on_time_west_coast.csv
./DS-SEA-06/data/bank-additional.csv
./DS-SEA-06/data/bikeshare.csv
./DS-SEA-06/data/chipotle.tsv
./DS-SEA-06/data/citibike_feb2014.csv
./DS-SEA-06/data/drinks.csv
./DS-SEA-06/data/drones.csv
./DS-SEA-06/data/hitters.csv
./DS-SEA-06/data/icecream.csv
./DS-SEA-06/data/imdb_1000.csv
./DS-SEA-06/data/mtcars.csv
./DS-SEA-06/data/NBA_players_2015.csv
./DS-SEA-06/data/ozone.csv
./DS-SEA-06/data/pronto_cycle_share/2015_station_data.csv
./DS-SEA-06/data/pronto_cycle_share/2015_trip_data.csv
./DS-SEA-06/data/pronto_cycle_share/2015_weather_data.csv
./DS-SEA-06/data/rossmann.csv
./DS-SEA-06/data/rt_critics.csv
./DS-SEA-06/data/sms.tsv
./DS-SEA-06/data/stores.csv
./DS-SEA-06/data/syria.csv
./DS-SEA-06/data/time_series_train.csv
./DS-SEA-06/data/titanic.csv
./DS-SEA-06/data/ufo.csv
./DS-SEA-06/data/vehicles_test.csv
./DS-SEA-06/data/vehicles_train.csv
./DS-SEA-06/data/yelp.csv
```

---------

**Question 7:**
Count the approximate number of occurrences of the word "dictionary" (regardless of case) across all files of [our class repo] (https://github.com/ga-students/DS-SEA-3).

**Solution**

Command with Output

```
grep -ri dictionary DS-SEA-06/ | wc -l
80
```
