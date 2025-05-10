// https://leetcode.com/problems/missing-number/

int missingNumber(int* nums, int numsSize) {
    int i;
    bool *inArray = calloc(numsSize+1, sizeof(bool)); // válido usar pq 1 <= numsSize <= 10^4
    for(i = 0; i < numsSize; ++i)
        inArray[nums[i]] = true;

    for(i = 0; i < numsSize; ++i)
        if(inArray[i] == false)
            break;
    
    free(inArray);
    return i;
}
