def read_file():
    with open("back/users", 'r', encoding='utf-8') as file:
        users = file.read()
        print(users)


def get_users():
    users = {}
    with open("back/users", 'r', encoding='utf-8') as file:
        lines = [line.rstrip() for line in file]
        for x in lines:
            id_user = int(x[x.find('id') + 4 : x.find(", 'name")])
            name_user = x[x.find('user') + 7 : x.find(", 'voice")]
            voice_prompt = int(x[x.find('prompt') + 8 :])
            print(id_user)
            print(name_user)
            print(voice_prompt)
            users[id_user] = {'name_user': name_user, 'voice_prompt': voice_prompt}
    return users


def update_user(users):
    print(users)
    with open("back/users", 'w', encoding='utf-8') as file:
        result = "id: "
        for x in users:
            result += str(x) + ', '
            result += ''.join([y for y in str(users[x]) if y not in ['"', '{', '}']])
        print(result)
        file.write(result)
get_users()