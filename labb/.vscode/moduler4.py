import count
import mellan

print(count.nxt())
print(mellan.dubbel())

# mellan.py
import count


def dubbel():
    return count.nxt() * 2

# count.py
serie = [1.5 * x for x in range(1, 100)]
index = 0


def nxt():
    global index
    ret = serie[index]
    index = index + 1
    return ret
