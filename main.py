"""

    """

from pathlib import Path

import pandas as pd
from githubdata import GitHubDataRepo
from persiantools.characters import ar_to_fa

from mirutil.ns import update_ns_module , rm_ns_module
from mirutil.df import save_as_prq_wo_index as save_as_prq

update_ns_module()
import ns

gdu = ns.GDU()
c = ns.Col()

ptrns = {
        0     : lambda x : x ,
        'f0'  : lambda x : ar_to_fa(x) ,
        1     : lambda x : x + '1' ,
        'f1'  : lambda x : ar_to_fa(x) + '1' ,
        2     : lambda x : x + '2' ,
        'f2'  : lambda x : ar_to_fa(x) + '2' ,
        3     : lambda x : x + '3' ,
        'f3'  : lambda x : ar_to_fa(x) + '3' ,
        4     : lambda x : x + '4' ,
        'f4'  : lambda x : ar_to_fa(x) + '4' ,
        'h'   : lambda x : x + 'ح' ,
        'fh'  : lambda x : ar_to_fa(x) + 'ح' ,
        'h1'  : lambda x : x + 'ح' + '1' ,
        'fh1' : lambda x : ar_to_fa(x) + 'ح' + '1' ,
        'h2'  : lambda x : x + 'ح' + '2' ,
        'fh2' : lambda x : ar_to_fa(x) + 'ح' + '2' ,
        'h3'  : lambda x : x + 'ح' + '3' ,
        'fh3' : lambda x : ar_to_fa(x) + 'ح' + '3' ,
        'h4'  : lambda x : x + 'ح' + '4' ,
        'fh4' : lambda x : ar_to_fa(x) + 'ح' + '4' ,
        }

def main() :
    pass

    ##

    gdsa = GitHubDataRepo(gdu.srca)
    gdsa.clone_overwrite()

    ##
    dfa = gdsa.read_data()

    ##
    df = pd.DataFrame()

    for _ , vl in ptrns.items() :
        _df = dfa.copy()
        _df[c.tic] = _df[c.ftic].apply(vl)

        df = pd.concat([df , _df])

    ##
    df = df.drop_duplicates()

    ##
    gdsb = GitHubDataRepo(gdu.srcb)
    gdsb.clone_overwrite()

    ##
    dfb = gdsb.read_data()

    ##
    dfb = dfb[[c.btic , c.ftic]]

    ##
    dfc = pd.DataFrame()

    for _ , vl in ptrns.items() :
        _df = dfb.copy()
        _df[c.tic] = _df[c.btic].apply(vl)

        dfc = pd.concat([dfc , _df])

    ##
    dfc = dfc.drop_duplicates()

    ##
    df = pd.concat([df , dfc])

    ##
    df = df.drop_duplicates()

    ##
    df = df[[c.tic , c.ftic]]

    ##
    msk = df.duplicated(subset = c.tic , keep = False)
    df1 = df[msk]

    ##
    df = df[~ msk]

    ##
    df = df.sort_values(by = [c.ftic , c.tic])

    ##
    gdt = GitHubDataRepo(gdu.trg)
    gdt.clone_overwrite()

    ##
    dffp = gdt.local_path / 'data.prq'

    ##
    save_as_prq(df , dffp)

    ##
    msg = 'Updated by: '
    msg += gdu.slf

    ##
    gdt.commit_and_push(msg)

    ##
    gdsa.rmdir()
    gdsb.rmdir()
    gdt.rmdir()

    rm_ns_module()

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')
