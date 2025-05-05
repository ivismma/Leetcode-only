// https://leetcode.com/problems/rotate-array/


// resolvi recursivo -> mais f�cil de codar, levemente mais lento.

// "cont" � pra contar quantos j� foram, pois est� percorrendo o vetor circularmente
// "newValue" salva quem era o

void _rotate(int *nums, int numsSize, int k, int i, int cont){
	if(cont < numsSize){
		int newValue = nums[i]; 		       // salva quem � o atual da pos. i
		_rotate(nums, numsSize, k, (i+1)%numsSize, cont+1);
		nums[(k+i)%numsSize] = newValue;       // volta a pilha de recurs�o alterando os 
	}                                          // (k+i)-�simos pelos previamente salvos
	else
		return;
}

void rotate(int* nums, int numsSize, int k) {
    _rotate(nums, numsSize, k, 0, 0);
}
