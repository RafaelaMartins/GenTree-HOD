from typing import List, Optional

class Node:
    def __init__(self, name:str, nickname:str, gender:str, is_married:bool, pair:Optional['Node'], king:bool, children:Optional[List['Node']], parents:Optional[tuple['Node', 'Node']], dragon:str=None) -> None:
        self.name: Optional[str] = name
        self.nickname: Optional[str] = nickname
        self.gender: Optional[str] = gender
        self.is_married: Optional[bool] = is_married
        self.pair: Optional['Node'] = pair
        self.king: Optional[bool] = king
        self.children: Optional[List['Node']] = children
        self.parents: Optional[tuple['Node', 'Node']] = parents
        self.dragon: Optional[str] = dragon
