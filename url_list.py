with open('image_urls.txt', 'r') as f:
    url_list = []
    total = 0
    for line in f:
        total += 1
        if total <= 100:
            url_list.append(line.strip('\n'))

    print(url_list)
