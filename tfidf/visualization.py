import altair as alt
import numpy as np
import pandas as pd

tfidf_data_df = pd.read_csv('C:\\Users\\mc505\\Downloads\\College_Info_Program\\digitalethnicfutureslab\\tfidf_vectors.csv')
tfidf_data_df = tfidf_data_df[tfidf_data_df['tfidf score'] != 0.0]  

term_list = []

top_tfidf_plusRand = tfidf_data_df.copy()
top_tfidf_plusRand['tfidf score'] = top_tfidf_plusRand['tfidf score'] + np.random.rand(tfidf_data_df.shape[0]) * 0.0001

# base for all visualizations, with rank calculation
base = alt.Chart(top_tfidf_plusRand).encode(
    x = 'rank:O',
    y = 'document:N'
).transform_window(
    rank = "rank()",
    sort = [alt.SortField("tfidf", order="descending")],
    groupby = ["document"],
)

# heatmap specification
heatmap = base.mark_rect().encode(
    color = 'tfidf:Q'
)

# red circle over terms in above list
circle = base.mark_circle(size=100).encode(
    color = alt.condition(
        alt.FieldOneOfPredicate(field='term', oneOf=term_list),
        alt.value('red'),
        alt.value('#FFFFFF00')        
    )
)

# text labels, white for darker heatmap colors
text = base.mark_text(baseline='middle').encode(
    text = 'term:N',
    color = alt.condition(alt.datum.tfidf >= 0.23, alt.value('white'), alt.value('black'))
)

# display the three superimposed visualizations
#chart = (heatmap + circle + text)
#chart.save('visualization.html')
    

