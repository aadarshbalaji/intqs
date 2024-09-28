class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        hs = {}
        for action in transactions:
            name, time, amount, city = action.split(',')
            time = int(time)
            if time in hs:
                if name in hs[time]:
                    hs[time][name].append(city)
                else:
                    hs[time][name] = [city]
            else:
                hs[time] = {name: [city]}
        
        ans = []
        for action in transactions:
            name, time, amount, city = action.split(',')
            time = int(time)
            amount = int(amount)
            if amount > 1000:
                ans.append(action)
                continue
            for t in range(time-60,time+61):
                if t in hs:
                    if name in hs[t]:
                        if hs[t][name][0] != city or len(hs[t][name]) > 1:
                            ans.append(action)
                            break
        return ans
