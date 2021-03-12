import seaborn as sns
import streamlit as st

st.title("Old Faithful eruptions")

geyser = sns.load_dataset('geyser')

st.markdown(
  """
  This is a tiny app to explore the
  [Old Faithful Geyser Data](https://www.stat.cmu.edu/~larry/all-of-statistics/=data/faithful.dat).
  First, we can view some summary statistics.
  The `duration` variable is the duration of an eruption in minutes,
  and the `waiting` variable is the time between eruptions in minutes.
  """
)

st.write(geyser.describe().T)


"""
So the mean waiting time between eruptions is around 70 minutes,
with a mean eruption duration of three and a half minutes.
Summary statistics can be misleading.
Let us plot the waiting and duration variables against each other.

We'll use a joint density plot, with the marginal densities for each
variable on the corresponding axis.
There are clearly two clusters:
shorter eruptions with a shorter waiting time,
and longer eruptions with a longer waiting time.
These are labeled in our data set, so we separate the data and color by cluster.
"""


with sns.axes_style("white"):
    st.pyplot(
        sns.jointplot(
          data=geyser,
          x="waiting",
          y="duration",
          hue="kind",
          kind="kde"
        )
    )