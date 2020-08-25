import csv
import datetime

class Director: ##1
    def __init__(self, director_full_name = ""):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = "None"
        else:
            self.__director_full_name = director_full_name.strip()
        
    def __repr__(self):
        return "<Director " + self.__director_full_name  + ">"
        
    def __eq__(self, other):
        return self.__director_full_name == other.__director_full_name
        
    def __lt__(self, other):
        return self.__director_full_name < other.__director_full_name
        
    def __hash__(self):
        return hash(self.__director_full_name)

class Genre: ##2
    def __init__(self, genre_name = ""):
        if genre_name == "" or type(genre_name) != str:
            self.__genre_name = "None"
        else:
            self.__genre_name = genre_name.strip()
        
    def __repr__(self):
        if self.__genre_name == "":
            self.__genre_name = "None"
        return "<Genre " + self.__genre_name  + ">"
        
    def __eq__(self, other):
        return self.__genre_name == other.__genre_name
        
    def __lt__(self, other):
        return self.__genre_name < other.__genre_name
        
    def __hash__(self):
        return hash(self.__genre_name)

class Actor: ##3
    def __init__(self, name = ""):
        self.__actor_full_name = name
        if self.__actor_full_name == "" or type(self.__actor_full_name) != str:
            self.__actor_full_name = "None"
        else:
            self.__actorlst = []
        
    def __repr__(self):
        return "<Actor " + self.__actor_full_name  + ">"
        
    def __eq__(self, other):
        return self.__actor_full_name == other.__actor_full_name
        
    def __lt__(self, other):
        return self.__actor_full_name < other.__actor_full_name
        
    def __hash__(self):
        return hash(self.__actor_full_name)
    
    def add_actor_colleague(self, colleague):
        self.__actorlst += [colleague]
        
    def check_if_this_actor_worked_with(self, colleague):
        return colleague in self.__actorlst

class Movie: ##4
    def __init__(self, movie = "", year = int()):
        if movie != "" and type(movie) == str:
            movie = movie.strip()
            self.__title = movie
        if year >= 1900:
            self.__year = year
        self.__description = ""
        self.director = Director()
        self.actors = []
        self.genres = []
        self.runtime_minutes = int()

    def __setattr__(self, name, val):
        self.__dict__[name] = val
##        print(self.__dict__)
        if 'description' in self.__dict__:
            self.__dict__['description'] = self.__dict__['description'].strip()
        if 'runtime_minutes' in self.__dict__:
            if self.__dict__['runtime_minutes'] < 0:
                raise ValueError("Constraint: the runtime is a positive number")
        
    def __repr__(self):
        return "<Movie " + self.__title + ", " + str(self.__year) + ">"

    def __eq__(self, other):
        s = self.__title.lower() + str(self.__year)
        o = other.__title.lower() + str(other.__year)
        return s == o
        
    def __lt__(self, other):
        s = self.__title.lower() + str(self.__year)
        o = other.__title.lower() + str(other.__year)
        return s < o
        
    def __hash__(self):
        s = self.__title.lower() + str(self.__year)
        return hash(s)

    def add_actor(self, actor):
        self.actors.append(actor)

    def remove_actor(self, actor):
        try:
            self.actors.index(actor)
            self.actors.pop(self.actors.index(actor))
        except ValueError:
            pass
                   
    def add_genre(self, genre): 
        self.genres.append(genre)

    def remove_genre(self, genre):
        try:
            self.genres.index(genre)
            self.genres.pop(self.genres.index(genre))
        except ValueError:
            pass

class MovieFileCSVReader: ##5
    def __init__(self, filename):
        self.__file_name = filename
        self.dataset_of_movies = []
        self.dataset_of_actors = []
        self.dataset_of_directors = []
        self.dataset_of_genres = []
        
    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)
            
            index = 0
            all_act = []
            all_dir = []
            all_gen = []
            for row in movie_file_reader:
                title = row['Title']
                title = title.strip()
                release_year = int(row['Year'])
                mov = (title, release_year)
                
                actors = row['Actors']
                actors = actors.split(",")
                
                director = row['Director']
                director = director.strip()
                
                genre = row['Genre']
                genre = genre.split(",")

                self.dataset_of_movies += [mov]

                all_act += actors
                all_gen += genre
                
                if director not in self.dataset_of_directors:
                    self.dataset_of_directors += [director]

                index += 1

            for m in range(len(self.dataset_of_movies)): #movie
                self.dataset_of_movies[m] = Movie(self.dataset_of_movies[m][0], self.dataset_of_movies[m][1])
            
            for a in all_act: #actor
                a = a.strip()
                if a not in self.dataset_of_actors:
                    self.dataset_of_actors += [a]
            for i in range(len(self.dataset_of_actors)):
                self.dataset_of_actors[i] = Actor(self.dataset_of_actors[i])
                    
            for i in range(len(self.dataset_of_directors)): #director
                self.dataset_of_directors[i] = Director(self.dataset_of_directors[i])

            for g in all_gen: #genre
                g = g.strip()
                if g not in self.dataset_of_genres:
                    self.dataset_of_genres += [g]
            for i in range(len(self.dataset_of_genres)):
                self.dataset_of_genres[i] = Genre(self.dataset_of_genres[i])

class Review: ##6
    def __init__(self, movie = Movie(), review_text = "", rating = 1):
        self.movie = movie
        self.review_text = review_text.strip()
        self.timestamp = datetime.datetime.today()
        if type(rating) == int and rating >= 1 and rating <= 10:
            self.rating = rating
        else:
            self.rating = None

    def __repr__(self):
        return str(self.movie) + ", Review: " + str(self.review_text) + ", Rating: " + str(self.rating) + ", Time: " + str(self.timestamp)

    def __eq__(self, other):
        s = str(self.movie).lower() + self.review_text.lower() + str(self.rating) + str(self.timestamp)
        o = str(other.movie).lower() + other.review_text.lower() + str(other.rating) + str(other.timestamp)
        return  s == o

class User: ##7
    def __init__(self, username = str(), pw = str()):
        self.user_name = username.strip().lower()
        self.password = pw
        self.watched_movies = []
        self.reviews = []
        self.time_spent_watching_movies_minutes = int()

    def __repr__(self):
        return "<User " + self.user_name + ">"

    def __eq__(self, other):
        return self.user_name == other.user_name
    
    def __lt__(self, other):
        return self.user_name < other.user_name

    def __hash__(self):
        return hash(self.user_name)

    def watch_movie(self, movie):
        if movie not in self.watched_movies:
            self.watched_movies.append(movie)
        self.time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if review not in self.reviews:
            self.reviews.append(review)
