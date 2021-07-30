class sol:
    def missing_num(num):
        n=[0]*(len(num)+1)
        for i in num:
            n[i] += 1
        missing = []
        for i in range(len(n)):
            if n[i]==0 and i != 0:
                missing.append(i)
        return missing
ob = sol()
print(ob.missing_num([1,2,4,5]))

