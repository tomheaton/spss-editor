import os
import pandas as pd
import numpy as np
import pyreadstat


def main():
    # data = pd.read_spss(os.path.join(os.path.dirname(__file__), './data/Profile1.sav'))
    # data.tail()
    df, meta = pyreadstat.read_sav(os.path.join(os.path.dirname(__file__), './data/Profile1.sav'))


if __name__ == '__main__':
    main()
