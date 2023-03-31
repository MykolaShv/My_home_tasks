moves=# insert into directors (name, years_live, the_first_film , the_secomd_film) values ('James Wan', '1977- present', 'Aquaman 2', 'Malignant'), ('Sam Raimi', '1959- present', 'Spider-Man', 'The Black Ghiandola');
INSERT 0 2

moves=# SELECT name_film, type_film, production_company, name, years_live FROM films  INNER JOIN directors  ON 

moves=# SELECT name_film, type_film, production_company, name, years_live FROM films  LEFT JOIN  directors  ON 

moves=# SELECT name_film, type_film, production_company, name, years_live FROM films  FULL  JOIN  directors  ON (directors.the_first_film = films.name_film);

moves=# SELECT name_film, type_film, production_company, name, years_live FROM films  RIGHT  JOIN  directors  ON (directors.the_first_film = films.name_film);

