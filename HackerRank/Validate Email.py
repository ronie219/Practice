def fun(s):
    email = s.split("@")
    if len(email) != 2 and email[0] != '':
        return False
    print(email)
    websitename = email[1].split(".")
    if len(websitename) != 2 and websitename[0] != '':
        return False
    if len(websitename[1]) > 3:
        return False
    for i in email[0]:
        if not (i.isdigit() or i.isalpha() or i == '_' or i == '-'):
            return False
    for i in websitename[0]:
        if not (i.isdigit() or i.isalpha()):
            return False
    return True
    
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)