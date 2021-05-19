def game_with_number (arr,  n) : 
    #Complete the function
    
    for i in range(n-1):
        arr[i]=(arr[i]|arr[i+1]) #performing or operation on consecutive elements and printing the new array
    return arr
