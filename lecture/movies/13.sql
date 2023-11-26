--In 13.sql, write a SQL query to list the names of all people who starred in a movie in which Kevin Bacon also starred.
--Your query should output a table with a single column for the name of each person.
--There may be multiple people named Kevin Bacon in the database. Be sure to only select the Kevin Bacon born in 1958.
--Kevin Bacon himself should not be included in the resulting list.

SELECT DISTINCT people_stars.name
FROM stars AS stars_kevin_bacon
JOIN stars AS stars_others ON stars_kevin_bacon.movie_id = stars_others.movie_id
JOIN people AS people_kevin_bacon ON stars_kevin_bacon.person_id = people_kevin_bacon.id
JOIN people AS people_stars ON stars_others.person_id = people_stars.id
WHERE people_kevin_bacon.name = 'Kevin Bacon' AND people_kevin_bacon.birth = 1958 AND people_stars.id != people_kevin_bacon.id;
