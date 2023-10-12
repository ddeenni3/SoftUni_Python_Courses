def next_version(version: list):
    version[2] += 1
    if version[2] > 9:
        version[2] = 0
        version[1] += 1
        if version[1] > 9:
            version[1] = 0
            version[0] += 1
    return list(map(str, version))


current_version = list(map(int, input().split('.')))

print('.'.join(next_version(current_version)))

