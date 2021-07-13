-- Import the database dump from hbtn_0d_tvshows to your MySQL server
SELECT s.title FROM tv_shows s
INNER JOIN tv_show_genres sg ON sg.show_id = s.id
INNER JOIN tv_genres g ON sg.genre_id = g.id
WHERE g.name = "Comedy"
ORDER BY s.title ASC;
