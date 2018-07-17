class RelationException(Exception):
    def __init__(self, p1, p2):
        self.msg = "Are you sure " + p2 + " and " + p2 + " are in live with each other?"

    def __str__(self):
        return self.msg

relation = {'Jason':'Mary', 'Mary':'Jason', 'Jennifer':'Ken', 'Ken':'Jennifer', 'Tina':'Kim', 'Kim':'Tina'}
def check(pa, pb):
    if pa not in relation:
        print("No relation found")
        raise RelationException(pa, pb)
    elif relation[pa] != pb:
        # TODO: raise exception
        # TIPS: 這個地方會需要 raise 兩種 exception
        raise RelationException(pa, pb)

    
try:
    p1 = input("Please enter the first person: ")
    p2 = input("Please enter the second person: ")
    check(p1, p2)
    print("{} and {} are in love with each other!".format(p1, p2))
    
except RelationException as e:
    print(e)