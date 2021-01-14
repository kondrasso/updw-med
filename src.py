def number_of_series_counter(ts):
    num_of_series = 1
    max_series_len = 1
    series_len = 1
    for i in range(len(ts)-1):
        if ts[i] != ts[i+1] and i+1 != len(ts):
            num_of_series += 1
            if series_len > max_series_len:
                max_series_len = series_len
            series_len = 0
        elif ts[i] == ts[i+1]:
            series_len += 1
        elif i+1 == len(ts):
            num_if_series += 1
            series_len += 1
    if series_len > max_series_len:
        max_series_len = series_len
    return num_of_series, max_series_len

def median_test(ts):
    ranged_series = np.array(ts)
    median = np.median(ranged_series)
    d_series = []
    
    for element in ts:
        if element > median:
            d_series.append(1)
        elif element == median:
            d_series.append(0)
        else:
            d_series.append(-1)
            
    n, tmax = number_of_series_counter(d_series)
    
    n_const = int(0.5 * (n + 1 - 1.96 * pow(n-1, 0.5)))
    tmax_const = int(3.3* np.log10(n+1))
                  
    if n > n_const and tmax < tmax_const:
        print('hypotesis approven')
    else:
        print('hypotesis declined')

        
def upward_downward_test(ts):
    d_series = []
    
    for i in range(len(ts)-1):
        y_diff = ts[i+1] - ts[i]
        if y_diff > 0:
            d_series.append(1)
        elif y_diff == 0:
            d_series.append(0)
        elif y_diff < 0:
            d_series.append(-1)
    
    n, tmax = number_of_series_counter(d_series)

    n_const = int((1/3) * (2 * n - 1) - 1.96 * pow((16 * n - 29)/90, 0.5)) 
    if n <= 26:
        tmax_const = 5
    elif n > 26 and n <= 153:
        tmax_const = 6
    elif n > 153 and n <= 1170:
        tmax_const = 7
    else:
        tmax_const = 8
    
    if n > n_const and tmax < tmax_const:
        print('hypotesis approven')
    else:
        print('hypotesis declined')
