--In 6.sql, write a SQL query to determine the average rating of all movies released in 2012.
--Your query should output a table with a single column and a single
--row (not counting the header) containing the average rating.

SELECT AVG(rating) FROM ratings JOIN movies ON id = movie_id WHERE year = 2012;