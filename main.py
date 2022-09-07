"""

    """

import pandas as pd
from githubdata import GithubData
from mirutil.df_utils import save_df_as_a_nice_xl as sxl


class GDUrl :
    cur = 'https://github.com/imahdimir/b-d-Ticker-2-FirmTicker'
    src = 'https://github.com/imahdimir/d-TSETMC_ID-2-FirmTicker'
    trg = 'https://github.com/imahdimir/d-Ticker-2-FirmTicker'

gdu = GDUrl()

class ColName :
    ftic = 'FirmTicker'
    tic = 'Ticker'

c = ColName()

ptrns = {
        0    : lambda x : x ,
        2    : lambda x : f'{x}2' ,
        3    : lambda x : f'{x}3' ,
        4    : lambda x : f'{x}4' ,
        'h'  : lambda x : f'{x}ح' ,
        'h2' : lambda x : f'{x}ح' + '2' ,
        'h3' : lambda x : f'{x}ح' + '3' ,
        'h4' : lambda x : f'{x}ح' + '4' ,
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
    dap = gd_trg.data_fp
    sxl(da , dap)

    ##
    msg = 'builded by: '
    msg += gdu.cur
    ##
    gd_trg.commit_and_push(msg)

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
