'''
we have seen so far how to perform 2 way merging
we have seen so far how to perform m way merging

in merge sort, we break the list into its most
primitive form, that is we break into single size list

so for length n, we have n single size list.
we now perform n-way merge on this particular list
and voilaaaa we have our resultant list merge sorted

'''
from m_merge import m_way_merge
import numpy as np 
l = [11,2,5,3,7,22,10, -9,0,1,345]

def merge_sort(l):
    # l = 
    response = m_way_merge([[i] for i in l])

    print('my final merge sorted list is ', response)

merge_sort(l)