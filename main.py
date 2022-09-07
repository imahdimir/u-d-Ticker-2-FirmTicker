"""

    """

import pandas as pd
from githubdata import GithubData
from mirutil.df_utils import save_df_as_a_nice_xl as sxl
from persiantools.characters import ar_to_fa


class GDUrl :
    cur = 'https://github.com/imahdimir/b-d-Ticker-2-FirmTicker'
    src0 = 'https://github.com/imahdimir/d-FirmTickers'
    src1 = 'https://github.com/imahdimir/md-Ticker-2-FirmTicker'
    trg0 = 'https://github.com/imahdimir/d-0-Ticker-2-FirmTicker'
    trgf = 'https://github.com/imahdimir/d-Ticker-2-FirmTicker'

gdu = GDUrl()

class ColName :
    ftic = 'FirmTicker'
    tic = 'Ticker'
    faftic = 'faFirmTicker'
    src = 'Source'

c = ColName()

class Source :
    ptr = 'ptr'  # builded by pattern
    man = 'man'  # manually added

src = Source()

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

    gd_src0 = GithubData(gdu.src0)
    gd_src0.overwriting_clone()
    ##
    ds0 = gd_src0.read_data()
    ##
    ds0 = ds0[[c.ftic]]
    ds0.drop_duplicates(inplace = True)
    ##
    df = pd.DataFrame()

    for _ , vl in ptrns.items() :
        _df = ds0.copy()
        _df[c.tic] = _df[c.ftic].apply(vl)

        df = pd.concat([df , _df])

    ##
    df.drop_duplicates(inplace = True)
    ##
    df[c.src] = src.ptr
    ##

    gd_src1 = GithubData(gdu.src1)
    gd_src1.overwriting_clone()
    ##
    ds1 = gd_src1.read_data()
    ##
    ds1[c.src] = src.man
    ##
    df = pd.concat([ds1 , df])
    ##

    msk = df.duplicated(subset = c.tic , keep = False)
    df1 = df[msk]
    ##
    df = df[~ msk]
    ##
    df.sort_values(by = [c.ftic , c.tic] , inplace = True)
    ##
    df = df[[c.tic , c.ftic , c.src]]

    ##

    gd_trg0 = GithubData(gdu.trg0)
    gd_trg0.overwriting_clone()
    ##
    dt0p = gd_trg0.data_fp
    ##
    sxl(df , dt0p)
    ##
    msg = 'builded by: '
    msg += gdu.cur
    ##
    gd_trg0.commit_and_push(msg)

    ##
    df.drop(columns = c.src , inplace = True)

    ##

    gd_trg = GithubData(gdu.trgf)
    gd_trg.overwriting_clone()
    ##
    dfp = gd_trg.data_fp
    sxl(df , dfp)

    ##
    msg = 'builded by: '
    msg += gdu.cur
    ##
    gd_trg.commit_and_push(msg)

    ##


    gd_src0.rmdir()
    gd_src1.rmdir()
    gd_trg0.rmdir()
    gd_trg.rmdir()


    ##

##
if __name__ == "__main__" :
    main()

##
# noinspection PyUnreachableCode
if False :
    pass

    ##


    ##


    ##

##
