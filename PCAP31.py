def quota(quo):
    def embed(str):
        return quo+str+quo
    return embed
dblq = quota('"')
print(dblq('Jan Doe'))