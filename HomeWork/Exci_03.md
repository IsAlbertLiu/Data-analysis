1.第一题
```python
import pandas as pd
import numpy as np
from numpy import NaN
df_obj=pd.DataFrame({'A':[1,2,7,3],
                   'B':[5,2,4,0],
                    'C':[8,4,2,5],
                    'D':[8,9,3,2]})
df_obj
```

2.第二题
```python
import pandas as pd
import numpy as np
from numpy import NaN
df_obj=pd.DataFrame({'A':[1,2,7,3],
                   'B':[5,2,4,0],
                    'C':[8,4,2,5],
                    'D':[8,9,3,2]})

df_obj.sort_values(by=['B'],ascending=False)
```

3.第三题
```python
import pandas as pd
import numpy as np
from numpy import NaN
df_obj=pd.DataFrame({'A':[1,2,7,3],
                   'B':[5,2,4,0],
                    'C':[8,4,2,5],
                    'D':[8,9,3,2]})

df_obj.sort_values(by=['B'],ascending=False)
df_obj.to_csv(r'D:\write_data.csv')
```

