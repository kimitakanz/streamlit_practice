import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit test')


st.write('interactive widgets')

left_column, right_column = st.columns(2)
button = left_column.button('show right column')
if button:
    right_column.write('this is right column')



option = st.selectbox(
    'type a number',
    list(range(1,11))
)
'you choose the number ', option, 'from the list.'


text = st.text_input('type a number')
'you choose the number ', text

condition = st.slider('how do you feel now?', 0, 100, 50)
'condition', condition

if st.checkbox('Show Image'):
   img = Image.open('PoochJuice.png')
   st.image(img, caption='PoochJuice', use_column_width=True)

# df = pd.DataFrame({
#     'line1' : [1,2,3,4],
#     'line2' : [10,50,30,40]
# })

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69, 139.70],
    columns=['lat','lon',]
)
df

# st.write(df)

# st.dataframe(df.style.highlight_max(axis=0), width=300,  height=100)

# st.table(df.style.highlight_max(axis=0))

# st.line_chart(df)

# st.area_chart(df)

st.map(df)


"""
# chapter
## Paragraph
### Section
   
```python
import streamlit as st
import numpy as np
import pandas as pd
```
    
"""