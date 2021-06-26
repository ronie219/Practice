for _ in range(int(input())):
    Amin,Bmin,Cmin,Tmin, A , B, C = map(int,input().split())
    single_subject = all([Amin <= A,Bmin <= B, Cmin <= C])
    cumulative = (A + B + C ) >= Tmin
    print("YES") if single_subject and cumulative else print("NO")