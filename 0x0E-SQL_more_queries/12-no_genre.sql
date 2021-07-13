-- Import the database dump from hbtn_0d_tvshows to your MySQL server
SELECT s.title, sg.genre_id FROM tv_show_genres sg RIGHT OUTER JOIN tv_shows s ON sg.show_id = s.id WHERE sg.show_id IS NULL ORDER BY s.title, sg.genre_id;
