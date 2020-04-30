# Common imports
import numpy as np
import pandas as pd
import seaborn as sns
import os
# to make this notebook's output stable across runs
np.random.seed(42)

# To plot pretty figures
import matplotlib as mpl
import matplotlib.pyplot as plt

import dagster as dag
import yaml
from datetime import datetime
from dagster import TypeCheck, EventMetadataEntry


def get_data_stats(df):
    return [
        EventMetadataEntry.text(
            str(df.shape[0]), "n_rows", "Number of rows seen in the data frame",
        ),
        EventMetadataEntry.text(
            str(df.shape[1]), "n_cols", "Number of columns seen in the data frame",
        ),
        EventMetadataEntry.text(
            str(list(df.columns) if len(df.columns) < 50 else "Too Many to Display"),
            "column_names",
            "Columns seen in the data frame",
        ),
        EventMetadataEntry.text(
            str(df.isnull().sum()), "missing_values", "MIssing Values in DataFrame",
        ),
    ]


@dag.input_hydration_config(dag.Selector({"csv": dag.Field(dag.String)}))
def dataframe_input_hydration(context, selector):
    try:
        df = pd.read_csv(selector["csv"])
    except FileNotFoundError:
        raise Exception(f"File does not Exist:{selector['csv']}")
    except:
        raise Exception("Unreadable File")

    context.log.info(f"{df.shape[0]} Rows & {df.shape[1]} Columns")
    context.log.info(f"Data Info:\n {df.info()}")
    return df


SimpleDataFrame = dag.DagsterType(
    name="SimpleDataFrame",
    type_check_fn=lambda _, value: isinstance(value, pd.DataFrame),
    input_hydration_config=dataframe_input_hydration,
    description="A csv file representing a DataFrame",
)
