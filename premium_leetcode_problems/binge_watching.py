def solve(durations):
    durations.sort()
    # duration of each movie less 1.99 to combine with other movie
    # at most 2 movies can be combined
    min_days = 0
    min_movie_index = 0
    for max_movie_index in range(len(durations)):
        if durations[max_movie_index] > 1.99:
            min_days +=1
        elif (min_movie_index < max_movie_index and durations[min_movie_index] + durations[max_movie_index] <= 3):
            min_movie_index +=1
            min_days +=1
    return min_days


if __name__ == "__main__":
    print(solve([1.90,1.04,1.25,2.5,1.75]))