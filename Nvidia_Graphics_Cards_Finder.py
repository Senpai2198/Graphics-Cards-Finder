import streamlit as st
import pandas as pd
##########################################################################################

GPC=pd.read_csv("Nvidia Graphics Cards.csv")
GPC.reset_index(drop=True, inplace=True)
#GPC=GPC.sort_values('Released Year')
NvidiaorAMD=['Both NVIDIA and AMD','NVIDIA','AMD']
database_url="https://www.techpowerup.com/gpu-specs/"

#########################################################################################
st.write("""
         # GRAPHICS CARD LIST FILTER
         """)
st.text('         The purpose of this application is to let user choose the specification they')
st.text('require from a graphics card either for their graphics intensive jobs, researchs')
st.text('or gaming in general.')
st.text('         It simple to use, just move the sliders in the sidebar and the graphics card list')
st.text(' will be filtered.')
st.text('Note: Only popular graphics cards from year 2010 are listed in this table!')

##########################################################################################    

st.sidebar.write('Move the sliders to filter the list:')

type_GPC = st.sidebar.selectbox('Select NVIDIA and/or AMD:', NvidiaorAMD, 0)

year = st.sidebar.checkbox('Sort Year', help=help_year)
if year:
        GPC=GPC.sort_values('Released Year')

memory = st.sidebar.slider('Select Lowest Memory Size (in Gb):', 1,24,1, help=help_memory)
    
gpu=st.sidebar.slider('Select lowest GPU Clock (in MHz):', 675,2321,675, help=help_gpu)
      
memory_c=st.sidebar.slider('Select Lowest Memory Clock (in MHz)', 900,2248, 900, help=help_memory_c)
     
shaders=st.sidebar.slider('Select Lowest Shaders:', 192,10496,192,help=help_shaders)

#########################################################################################

if type_GPC=='NVIDIA':
         GPC = GPC[GPC['Product Name'].str.contains('GeForce')]
elif type_GPC=='AMD':
         GPC = GPC[GPC['Product Name'].str.contains('Radeon')]
else:
         GPC = GPC

GPC = GPC[GPC['Memory (Gb)'] >= memory] 

GPC = GPC[GPC['GPU clock (MHz)'] >= gpu] 

GPC = GPC[GPC['Memory clock (MHz)'] >= memory_c] 

GPC = GPC[GPC['Shaders'] >= shaders] 


########################################################################################

if len(GPC.index)==0:
    st.subheader('No Graphics Cards Found')
else:
    st.table(GPC)

st.markdown('Database Source ---> [TechPowerUp: GPU Specs Database](%s)' % database_url)

st.image("https://www.gpumag.com/wp-content/uploads/2020/05/computer-graphics-card.jpg")

#########################################################################################

help_year = '''
Sort GPUs'released years in ascending order.
'''.strip()

help_memory = '''
GPU VRAM holds multiple data such as vertex (geometry), terrain, mesh , texture of the games.
If there isn't enough space in GPU memory, modern GPUs will use VRAM (a dedicated memory portion of CPU RAM).
'''.strip()

help_gpu = '''
Also known as engine clock, GPU clock speed indicates how fast the cores of a graphics processing unit (GPU) are.
The function of these cores is to render graphics; therefore, the higher the GPU clock speed, the faster the processing.
'''.strip()

help_memory_c = '''
The memory clock is the speed of the VRAM on the GPU.
'''.strip()

help_shaders = '''
A shader is a piece of code that is executed on the Graphics Processing Unit (GPU), usually found on a graphics card, 
to manipulate an image before it is drawn to the screen. Shaders allow for various kinds of rendering effect, ranging 
from adding an X-Ray view to adding cartoony outlines to rendering output.
'''.strip()

###########################################################################################
