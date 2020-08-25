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

class WatchList:
    def __init__(self):
        self.watch_list = []

    def add_movie(self, movie):
        if movie not in self.watch_list:
            self.watch_list.append(movie)

    def remove_movie(self, movie):
        try:
            i = self.watch_list.index(movie)
            self.watch_list.pop(i)
        except ValueError:
            pass

    def select_movie_to_watch(self, index):
        lst_len = self.size()
        if index >= lst_len:
            return None
        return self.watch_list[index]

    def size(self):
        return len(self.watch_list)

    def first_movie_in_watchlist(self):
        lst_len = self.size()
        if lst_len > 0:
            return self.watch_list[0]
        return None

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        lst_len = self.size()
        if self.i < lst_len:
            m = self.watch_list[self.i]
            self.i += 1
            return m
        else:
            raise StopIteration()
