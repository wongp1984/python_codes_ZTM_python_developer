picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

def show_tree(emp, fill):
    for row in picture:
        astr = ''
        for x in row:
            astr=astr+emp if x==0 else astr+fill
        print(astr)

show_tree(fill='^', emp=' ')