# n = int(input())
# print(n//3600,":",n//60,":",n % 60)


# second = int(input())
# hr = second//3600
# mint = int(second//60)
# sec = second%60
# print(str(hr)+":"+str(mint)+":"+str(sec))

second = int(input())
mint = int(second//60)
sec = second%60
hr = second//3600

print(str(hr)+":"+str(mint)+":"+str(sec))

# seconds = int(input());
#
# minutes = int(seconds/60);
# seconds -= minutes*60;
# hours = int(minutes/60);
# minutes -= hours*60;
#
# print(repr(hours)+":"+repr(minutes)+":"+repr(seconds))

