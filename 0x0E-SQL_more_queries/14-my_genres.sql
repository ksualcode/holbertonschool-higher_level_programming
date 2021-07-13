-- Import the database dump from hbtn_0d_tvshows to your MySQL server
SELECT g.name FROM tv_genres g
INNER JOIN tv_show_genres sg ON sg.genre_id = g.id
INNER JOIN tv_shows s ON sg.show_id = s.id
WHERE s.title = "Dexter"
GROUP BY g.name
ORDER BY g.name ASC;
