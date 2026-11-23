strs = ["act","pots","tops","cat","stop","hat"]

class Solustion:
    def groupAns(self, strs:list[str]):
        group = {}

        for str1 in strs:
            key = "".join(sorted(str1))
            if key not in group:
                group[key] = []
            group[key].append(str1)
        return list(group.values())

obj = Solustion()
print(obj.groupAns(strs))