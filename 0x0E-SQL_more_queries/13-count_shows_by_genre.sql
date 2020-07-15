-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

SELECT tv_genres.name AS genre, Count(tv_show_genres.show_id) AS number_of_shows FROM tv_shows LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id WHERE tv_show_genres.genre_id IS NULL ORDER BY genre DESC;
