

void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n){
    int i = 0; int j = 0;
    while (i <= (m+n-1))
        if (i == m)
            nums1[i++] = nums2[j++];

    int p = 0; int q = 0; int temp;
    for(p = 0; p<=(m+n-1); p++)
    {
        for(q = 0; q<=(m+n-1-p); q++)
        {
            if(nums1[q] > nums1[q+1])
            {
                temp = nums1[q];
                nums1[q] = nums1[q+1];
                nums1[q+1] = temp;
        }
    }
}



}
