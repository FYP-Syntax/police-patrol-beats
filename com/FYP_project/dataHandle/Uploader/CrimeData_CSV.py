import pandas as pd
import numpy as np
from datetime import datetime

data_set_url = './data/Police_Department_Incident_Reports_Historical_2003_to_May_2018.csv'

data_types = {
    'IncidntNum': np.dtype(str),
    'Category': np.dtype(str),
    'Descript': np.dtype(str),
    'DayOfWeek': np.dtype(str),
    'Date': np.dtype(datetime),
    'Time': np.dtype(datetime),
    'PdDistrict': np.dtype(str),
    'Resolution': np.dtype(str),
    'Address': np.dtype(str),
    'X': np.dtype(float),
    'Y': np.dtype(float),
    'Location': np.dtype(str),
    'PdId': np.dtype(int)
}

data = pd.read_csv(data_set_url, dtype=data_types)
