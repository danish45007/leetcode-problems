def solve(slots):
    intervals = {} #{start:end}
    res = []
    for start,end in slots:
        work = 0
        while start < end:
            if start in intervals:
                prev_end = intervals[start]
                intervals[start] = max(intervals[start],end)
                start = prev_end
            else:
                intervals[start] = end
                work +=1
                start +=1
        res.append(work)
    return res


if __name__ == '__main__':
    print(solve([[1,4],[4,7],[5,8]]))