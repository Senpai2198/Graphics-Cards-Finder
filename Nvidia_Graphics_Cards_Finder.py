import streamlit as st
import pandas as pd
##########################################################################################
#PC Components List
#memory_size=(1, 2, 4, 6, 8, 10, 11, 12, 16, 24)

nvidia=pd.read_csv("Nvidia Graphics Cards.csv")
nvidia.reset_index(drop=True, inplace=True)
nvidia=nvidia.sort_values('Released Year')

st.write("""
         # GRAPHICS CARD LIST FILTER
         """)
st.text('         The purpose of this application is to let user choose the specification they require from')
st.text('a graphics either for their graphics intensive jobs or hobby.')
st.text('')
st.text('         It simple to use, just move the sliders in the sidebar and the graphics card list will be filtered.')

st.text('Database Source: https://www.techpowerup.com/gpu-specs/')
##########################################################################################    

st.sidebar.write('Move the sliders to filter the list:')

memory = st.sidebar.slider('Select Lowest Memory Size (in Gb):', 1,24,1)
    
gpu=st.sidebar.slider('Select lowest GPU Clock (in MHz):', 675,2321,675)
    
    
memory_c=st.sidebar.slider('Select Lowest Memory Clock (in MHz)', 900,2248, 900)
    
    
shaders=st.sidebar.slider('Select Lowest Shaders:', 192,10496,192)

#########################################################################################

nvidia = nvidia[nvidia['Memory (Gb)'] >= memory] 

nvidia = nvidia[nvidia['GPU clock (MHz)'] >= gpu] 

nvidia = nvidia[nvidia['Memory clock (MHz)'] >= memory_c] 

nvidia = nvidia[nvidia['Shaders'] >= shaders] 


########################################################################################
if len(nvidia.index)==0:
    st.subheader('No Graphics Cards Found')
else:
    st.table(nvidia)
#########################################################################################

st.bar_chart(nvidia, width='Product Name', height='Memory (Gb)')
