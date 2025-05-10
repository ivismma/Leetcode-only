// https://leetcode.com/problems/single-number/

int singleNumber(int* nums, int numsSize) {
    int current = nums[0];
    for(int i = 1; i < numsSize; ++i){
        current = current ^ nums[i]; // xor
    }
    
    return current;
}
