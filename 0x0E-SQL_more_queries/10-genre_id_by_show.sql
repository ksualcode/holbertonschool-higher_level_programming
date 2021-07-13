-- Import the database dump from hbtn_0d_tvshows to your MySQL server
SELECT s.title, sg.genre_id FROM tv_show_genres sg INNER JOIN tv_shows s ON sg.show_id = s.id ORDER BY s.title, sg.genre_id;
