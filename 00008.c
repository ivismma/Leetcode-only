// https://leetcode.com/problems/string-to-integer-atoi/

int myAtoi(char* s) {
    int i = 0;
	while(s[i] == ' ')
		++i;
	
	if(s[i] == '\0') return 0;
	
	
	long long value = 0;
	bool isNegative = false;
	
	if(s[i] == '-'){
		isNegative = true;
		++i;
	}
	else if(s[i] == '+')
		++i;
	
	char c = s[i++];
	while(c != '\0'){
		if(c < 48 || c > 57)
			break;
		else{
			int digit = c-48;
			
			if(!isNegative){
				if(value*10 + digit > INT_MAX)
					return INT_MAX;
			}
			else{
				if((long long) (-(value*10 + digit) <= INT_MIN))
					return INT_MIN;
			}
				
			value = value*10 + digit;
		}
		c = s[i++];
	}
	return (isNegative)? -value : value;
}
