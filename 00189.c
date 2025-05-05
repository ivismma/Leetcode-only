// https://leetcode.com/problems/rotate-array/


// resolvi recursivo -> mais fácil de codar, levemente mais lento.

// "cont" é pra contar quantos já foram, pois está percorrendo o vetor circularmente
// "newValue" salva quem era o

void _rotate(int *nums, int numsSize, int k, int i, int cont){
	if(cont < numsSize){
		int newValue = nums[i]; 		       // salva quem é o atual da pos. i
		_rotate(nums, numsSize, k, (i+1)%numsSize, cont+1);
		nums[(k+i)%numsSize] = newValue;       // volta a pilha de recursão alterando os 
	}                                          // (k+i)-ésimos pelos previamente salvos
	else
		return;
}

void rotate(int* nums, int numsSize, int k) {
    _rotate(nums, numsSize, k, 0, 0);
}
