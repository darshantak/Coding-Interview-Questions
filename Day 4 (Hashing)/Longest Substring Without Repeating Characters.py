def longestSub(s):
    last_seen={}
    start=0
    max_len=0
    for i in range(len(s)):
        if s[i] in last_seen:
            start=max(start,last_seen[s[i]]+1)

        last_seen[s[i]]=i
        max_len=max(max_len,i-start+1)

    return max_len

string = "geeksforgeeks"

print(longestSub(string))