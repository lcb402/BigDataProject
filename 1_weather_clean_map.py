import sys

for line in sys.stdin:
    #if line[0:6] != '  USAF':
    date = line[13:25]
    speed = line[30:34]
    gust = line[34:37]
    cloud = line[38:41]
    sky_cover = line[42:45]
    vsb = line[52:56]
    p_w1 = line[57:68]
    p_w2 = line[69:80]
    temp = line[83:87]
    dew = line[87:92]
    sea = line[93:99]
    max_temp = line[113:116]
    min_temp = line[117:120]
    l_p1 = line[121:126]
    l_p6 = line[127:132]
    l_p24 = line[133:138]
    snow = line[145:147]
    print '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (date, speed, gust, cloud, sky_cover, vsb, p_w1, p_w2, temp, dew, sea, max_temp, min_temp, l_p1, l_p6, l_p24, snow)

