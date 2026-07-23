# 장르마다 합을 구한다
# 장르높은순서대로 순서를 나열해서.. 각 장르마다 최대 2곡씩 선정한다
def get_melon_best_album(genre_array, play_array):
    n = len(genre_array)
    genre_total_play_dict = {}
    genre_index_play_array_dict = {}
    result = []
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]

        if genre not in genre_total_play_dict:
            genre_total_play_dict[genre]=play
            genre_index_play_array_dict[genre] = [[i,play]]
        else:
            genre_total_play_dict[genre]+=play
            genre_index_play_array_dict[genre].append([i,play])
    sorted_genre_play_array = sorted(genre_total_play_dict.items(),key=lambda item:item[1],reverse=True)

    for genre,_value in sorted_genre_play_array:
        index_play_array = genre_index_play_array_dict[genre]
        sorted_by_play_and_index_play_index_array = sorted(index_play_array,key=lambda item:item[1],reverse=True)
        for i in range(len(sorted_by_play_and_index_play_index_array)):
            if i > 1:
                break
            result.append(sorted_by_play_and_index_play_index_array[i][0])
    
    return result


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))