"""

    """

import pandas as pd
from githubdata import GithubData
from mirutil.df_utils import save_df_as_a_nice_xl as sxl
from persiantools.characters import ar_to_fa


class GDUrl :
    cur = 'https://github.com/imahdimir/b-d-Ticker-2-FirmTicker'
    src = 'https://github.com/imahdimir/d-FirmTickers'
    trg = 'https://github.com/imahdimir/d-Ticker-2-FirmTicker'

gdu = GDUrl()

class ColName :
    ftic = 'FirmTicker'
    tic = 'Ticker'
    faftic = 'faFirmTicker'

c = ColName()

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

    gd_src = GithubData(gdu.src)
    gd_src.overwriting_clone()
    ##
    ds = gd_src.read_data()
    ##
    ds = ds[[c.ftic]]
    ds.drop_duplicates(inplace = True)
    ##
    df = pd.DataFrame()

    for _ , vl in ptrns.items() :
        _df = ds.copy()
        _df[c.tic] = _df[c.ftic].apply(vl)

        df = pd.concat([df , _df])

    ##
    df.drop_duplicates(inplace = True)
    ##
    msk = df.duplicated(subset = c.tic , keep = False)
    df1 = df[msk]
    ##
    df = df[~ msk]
    ##
    df.sort_values(by = [c.ftic , c.tic] , inplace = True)
    ##
    df = df[[c.tic , c.ftic]]
    ##

    gd_trg = GithubData(gdu.trg)
    gd_trg.overwriting_clone()
    ##
    da = gd_trg.read_data()
    ##
    da = pd.concat([da , df])
    ##
    da.drop_duplicates(inplace = True)
    ##
    msk = da.duplicated(subset = c.tic , keep = False)
    df1 = da[msk]

    da = da[~ msk]
    ##
    dap = gd_trg.data_fp
    sxl(da , dap)

    ##
    msg = 'builded by: '
    msg += gdu.cur
    ##
    gd_trg.commit_and_push(msg)

    ##


    gd_src.rmdir()
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
