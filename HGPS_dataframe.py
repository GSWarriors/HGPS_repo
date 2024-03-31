import pandas as pd
import numpy as np

#sample dataset for hutchinson-gilford progeria syndrome (HGPS)
data = {
  'Patient_ID': [1, 2, 3, 4, 5],
  'Age': [2, 4, np.nan, 5, 2],
  'Height_cm': [70, np.nan, 72, 78, 71],
  'Weight_kg': [8, 10, 9, np.nan, 8.5],
  'Baldness': [1, 1, np.nan, 1, 1],
  'Skin_thickness': [0.8, 0.9, 0.85, np.nan, 0.82],
  'Joint_Stiffness': [1, np.nan, 0, 1, 0],
  'Bone_Density': [0.7, 0.6, np.nan, 0.58, 0.7],
  'Cardiovascular_Issues': [np.nan, 1, 0, 1, 0],
  'HGPS_Diagnosis': [1, 1, 0, 1, np.nan]
}

#create dataframe
df = pd.DataFrame(data)

print("the dataframe: " + str(df))
