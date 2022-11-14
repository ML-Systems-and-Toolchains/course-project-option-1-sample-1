# 14813/18813 Course Project Option1

Author: Chong Tan (chongtan); Yanjun Chen (yanjunc2)

# Please follow these steps to run the code

## Task1:

1. make sure your PostgreSQL is up and running.
2. run `pip install -r requirements.txt` to install all the required dependencies.
3. run `python3 project_task1.py`.
4. put your db username when you see "Enter your username:".
   - if you don't enter anything, the username will be set to 'postgres' by default.
5. put your db password when you see "Enter your password:".
   - Don't leave it blank.
   - make sure you put the correct username and password, otherwise you will have to rerun the code from step 3 to get correct result.
6. after the run completed, you should be able to see table 'fifa' in your database.
   - you can find [constraints for the dataset](#constraints-that-are-required-to-generate-dataset-for-task-1) and [dataset features](#features-for-fifa-table-2015-2022-in-task-1) in [additional information](#additional-information)

## Task2:

1. make sure your PostgreSQL is up and running and all the required dependencies are installed.
   - if dependencies are not installed, run `pip install -r requirements.txt`
2. run `python3 project_task2.py`.
3. when you see "Enter X values:", enter the number of clubs you want to see that have the highest number of players with contracts ending in 2023.
   - if you don't enter anything, it will be set to 1 by default
4. when you see "Enter Y values:", enter the number of clubs you want to see that have the highest average number of players older than 27.
   - if you don't enter anything, it will be set to 1 by default
5. put your db username when you see "Enter your username:".
   - if you don't put anything, the username will be 'postgres' by default.
6. put your db password when you see "Enter your password:". Don't leave it blank.
   - make sure you put the correct username and password, otherwise you will have to rerun the code from step 2 to get correct result.
7. after the run completed, you should be able to see the results in dataframe format with required size in terminal.
   - you can find [results table features](#task-2-results-explaining) in [additional information](#additional-information)

# Additional Information

## Constraints that are required to generate dataset for Task 1:

- Data file needs to be csv format.
- Data file name must be in format of 'players_xx.csv'.
- Year information must follow an underline ('\_') and only last two letter of year should be used.

sofifa_id: must be positive integer number

player_url: must be in url format

short_name: must be string

long_name: must be string

player_positions: a list of string

overall: must be positive integer

potential: must be positive integer

value_eur: must be positive float

wage_eur: must be positive float 

age: must to be positive integer

dob: must be in data format

height_cm: must to be positive integer

weight_kg: must to be positive integer

club_team_id: must be positive float

club_name: must be string

league_name: must be string

league_level: must be positive integer in range(1, 4)

club_position: must be string

club_jersey_number: must to be positive integer

club_loaned_from: must be string

club_joined: must be in data format

club_contract_valid_until: must be a year

nationality_id: must to be positive integer

nationality_name: must be string

nation_team_id: must be positive float

nation_position: must be string

nation_jersey_number: must to be positive integer

preferred_foot: must be either Right or Left

weak_foot: must be positive integer in range(1, 5)

skill_moves: must be positive integer in range(1, 5)

international_reputation: must be positive integer in range(1, 5)

work_rate: must be string (Medium, High, Low / Medium, High, Low)

body_type: must be string

real_face: must be boolean (Yes / No)

player_tags: must be list string

player_traits: must be list string

pace: must be positive integer

shooting: must be positive integer

passing: must be positive integer

dribbling: must be positive integer

defending: must be positive integer

physic: must be positive integer

attacking_crossing: must be positive integer

attacking_finishing: must be positive integer

attacking_heading_accuracy: must be positive integer

attacking_short_passing: must be positive integer

attacking_volleys: must be positive integer

skill_dribbling: must be positive integer

skill_curve: must be positive integer

skill_fk_accuracy: must be positive integer

skill_long_passing: must be positive integer

skill_ball_control: must be positive integer

movement_acceleration: must be positive integer

movement_sprint_speed: must be positive integer

movement_agility: must be positive integer

movement_reactions: must be positive integer

movement_balance: must be positive integer

power_shot_power: must be positive integer

power_jumping: must be positive integer

power_stamina: must be positive integer

power_strength: must be positive integer

power_long_shots: must be positive integer

mentality_aggression: must be positive integer

mentality_interceptions: must be positive integer

mentality_positioning: must be positive integer 

mentality_vision: must be positive integer

mentality_penalties: must be positive integer

defending_marking_awareness: must be positive integer

defending_standing_tackle: must be positive integer

defending_sliding_tackle: must be positive integer

goalkeeping_diving: must be positive integer

goalkeeping_handling: must be positive integer

goalkeeping_kicking: must be positive integer

goalkeeping_positioning: must be positive integer

goalkeeping_reflexes: must be positive integer

goalkeeping_speed: must be positive integer

ls: must be positive integer

st: must be positive integer

rs: must be positive integer

lw: must be positive integer

lf: must be positive integer

cf: must be positive integer

rf: must be positive integer

rw: must be positive integer

lam: must be positive integer

cam: must be positive integer

ram: must be positive integer

lm: must be positive integer

lcm: must be positive integer

cm: must be positive integer

rcm: must be positive integer

rm: must be positive integer

lwb: must be positive integer

ldm: must be positive integer

cdm: must be positive integer

rdm: must be positive integer

rwb: must be positive integer

lb: must be positive integer

lcb: must be positive integer

cb: must be positive integer

rcb: must be positive integer

rb: must be positive integer

gk: must be positive integer

player_face_url: must be in url format

club_logo_url: must be in url format

club_flag_url: must be in url format

nation_logo_url: must be in url format

nation_flag_url: must be in url format

year: must be in year format

## Features for 'fifa' table (2015-2022) in Task 1:

sofifa_id: unique player ID on sofifa

player_url: URL of the scraped player

short_name: player short name

long_name: player long name

player_positions: player preferred positions

overall: player current overall attribute

potential: player potential overall attribute

value_eur: player value (in EUR)

wage_eur: player weekly wage (in EUR)

age: player age

dob: player date of birth

height_cm: player height (in cm)

weight_kg: player weight (in kg)

club_team_id: club team_id on sofifa where the player plays

club_name: club name where the player plays

league_name: league name of the club

league_level: league rank of the club (e.g. English Premier League is 1, English League Championship is 2, etc.)

club_position: player position in the club (e.g. SUB means substitute, RES means reserve)

club_jersey_number: player jersey number in the club

club_loaned_from: club loaning out the player - if applicable

club_joined: date when the player joined his current club

club_contract_valid_until: player contract expiration date

nationality_id: player nationality id on sofifa

nationality_name: player nationality name

nation_team_id: national team_id on sofifa where the player plays

nation_position: player position in the national team

nation_jersey_number: player jersey number in the national team

preferred_foot: player preferred foot

weak_foot: player weak foot attribute

skill_moves: player skill moves attribute

international_reputation: player international reputation attribute

work_rate: player work rate attributes (attacking / defensive)

body_type: player body type

real_face: player real face

release_clause_eur: player release clause (in EUR) - if applicable

player_tags: player tags

player_traits: player traits

pace: player pace attribute

shooting: player shooting attribute

passing: player passing attribute

dribbling: player dribbling attribute

defending: player defending attribute

physic: player physic attribute

attacking_crossing: player crossing attribute

attacking_finishing: player finishing attribute

attacking_heading_accuracy: player heading accuracy attribute

attacking_short_passing: player short passing attribute

attacking_volleys: player volleys attribute

skill_dribbling: player dribbling attribute

skill_curve: player curve attribute

skill_fk_accuracy: player free-kick accuracy attribute

skill_long_passing: player long passing attribute

skill_ball_control: player ball control attribute

movement_acceleration: player acceleration attribute

movement_sprint_speed: player sprint speed attribute

movement_agility: player agility attribute

movement_reactions: player reactions attribute

movement_balance: player balance attribute

power_shot_power: player shot power attribute

power_jumping: player jumping attribute

power_stamina: player stamina attribute

power_strength: player strength attribute

power_long_shots: player long shots attribute

mentality_aggression: player aggression attribute

mentality_interceptions: player interceptions attribute

mentality_positioning: player positioning attribute

mentality_vision: player vision attribute

mentality_penalties: player penalties attribute

mentality_composure: player composure attribute

defending_marking_awareness: player marking awareness attribute

defending_standing_tackle: player standing tackle attribute

defending_sliding_tackle: player sliding tackle attribute

goalkeeping_diving: player GK diving attribute

goalkeeping_handling: player GK handling attribute

goalkeeping_kicking: player GK kicking attribute

goalkeeping_positioning: player GK positioning attribute

goalkeeping_reflexes: player GK reflexes attribute

goalkeeping_speed: player GK speed attribute

ls: player attribute playing as LS

st: player attribute playing as ST

rs: player attribute playing as RS

lw: player attribute playing as LW

lf: player attribute playing as LF

cf: player attribute playing as CF

rf: player attribute playing as RF

rw: player attribute playing as RW

lam: player attribute playing as LAM

cam: player attribute playing as CAM

ram: player attribute playing as RAM

lm: player attribute playing as LM

lcm: player attribute playing as LCM

cm: player attribute playing as CM

rcm: player attribute playing as RCM

rm: player attribute playing as RM

lwb: player attribute playing as LWB

ldm: player attribute playing as LDM

cdm: player attribute playing as CDM

rdm: player attribute playing as RDM

rwb: player attribute playing as RWB

lb: player attribute playing as LB

lcb: player attribute playing as LCB

cb: player attribute playing as CB

rcb: player attribute playing as RCB

rb: player attribute playing as RB

gk: player attribute playing as GK

player_face_url: URL of the player face

club_logo_url: URL of the club logo

club_flag_url: URL of the club nationality flag

nation_logo_url: URL of the national team logo

nation_flag_url: URL of the national flag

year: dataset year

## Task 2 results explaining:

1. club_name: club name that have the highest number of players with contracts ending in 2023

   count: number of players for each club in 2023

2. club_name: club name that have highest average number of players that are older than 27 years across all years

   count: number of players that are older than 27 years

   average: average number of players that match from 2015 to 2022

3. nation_position: the most frequent position for each nation in each year

   year: dataset year

   count: number of nation_position shown up in dataset

   rank: the rank in orde of number of count
