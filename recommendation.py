class MovieRecommendationSystem:
    def __init__(self):
        self.movie_ratings = {}  # Dictionary to store movie ratings

    def add_rating(self, user_id, movie_id, rating):
        """Add a user's rating for a movie."""
        if user_id not in self.movie_ratings:
            self.movie_ratings[user_id] = {}
        self.movie_ratings[user_id][movie_id] = rating

    def get_movie_recommendations(self, user_id):
        """Get movie recommendations for a user using collaborative filtering."""
        user_ratings = self.movie_ratings.get(user_id, {})
        if not user_ratings:
            return "User not found or no ratings available."

        # Calculate movie scores based on collaborative filtering (simple average of ratings)
        movie_scores = {}
        for other_user_id, other_ratings in self.movie_ratings.items():
            if other_user_id == user_id:
                continue
            for movie_id, rating in other_ratings.items():
                if movie_id not in user_ratings:
                    movie_scores.setdefault(movie_id, []).append(rating)

        # Sort movies by average score
        sorted_movie_scores = {movie_id: sum(scores) / len(scores) for movie_id, scores in movie_scores.items()}
        sorted_movie_scores = sorted(sorted_movie_scores.items(), key=lambda x: x[1], reverse=True)

        return [movie_id for movie_id, _ in sorted_movie_scores]


# Create a MovieRecommendationSystem instance
recommendation_system = MovieRecommendationSystem()

# Dummy movie ratings (user_id, movie_id, rating)
dummy_ratings = [
    (1, 'Movie1', 4.5),
    (1, 'Movie2', 3.0),
    (1, 'Movie3', 2.5),
    (2, 'Movie1', 3.5),
    (2, 'Movie4', 4.0),
    (3, 'Movie2', 2.0),
    (3, 'Movie3', 4.0),
    (2, "Created now", 10.0),
]

# Add dummy ratings to the recommendation system
for user_id, movie_id, rating in dummy_ratings:
    recommendation_system.add_rating(user_id, movie_id, rating)

# Get movie recommendations for user with ID 1
user_id = 2
recommendations = recommendation_system.get_movie_recommendations(user_id)

# Display the movie recommendations
print(f"Movie recommendations for user {user_id}: {recommendations}")


# code explanations 

# Calculate movie scores based on collaborative filtering (simple average of ratings)
# movie_scores = {}
# for other_user_id, other_ratings in self.movie_ratings.items():
#     if other_user_id == user_id:
#         continue
#     for movie_id, rating in other_ratings.items():
#         if movie_id not in user_ratings:
#             movie_scores.setdefault(movie_id, []).append(rating)


'''
self.movie_ratings.items() iterates over the items (key-value pairs) in the self.movie_ratings dictionary. In this context, each item represents a user and their associated movie ratings.

other_user_id is a variable that holds the user ID (key) of the current iteration. It represents a user other than the target user (user_id).

other_ratings is a variable that holds the movie ratings (value) associated with the current user (other_user_id). It is a dictionary where the keys are movie IDs, and the values are the ratings given by the user.

The if other_user_id == user_id condition checks if the current user is the target user (user_id). If it is the target user, we skip this iteration and continue to the next user.

The inner loop for movie_id, rating in other_ratings.items(): iterates over the movie ratings of the current user (other_user_id).

movie_id is a variable that holds the movie ID for the current iteration, and rating is a variable that holds the rating given by the user (other_user_id) for that movie.

The if movie_id not in user_ratings: condition checks if the target user (user_id) has not already rated the movie. If the movie is not rated by the target user, we collect the rating for that movie and store it in the movie_scores dictionary.

movie_scores.setdefault(movie_id, []).append(rating) appends the rating for the movie to its entry in the movie_scores dictionary. If the movie is not already in movie_scores, it creates a new entry for the movie with an empty list and then appends the rating to that list.
'''



# this :   # Sort movies by average score
#         sorted_movie_scores = {movie_id: sum(scores) / len(scores) for movie_id, scores in movie_scores.items()}
#         sorted_movie_scores = sorted(sorted_movie_scores.items(), key=lambda x: x[1], reverse=True)

#         return [movie_id for movie_id, _ in sorted_movie_scores]

'''
sorted_movie_scores = {movie_id: sum(scores) / len(scores) for movie_id, scores in movie_scores.items()}:

This line calculates the average score for each movie based on the collected ratings. It iterates over the movie_scores dictionary, where each entry contains movie IDs as keys and lists of ratings as values. The average score for each movie is calculated by summing the ratings and dividing by the number of ratings for that movie.
sorted_movie_scores = sorted(sorted_movie_scores.items(), key=lambda x: x[1], reverse=True):

This line sorts the movie scores in descending order based on the average score. It uses the sorted function with a custom sorting key. The key=lambda x: x[1] indicates that we want to sort based on the second element of each tuple (the average score).
reverse=True ensures that the sorting is in descending order, so the highest-rated movies come first.
return [movie_id for movie_id, _ in sorted_movie_scores]:

Finally, we extract and return a list of movie IDs from the sorted movie scores. We're interested in the movie IDs, so we use a list comprehension to iterate over the sorted movie scores and extract only the movie IDs.
'''