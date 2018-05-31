'''Q.4- Create a class MovieDetails and initialize it with artistname,Year of release and ratings .
Make methods to 
1. Display-Display the details.
2. Add- Add the movie details.'''
class MovieDetails:
    ''' class to add and display movie details''' 
    director=""
    producer=""
    genre=""
    def __init__(self):
        self.movie_name='unnamed'
        self.artist_name='unnamed'
        self.year_of_release=0
        self.ratings=0.0
    def display(self):
        ''' method for dispalying the movie details'''
        print("MovieName={}, ArtistName={}, Year Of Release={}, Ratings={}".\
              format(self.movie_name,self.artist_name,self.year_of_release,self.ratings))
    def add(self,movie_name,artist_name,year_of_release,ratings):
        ''' method to add movie details'''
        self.movie_name=movie_name
        self.artist_name=artist_name
        self.year_of_release=year_of_release
        self.ratings=ratings
mov=MovieDetails()
mov.add("PK","Amir Khan",2015,5)
mov.display();
