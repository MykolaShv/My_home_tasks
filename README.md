Server [localhost]:
Database [postgres]:
Port [5432]:
Username [postgres]:
Пароль користувача postgres:
psql (15.2)
УВАГА: Кодова стор?нка консол? (866) в?др?зняється в?д кодової стор?нки Windows (1251)
         8-б?тов? символи можуть працювати неправильно. Детальн?ше у розд?л?
         "Нотатки для користувач?в Windows" у документац?ї psql.
Введ?ть "help", щоб отримати допомогу.

postgres=# \!chcp1251
Нев?рна команда \!chcp1251
Спробуйте \? для отримання дов?дки.
postgres=# \! chcp 1251
Active code page: 1251
postgres=# \c moves
Ви тепер під'єднані до бази даних "moves" як користувач "postgres".
moves=# \l
                                                                  Список баз даних
   Назва    | Власник  | Кодування |   Порядок сортування   |         Ctype          | Локалізація ICU | Постачальник локалі |     Права доступу
------------+----------+-----------+------------------------+------------------------+-----------------+---------------------+-----------------------
 books      | postgres | UTF8      | Ukrainian_Ukraine.1251 | Ukrainian_Ukraine.1251 |                 | libc                |
 moves      | postgres | UTF8      | Ukrainian_Ukraine.1251 | Ukrainian_Ukraine.1251 |                 | libc                |
 postgres   | postgres | UTF8      | Ukrainian_Ukraine.1251 | Ukrainian_Ukraine.1251 |                 | libc                |
 py6        | postgres | UTF8      | Ukrainian_Ukraine.1251 | Ukrainian_Ukraine.1251 |                 | libc                |
 template0  | postgres | UTF8      | Ukrainian_Ukraine.1251 | Ukrainian_Ukraine.1251 |                 | libc                | =c/postgres          +
            |          |           |                        |                        |                 |                     | postgres=CTc/postgres
 template1  | postgres | UTF8      | Ukrainian_Ukraine.1251 | Ukrainian_Ukraine.1251 |                 | libc                | =c/postgres          +
            |          |           |                        |                        |                 |                     | postgres=CTc/postgres
 university | postgres | UTF8      | Ukrainian_Ukraine.1251 | Ukrainian_Ukraine.1251 |                 | libc                |
(7 рядків)


moves=# \d
                   Список відношень
 Схема  |      Назва       |      Тип      | Власник
--------+------------------+---------------+----------
 public | actors           | таблиця       | postgres
 public | actors_id_seq    | послідовність | postgres
 public | directors        | таблиця       | postgres
 public | directors_id_seq | послідовність | postgres
 public | films            | таблиця       | postgres
 public | films_id_seq     | послідовність | postgres
(6 рядків)


moves=# select * from actors;
 id |       name        | year
----+-------------------+------
  1 | Pattinson Robert  | 1995
  2 | Stewart Kristen   | 1995
  3 | Cage Nicolas      | 1996
  4 | Depp Johnny       | 1993
  5 | Statham Jason     | 1995
  6 | Jovovich Milla    | 1994
  7 | Roberts Julia     | 1998
  8 | Diesel Vin        | 1990
  9 | Downey Jr. Robert | 1994
 10 | Pitt Brad         | 1995
 11 | Butler Gerard     | 1997
 12 | Efron Zach        | 1997
 13 | Washington Denzel | 1996
 14 | Travolta John     | 1996
 15 | Radcliffe Daniel  | 1993
(15 рядків)


moves=# select * from directors;
 id |       name       |  years_live  |    the_first_film    |  the_secomd_film
----+------------------+--------------+----------------------+-------------------
  1 | Alfred Hitchcock | 1899-1980    | Strangers on a Train | Rear Window
  2 | Orson Welles     | 1915-1985    | Citizen Kane         | Touch of Evil
  3 | John Ford        | 1895-1973    | Stagecoach           | The Searchers
  4 | Howard Hawks     | 1896-1977    | Bringing Up Baby     | Rio Bravo
  5 | Martin Scorsese  | 1942-present | Taxi Driver          | Raging Bull
  6 | Akira Kurosawa   | 1910-1998    | Rashomon             | The Seven Samurai
  7 | Buster Keaton    | 1895-1966    | Sherlock Jr          | The Navigator
(7 рядків)


moves=# select * from films;
 id |           name_film            |    type_film    |  production_company
----+--------------------------------+-----------------+----------------------
  1 | Nimona                         | Animation       | 20th Century Studios
  2 | The Tigers Apprentice          | Animation       | Paramount Pictures
  3 | Sesame Street                  | Comedy          | Warner Bros.
  4 | Minecraft                      | Action          | Warner Bros.
  5 | Spider-Man                     | Animation       | Sony Pictures
  6 | Aquaman 2                      | Action          | Warner Bros.
  7 | Black Panther: Wakanda Forever | Science fiction | Disney
(7 рядків)


moves=# insert into directors (name, years_live, the_first_film , the_secomd_film) values ('James Wan', '1977- present', 'Aquaman 2', 'Malignant'), ('Sam Raimi', '1959- present', 'Spider-Man', 'The Black Ghiandola');
INSERT 0 2
moves=# select * from directors;
 id |       name       |  years_live   |    the_first_film    |   the_secomd_film
----+------------------+---------------+----------------------+---------------------
  1 | Alfred Hitchcock | 1899-1980     | Strangers on a Train | Rear Window
  2 | Orson Welles     | 1915-1985     | Citizen Kane         | Touch of Evil
  3 | John Ford        | 1895-1973     | Stagecoach           | The Searchers
  4 | Howard Hawks     | 1896-1977     | Bringing Up Baby     | Rio Bravo
  5 | Martin Scorsese  | 1942-present  | Taxi Driver          | Raging Bull
  6 | Akira Kurosawa   | 1910-1998     | Rashomon             | The Seven Samurai
  7 | Buster Keaton    | 1895-1966     | Sherlock Jr          | The Navigator
  8 | James Wan        | 1977- present | Aquaman 2            | Malignant
  9 | Sam Raimi        | 1959- present | Spider-Man           | The Black Ghiandola
(9 рядків)


moves=# SELECT name_film, type_film, production_company, name, years_live FROM films  INNER JOIN directors  ON (directors.the_first_film = films.name_film);
 name_film  | type_film | production_company |   name    |  years_live
------------+-----------+--------------------+-----------+---------------
 Spider-Man | Animation | Sony Pictures      | Sam Raimi | 1959- present
 Aquaman 2  | Action    | Warner Bros.       | James Wan | 1977- present
(2 рядки)


moves=# SELECT name_film, type_film, production_company, name, years_live FROM films  LEFT JOIN  directors  ON (directors.the_first_film = films.name_film);
           name_film            |    type_film    |  production_company  |   name    |  years_live
--------------------------------+-----------------+----------------------+-----------+---------------
 Nimona                         | Animation       | 20th Century Studios |           |
 The Tigers Apprentice          | Animation       | Paramount Pictures   |           |
 Sesame Street                  | Comedy          | Warner Bros.         |           |
 Minecraft                      | Action          | Warner Bros.         |           |
 Spider-Man                     | Animation       | Sony Pictures        | Sam Raimi | 1959- present
 Aquaman 2                      | Action          | Warner Bros.         | James Wan | 1977- present
 Black Panther: Wakanda Forever | Science fiction | Disney               |           |
(7 рядків)


moves=# SELECT name_film, type_film, production_company, name, years_live FROM films  FULL  JOIN  directors  ON (directors.the_first_film = films.name_film);
           name_film            |    type_film    |  production_company  |       name       |  years_live
--------------------------------+-----------------+----------------------+------------------+---------------
 Nimona                         | Animation       | 20th Century Studios |                  |
 The Tigers Apprentice          | Animation       | Paramount Pictures   |                  |
 Sesame Street                  | Comedy          | Warner Bros.         |                  |
 Minecraft                      | Action          | Warner Bros.         |                  |
 Spider-Man                     | Animation       | Sony Pictures        | Sam Raimi        | 1959- present
 Aquaman 2                      | Action          | Warner Bros.         | James Wan        | 1977- present
 Black Panther: Wakanda Forever | Science fiction | Disney               |                  |
                                |                 |                      | Martin Scorsese  | 1942-present
                                |                 |                      | Buster Keaton    | 1895-1966
                                |                 |                      | Akira Kurosawa   | 1910-1998
                                |                 |                      | Howard Hawks     | 1896-1977
                                |                 |                      | Alfred Hitchcock | 1899-1980
                                |                 |                      | John Ford        | 1895-1973
                                |                 |                      | Orson Welles     | 1915-1985
(14 рядків)


moves=# SELECT name_film, type_film, production_company, name, years_live FROM films  RIGHT  JOIN  directors  ON (directors.the_first_film = films.name_film);
 name_film  | type_film | production_company |       name       |  years_live
------------+-----------+--------------------+------------------+---------------
 Spider-Man | Animation | Sony Pictures      | Sam Raimi        | 1959- present
 Aquaman 2  | Action    | Warner Bros.       | James Wan        | 1977- present
            |           |                    | Martin Scorsese  | 1942-present
            |           |                    | Buster Keaton    | 1895-1966
            |           |                    | Akira Kurosawa   | 1910-1998
            |           |                    | Howard Hawks     | 1896-1977
            |           |                    | Alfred Hitchcock | 1899-1980
            |           |                    | John Ford        | 1895-1973
            |           |                    | Orson Welles     | 1915-1985
(9 рядків)


moves=#
