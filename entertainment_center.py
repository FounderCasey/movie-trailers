import fresh_tomatoes
import media

# List of movies
this_is_where_i_leave_you = media.Movie(
    "This Is Where I leave You",
    "A family finally comes together after the passing of the father.",
    "http://t0.gstatic.com/images?q=tbn:ANd9GcTvx5pCM0lkBYbngKNfZroORVVnYW8iGI_i5atzJdvwCyNddBg0", # noqa
    "https://www.youtube.com/watch?v=fH0cEP0mvlU",
    "R",
    "1h 43m",
    "September 19, 2014")

gone_girl = media.Movie(
    "Gone Girl",
    "A man tries to prove his innocence after his wife dissapears.",
    "http://t1.gstatic.com/images?q=tbn:ANd9GcTwcWs6CK22NdvXZH0CbigLxoV-N3GIJypphImFYYv1vG_VKXTQ", # noqa
    "https://www.youtube.com/watch?v=Ym3LB0lOJ0o",
    "R",
    "2h 29m",
    "October 3, 2014")

black_mass = media.Movie(
    "Black Mass",
    "Whitey Bulger is is on the loose. This mad man is dangerous.",
    "http://t2.gstatic.com/images?q=tbn:ANd9GcSK3LiV9aI4uMtI91ZJjDM15AazxWB5uKkxV8D04NARj2sJdBOG", # noqa
    "https://www.youtube.com/watch?v=CE3e3hGF2jc",
    "R",
    "2h 3m",
    "September 18, 2015")

attack_the_block = media.Movie(
    "Attack The Block",
    "London teenagers defend their block from falling aliens.",
    "http://www.graffitiwithpunctuation.net/wp-content/uploads/2014/11/attackthebloxkposter.jpg", # noqa
    "https://www.youtube.com/watch?v=cD0gm7dHKKc",
    "R",
    "1h 28m",
    "July 29, 2011")

the_hurt_locker = media.Movie(
    "The Hurt Locker",
    "A Staff Sergeant goes on a daring EOD raid.",
    "https://resizing.flixster.com/AXN5EcGmOKPYd1fA6wq0ijmIsx4=/800x1200/v1.bTsxMTE3NTc3MztqOzE3MDcyOzIwNDg7ODAwOzEyMDA", # noqa
    "https://www.youtube.com/watch?v=2GxSDZc8etg",
    "R",
    "2h 11m",
    "June 5, 2009")

zootopia = media.Movie(
    "Zootopia",
    "Fox and a bunny are unlikly friends but awesome parters!",
    "http://t3.gstatic.com/images?q=tbn:ANd9GcQs5vPjzQ1GGkUi1HTW970HfTpdrhyZu13PPRua_pjKSqoGSSzg", # noqa
    "https://www.youtube.com/watch?v=jWM0ct-OLsM",
    "PG",
    "1h 48m",
    "March 4, 2016")

# Compiling a list of movies
movies = [attack_the_block, black_mass, gone_girl, the_hurt_locker, this_is_where_i_leave_you, zootopia]

# Accessing fresh_tomatoes.py to access open_movies_page function
fresh_tomatoes.open_movies_page(movies)
