self.A = {Александр, Екатерина, Анна, Оля, Виталий, Мария, София}
  
self.B = {Виктория, Андрей, Максим, Артем, Ярослав, Маргарита}
  
self.men - множество мужских имен, self.women - женских





def A_maty_B():
            a = set()
            for i in self.A:
                if i in self.women:
                    if i in self.men:
                        continue
                    else:
                        a.add(i)
            b = copy.copy(self.B)
            S = []
            for i in range(min(len(a), len(b))):
                p = random.choice(list(a))
                q = random.choice(list(b))
                S.append([p, q])
                a.remove(p)
                b.remove(q)
            print(S)
            return S
  
        def A_onuka_B():
            a = set()
            for i in self.A:
                if i in self.women:
                    if i in self.men:
                        continue
                    else:
                        a.add(i)
            w = self.B
            R = []
            for i in range(min(len(a), len(w))):
                p = random.choice(list(a))
                q = random.choice(list(w))
                if [p, q] not in self.S:
                    if [p, q] not in R:
                        R.append([p, q])
            print(R)
            return R
