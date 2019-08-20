"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces .
The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""
class Sol:
    def cal(self, s):
        s= s.replace(" ", "")
        i = 0
        items =[]

        while i < len(s):
            if s[i].isalnum():
                start = i
                while i < len(s) and s[i].isalnum():
                    i+=1
                items.append(s[start:i])
            else:
                items.append(s[i])
                i+=1

        items+=['+']
        numbers =[]
        operators = []
        sign = 1

        res = 0

        for item in items:
            if item.isalnum():
                numbers.append(int(item))
            else:
                if item in '*/':
                    operators.append(item)
                else:
            # After seeing a + or - sign, we can perform the actions in operators on numbers
            # and aggregate the result
                    temp = numbers[0]
                    for i in range(len(operators)):
                        if operators[i] == '*':
                            temp *= numbers[i + 1]
                        else:
                            temp //= numbers[i + 1]
            # The sign determines whether we add or substract from res
                    res +=sign * temp
            # This if/else clause determines what we do to the next number that comes in
                    sign = 1 if item == "+" else -1
            # Upon finishing aggregating to result, clear the numbers and operators array
                    numbers =[]
                    operators = []
        return res

if __name__ == '__main__':
    s="3+12*2"
    print(Sol().cal(s))
    t = s.split("+")

    e = int("   45 ")
    1==1
