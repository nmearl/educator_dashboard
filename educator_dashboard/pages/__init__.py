
import solara

from ..components.Dashboard import Dashboard
from ..components.SetClass import SetClass



from ..database.class_report import Roster
from typing import cast

from pandas import DataFrame




@solara.component
def Page():
    
    class_id = solara.use_reactive(195) # add class id here
    roster = solara.use_reactive(cast(Roster, None))
    first_run = solara.use_reactive(True)
    
    story_name = "Hubble Data Story"
    
    with solara.Card():
        #center on page
        solara.Markdown(f"# {story_name.title()} Educator Dashboard", style={'text-align': 'center', 'width': '100%'})

        SetClass(class_id, roster, first_run)
        
        Dashboard(roster) 
        # solara.DataFrame(df.value)


# The following line is required only when running the code in a Jupyter notebook:
Page()