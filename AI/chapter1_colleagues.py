def test():
    arr_numbers = ["one", "two", "three", "four"]
    arr_iter = [0, 1, 2, 3]
    arr_name = ["john", "carl", "jack", "leo"]

    print(
        [for_result
        for i in arr_iter
        for for_result in arr_name[i]]
    )

#test()
#pass

# предлагалка знакомых по знакомым знакомых
def main():
    users = [
        {"id": 0, "name": "Hero"},
        {"id": 1, "name": "Dunn"},
        {"id": 2, "name": "Sue"},
        {"id": 3, "name": "Chi"},
        {"id": 4, "name": "Thor"},
        {"id": 5, "name": "Clive"},
        {"id": 6, "name": "Hicks"},
        {"id": 7, "name": "Devin"},
        {"id": 8, "name": "Kate"},
        {"id": 9, "name": "Klein"}
    ]

    friendships_rcv = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), \
        (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

    # выделение места, массивы по кол-ву пользователей
    friendships = {user["id"]: [] for user in users}

    # заполнение друзей через итерацию по списку friendships_rcv
    for i, j in friendships_rcv:
        friendships[i].append(j)
        friendships[j].append(i)

    def number_of_friends(user):
        """ Сколько друзей у пользователя user """
        user_id = user["id"]
        friend_ids = friendships[user_id]
        return len(friend_ids)

    # сумма всех связей, всех пользователей
    total_connections = sum(number_of_friends(user) for user in users)

    # среднее кол-во связей у всех пользователей
    avg_connections = total_connections / len(users)
    
    # массив туплов (пользователь -> кол-во друзей)
    num_friends_by_id = [(user["id"], number_of_friends(user)) for\
         user in users]

    # сортировка по кол-ву друзей (каждый элемент массива как <id_and_friends>)
    num_friends_by_id.sort(key= lambda id_and_friends:\
         id_and_friends[1], reverse= True)

    def foaf_ids(user):
        searcher = user["id"]   # current user
        
        return [foaf_id
                for friend_id in friendships[user["id"]]
                for foaf_id in friendships[friend_id]
                if foaf_id != searcher
                and foaf_id not in friendships[searcher]]

    print(f"Рекомендованные друзья -> {foaf_ids(users[4])}")
    pass

if __name__ == "__main__":
    main()