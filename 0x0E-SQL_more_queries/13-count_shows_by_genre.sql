-- Import the database dump from hbtn_0d_tvshows to your MySQL server
SELECT g.name AS genre, COUNT(sg.genre_id) AS number_of_shows
FROM tv_genres g
INNER JOIN tv_show_genres sg
ON sg.genre_id = g.id
GROUP BY sg.genre_id, g.name
ORDER BY number_of_shows DESC;
