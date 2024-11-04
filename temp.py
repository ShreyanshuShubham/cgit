from dataclasses import dataclass

class Committer():
    def __init__(self,raw_data:str) -> None:
        print(raw_data)
        s = raw_data.split(" ")
        self.time=s[-1]
        self.epoc = s[-2]
        self.email=s[-3][1:-1]
        self.full_name=" ".join(s[:-3])
    
    def __repr__(self) -> str:
        return f"{self.full_name} <{self.email}> {self.epoc} {self.time}"

# @dataclass
class Commit():
    # tree : str # ref to tree object
    # parent : str # parent commit
    # # author : str # Full Name <email@address.com> epoc timeUTC ; omiting this for now
    # committer : str # Full Name <email@address.com> epoc timeUTC
    # # gpgsig : str # 16 line ; omiting this for now
    # # after the sig there is a space that should be ignored
    # commit_message : str # the remaining following the empty line

    def __init__(self,raw_data:str):
        s = raw_data.splitlines()
        self.tree = s[0].split(" ")[1]
        self.parent = s[1].split(" ")[1]
        self.committer = Committer(" ".join(s[2].split(" ")[1:]))
        self.commit_message = "\n".join(s[4:])
        print(f"#{self.commit_message}#")
        pass

    def __repr__(self) -> str:
        return f"tree {self.tree}\nparent {self.parent}\ncommitter {self.committer}\n\n{self.commit_message}"

data="""tree 29ff16c9c14e2652b22f8b78bb08a5a07930c147
parent 206941306e8a8af65b66eaaaea388a7ae24d49a0
committer Thibault Polge <thibault@thb.lt> 1527025044 +0200

Create first draft
but now this is 
a multiline commit"""

c = Commit(data)
print(c)