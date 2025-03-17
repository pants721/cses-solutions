n, m, k = map(int, input().split())
applicants = list(map(int, input().split()))
apartments = list(map(int, input().split()))

applicants.sort()
apartments.sort()

sum = 0

app_ptr = 0
apt_ptr = 0

while app_ptr < n and apt_ptr < m:
    app = applicants[app_ptr]
    apt = apartments[apt_ptr]
    diff = abs(app - apt)
    if diff <= k:
        sum += 1
        app_ptr += 1
        apt_ptr += 1
    else:
        if app >= apt:
            apt_ptr += 1
        else:
            app_ptr += 1

print(sum)


