def check_disk(disk1, disk2):
    return (disk1 < disk2) and not (disk1 % 2 == disk2 % 2)

def hanoi_solver(disks :int) -> str:
    hanoi_towers = {
        1 : [i for i in range(disks, 0, -1)],
        2 : [],
        3 : []
    }
    i, j = (2,3) if disks % 2 == 0 else (3,2) 
    moves = f"{hanoi_towers[1]} {hanoi_towers[2]} {hanoi_towers[3]}"


    while len(hanoi_towers[3]) < disks:
    
        while True:
            if len(hanoi_towers[i]) > 0:
                if len(hanoi_towers[1]) > 0 and check_disk(hanoi_towers[1][-1], hanoi_towers[i][-1]):
                    hanoi_towers[i].append(hanoi_towers[1].pop(-1))
                    moves += f"\n{hanoi_towers[1]} {hanoi_towers[2]} {hanoi_towers[3]}"
                elif len(hanoi_towers[j]) > 0 and check_disk(hanoi_towers[j][-1], hanoi_towers[i][-1]):
                    hanoi_towers[i].append(hanoi_towers[j].pop(-1))
                    moves += f"\n{hanoi_towers[1]} {hanoi_towers[2]} {hanoi_towers[3]}"
                else:
                    break
            elif len(hanoi_towers[1]) > 0:
                hanoi_towers[i].append(hanoi_towers[1].pop(-1))
                moves += f"\n{hanoi_towers[1]} {hanoi_towers[2]} {hanoi_towers[3]}"
            else:
                break
            
        while True:
            if len(hanoi_towers[j]) > 0:
                if len(hanoi_towers[i]) > 0 and check_disk(hanoi_towers[i][-1], hanoi_towers[j][-1]):
                    hanoi_towers[j].append(hanoi_towers[i].pop(-1))
                    moves += f"\n{hanoi_towers[1]} {hanoi_towers[2]} {hanoi_towers[3]}"
                elif len(hanoi_towers[1]) > 0 and check_disk(hanoi_towers[1][-1], hanoi_towers[j][-1]):
                    hanoi_towers[j].append(hanoi_towers[1].pop(-1))
                    moves += f"\n{hanoi_towers[1]} {hanoi_towers[2]} {hanoi_towers[3]}"
                else:
                    break
            elif len(hanoi_towers[1]) > 0:
                hanoi_towers[j].append(hanoi_towers[1].pop(-1))
                moves += f"\n{hanoi_towers[1]} {hanoi_towers[2]} {hanoi_towers[3]}"
            else:
                break
            
        while True:
            if len(hanoi_towers[1]) > 0:
                if len(hanoi_towers[j]) > 0 and check_disk(hanoi_towers[j][-1], hanoi_towers[1][-1]):
                    hanoi_towers[1].append(hanoi_towers[j].pop(-1))
                    moves += f"\n{hanoi_towers[1]} {hanoi_towers[2]} {hanoi_towers[3]}"
                elif len(hanoi_towers[i]) > 0 and check_disk(hanoi_towers[i][-1], hanoi_towers[1][-1]):
                    hanoi_towers[1].append(hanoi_towers[i].pop(-1))
                    moves += f"\n{hanoi_towers[1]} {hanoi_towers[2]} {hanoi_towers[3]}"
                else:
                    break
            elif len(hanoi_towers[2]) > 0:
                hanoi_towers[1].append(hanoi_towers[2].pop(-1))
                moves += f"\n{hanoi_towers[1]} {hanoi_towers[2]} {hanoi_towers[3]}"
            else:
                break  

    return moves
    

print(hanoi_solver(3))
