def issubelement(seq: str, subelement: str, pos = 0) -> bool:
    l = len(subelement)
    if pos <0:
        new_seq = seq[-l::]
        return True if subelement == new_seq else False
    elif pos>0:
        new_seq = seq[:l]
        return True if subelement == new_seq else False
    elif pos == 0:
        sub_len = len(subelement)
        seq_len = len(seq)
        for i in range(1, seq_len - sub_len):
            if seq[i:i+sub_len] == subelement:
                return True
        return False

if __name__ == "__main__":
    assert issubelement('running', 'ing') == False
    assert issubelement('running', 'ing', -1) == True
    assert issubelement('running', 'ing', 1) == False
    assert issubelement('ingwer', 'ing') == False
    assert issubelement('ingwer', 'ing',-1) == False
    assert issubelement('ingwer', 'ing',1) == True
    assert issubelement('qwingwer', 'ing') == True
    assert issubelement('.2,', '2') == True
    assert issubelement('.2,', '2',-1) == False
    assert issubelement('.2,', '2',1) == False