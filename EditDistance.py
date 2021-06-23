def editDistance( source, target):
    sourceLength = len(source)
    targetLength = len(target)
    if sourceLength == 0:
        return targetLength
    if targetLength == 0:
        return sourceLength
    dist = []
    for i in range(sourceLength + 1):
        row = [0] * (targetLength + 1)
        dist.append(row)
    for i in range(sourceLength + 1):
        for j in range(targetLength + 1):
            if i == 0:
                dist[i][j] = j
            elif j == 0:
                dist[i][j] = i
            else:
                if source[i - 1] == target[j - 1]:
                    dist[i][j] = dist[i - 1][j - 1]
                else:
                    dist[i][j] = min(dist[i - 1][j - 1], dist[i][j - 1], dist[i - 1][j]) + 1
    return dist[sourceLength][targetLength]




