# 面试题43：n个骰子的点数
# 题目：把n个骰子扔在地上，
# 所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

# 面试题44：扑克牌的顺子

# 题目：从扑克牌中随机抽 5张牌，判断是不是一个顺子，即这 
# 5张牌是不是连续的。2～10为数字本身，
# A为1，J为11，Q为12，K为13，而大、小王可以看成任意数字。
def numberOfDice(n):
    dp = [0 for _ in range(6*n+1)]
    
    for i in range(1,7):
        dp[i] = 1 
        
    for i in range(2,n+1):
        for j in range(6*i,-1,-1):
            dp[j] = 0 
            for k in range(6,0,-1):
                if j - k < 0:
                    continue  
                dp[j] += dp[j-k]
                
    return dp[n:]
###################################################
def probability(original,current,sum,pProbabilites):
    if current == 1:
        pProbabilites[sum-original] += 1 
        
    else:
        for i in range(1,7):
            probability(original,current-1,i+sum,pProbabilites)

def prob(number,pProbabilites):
    for i in range(1,7):
        probability(number,number,i,pProbabilites)
        
def printProb(number):
    if number < 1:
        return  
    maxSum = 6 * number  
    pProbabilites = int[maxSum-number+1]
    for i in range(number,maxSum+1):
        pProbabilites[i-number] = 0
        
    prob(number,pProbabilites)
    
    total = pw
    

if __name__ == '__main__':
    n = 2 
    res = numberOfDice(n)
    print(res)