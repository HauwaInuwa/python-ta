import sys
import os


def prime(s):
    # your code goes here
	if s>1:
		for n in range (2,s):
			if(s % n)==0:
				return False
			return True
		else:
			return False
numb = input ("Enter a number: ")	
s = int(numb)		
print(prime(s))

def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error())

    print(solution(sys.argv[1]))
