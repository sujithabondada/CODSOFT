# ============================================================
# CodSoft AI Internship — Task 4
# Movie Recommendation System
# Using Content-Based + Collaborative Filtering
# ============================================================

# No extra libraries needed — only built-in Python!

# ──────────────────────────────────────────────
# Movie Database
# ──────────────────────────────────────────────
movies = {
    1:  {"title": "The Dark Knight",       "genre": ["Action", "Crime", "Drama"],      "rating": 9.0},
    2:  {"title": "Inception",             "genre": ["Action", "Sci-Fi", "Thriller"],  "rating": 8.8},
    3:  {"title": "Interstellar",          "genre": ["Sci-Fi", "Drama", "Adventure"],  "rating": 8.6},
    4:  {"title": "The Matrix",            "genre": ["Action", "Sci-Fi"],              "rating": 8.7},
    5:  {"title": "Avengers: Endgame",     "genre": ["Action", "Adventure", "Sci-Fi"], "rating": 8.4},
    6:  {"title": "The Godfather",         "genre": ["Crime", "Drama"],                "rating": 9.2},
    7:  {"title": "Pulp Fiction",          "genre": ["Crime", "Drama", "Thriller"],    "rating": 8.9},
    8:  {"title": "The Shawshank",         "genre": ["Drama"],                         "rating": 9.3},
    9:  {"title": "Forrest Gump",          "genre": ["Drama", "Romance"],              "rating": 8.8},
    10: {"title": "Titanic",               "genre": ["Drama", "Romance"],              "rating": 7.9},
    11: {"title": "Spider-Man",            "genre": ["Action", "Adventure"],           "rating": 7.4},
    12: {"title": "Iron Man",              "genre": ["Action", "Sci-Fi"],              "rating": 7.9},
    13: {"title": "Joker",                 "genre": ["Crime", "Drama", "Thriller"],    "rating": 8.4},
    14: {"title": "Get Out",               "genre": ["Horror", "Thriller"],            "rating": 7.7},
    15: {"title": "A Quiet Place",         "genre": ["Horror", "Sci-Fi", "Thriller"],  "rating": 7.5},
}

# User ratings database (collaborative filtering)
user_ratings = {
    "Alice": {1: 5, 2: 4, 3: 5, 4: 4, 6: 3},
    "Bob":   {2: 5, 3: 4, 4: 5, 5: 4, 12: 5},
    "Carol": {6: 5, 7: 5, 8: 5, 9: 4, 13: 4},
    "Dave":  {1: 4, 5: 5, 11: 5, 12: 4, 4: 3},
    "Eve":   {8: 5, 9: 5, 10: 4, 6: 4, 7: 3},
}

# ──────────────────────────────────────────────
# Content-Based Filtering
# Recommends movies with similar genres
# ──────────────────────────────────────────────
def content_based_recommend(movie_id, top_n=5):
    if movie_id not in movies:
        return []

    target = movies[movie_id]
    target_genres = set(target["genre"])
    scores = []

    for mid, movie in movies.items():
        if mid == movie_id:
            continue
        common_genres = target_genres & set(movie["genre"])
        score = len(common_genres) + movie["rating"] * 0.1
        scores.append((mid, score, movie["title"], movie["genre"], movie["rating"]))

    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:top_n]

# ──────────────────────────────────────────────
# Collaborative Filtering
# Recommends based on what similar users liked
# ──────────────────────────────────────────────
def find_similar_users(username, user_ratings):
    if username not in user_ratings:
        return []

    user_movies = set(user_ratings[username].keys())
    similarity = []

    for other_user, ratings in user_ratings.items():
        if other_user == username:
            continue
        other_movies = set(ratings.keys())
        common = user_movies & other_movies
        if common:
            # Simple similarity: average rating difference on common movies
            diff = sum(abs(user_ratings[username][m] - ratings[m]) for m in common)
            sim_score = len(common) / (1 + diff)
            similarity.append((other_user, sim_score))

    similarity.sort(key=lambda x: x[1], reverse=True)
    return similarity

def collaborative_recommend(username, top_n=5):
    if username not in user_ratings:
        return []

    similar_users = find_similar_users(username, user_ratings)
    watched = set(user_ratings[username].keys())
    recommendations = {}

    for similar_user, sim_score in similar_users:
        for movie_id, rating in user_ratings[similar_user].items():
            if movie_id not in watched:
                if movie_id not in recommendations:
                    recommendations[movie_id] = 0
                recommendations[movie_id] += rating * sim_score

    sorted_recs = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return sorted_recs[:top_n]

# ──────────────────────────────────────────────
# Display Helpers
# ──────────────────────────────────────────────
def display_movies():
    print("\n" + "=" * 50)
    print("         🎬 Available Movies")
    print("=" * 50)
    for mid, movie in movies.items():
        genres = ", ".join(movie["genre"])
        print(f"  {mid:2}. {movie['title']:<30} ⭐ {movie['rating']}  [{genres}]")
    print("=" * 50)

def display_users():
    print("\n" + "=" * 50)
    print("         👤 Available Users")
    print("=" * 50)
    for user, ratings in user_ratings.items():
        watched = [movies[m]["title"] for m in ratings.keys()]
        print(f"  {user}: watched {len(watched)} movies")
    print("=" * 50)

# ──────────────────────────────────────────────
# Main Menu
# ──────────────────────────────────────────────
def main():
    print("=" * 50)
    print("   CodSoft AI Internship — Task 4")
    print("   Movie Recommendation System")
    print("=" * 50)

    while True:
        print("\n📌 MENU:")
        print("  1. Content-Based Recommendation (by movie)")
        print("  2. Collaborative Filtering (by user)")
        print("  3. Show all movies")
        print("  4. Show all users")
        print("  5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        # ── Content-Based ──────────────────────
        if choice == '1':
            display_movies()
            try:
                movie_id = int(input("Enter movie number to get similar recommendations: "))
                if movie_id not in movies:
                    print("Invalid movie number!")
                    continue
                recs = content_based_recommend(movie_id)
                print(f"\n🎬 Because you liked '{movies[movie_id]['title']}', you might enjoy:")
                print("-" * 50)
                for i, (mid, score, title, genre, rating) in enumerate(recs, 1):
                    print(f"  {i}. {title:<30} ⭐ {rating}  {genre}")
            except ValueError:
                print("Please enter a valid number!")

        # ── Collaborative ──────────────────────
        elif choice == '2':
            display_users()
            username = input("Enter username: ").strip().capitalize()
            if username not in user_ratings:
                print(f"User '{username}' not found!")
                continue
            recs = collaborative_recommend(username)
            if not recs:
                print("Not enough data for recommendations!")
                continue
            print(f"\n👤 Recommendations for {username}:")
            print("-" * 50)
            for i, (mid, score) in enumerate(recs, 1):
                movie = movies[mid]
                print(f"  {i}. {movie['title']:<30} ⭐ {movie['rating']}")

        # ── Show Movies ────────────────────────
        elif choice == '3':
            display_movies()

        # ── Show Users ─────────────────────────
        elif choice == '4':
            display_users()

        # ── Exit ───────────────────────────────
        elif choice == '5':
            print("\nGoodbye! 👋 Happy watching!")
            break

        else:
            print("Invalid choice! Enter 1-5.")

# ──────────────────────────────────────────────
if __name__ == "__main__":
    main()
