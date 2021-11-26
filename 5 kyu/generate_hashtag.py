def generate_hashtag(s):
    chars = '#' + ''.join(s.title().split())
    return False if (len(chars) > 140 or not s) else chars


# hey = " Hello there thanks    for trying my Kata"
# print(generate_hashtag(hey))