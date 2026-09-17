import pandas as pd

from .data.sources import URL, SeriesID


def read_usa_bea_excel(**kwargs) -> pd.DataFrame:
    return pd.DataFrame()


def main() -> None:
    [
        #######################################################################
        # Fixed Assets Series: K160021, 1951--2011
        #######################################################################
        #######################################################################
        # K10002 << K100021 << K160021
        #######################################################################
        SeriesID("k1n31gd1es00", URL.BEA_FIXED_ASSETS_URL)
    ] or [
        #######################################################################
        # Fixed Assets Series: K10070
        #######################################################################
        SeriesID("K10070" or "K10002" or "K16002", URL.BEA_NIPA_URL)
    ] or [
        #######################################################################
        # U.S. Bureau of Economic Analysis, Produced assets, closing balance: Fixed assets (DISCONTINUED) [K160491A027NBEA], retrieved from FRED, Federal Reserve Bank of St. Louis;
        # https://fred.stlouisfed.org/series/K160491A027NBEA, August 23, 2018.
        # http://www.bea.gov/data/economic-accounts/national
        # https://fred.stlouisfed.org/series/K160491A027NBEA
        # https://search.bea.gov/search?affiliate=u.s.bureauofeconomicanalysis&query=k160491
        #######################################################################
        #######################################################################
        # 'K16049' Replaced with 'K10070' in 'combine_combined_archived()'
        #######################################################################
        SeriesID("K16049", URL.BEA_NIPA_URL)
    ]

    ###########################################################################
    # Fixed Assets Series: K160021, 1951--1969
    ###########################################################################
    SERIES_ID = "K160021"
    ###########################################################################
    # www.bea.gov/histdata/Releases/GDP_and_PI/2012/Q1/Second_May-31-2012/Section5ALL_Hist.xls
    ###########################################################################
    ###########################################################################
    # Metadata: 'Section5ALL_Hist.xls'@['dataset_usa_bea-release-2010-08-05 Section5ALL_Hist.xls' Offsets 'dataset_usa_bea-release-2013-01-31-SectionAll_xls_1929_1969.zip']"""
    ###########################################################################

    read_usa_bea_excel(
        **{
            "archive_name": "dataset_usa_bea-release-2013-01-31-SectionAll_xls_1929_1969.zip",
            "wb_name": "Section5ALL_Hist.xls",
            "sh_name": "50900 Ann",
        }
    ).loc[:, [SERIES_ID]]
