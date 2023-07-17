# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 20:23:49 2023

@author: NAVEEN
"""

import streamlit as st
import numpy as np
import pickle
cricket_model = pickle.load(open('C:/models/cricket_model.sav','rb'))

def cricket_prediction(AverageScore,delivery_left,score,CurrentRunRate,wicketsLeft,Run_In_Last5,Wickets_In_Last5,innings,battingTeam,bowlingTeam,city):
  inp=np.array([[AverageScore,delivery_left,score,CurrentRunRate,wicketsLeft,Run_In_Last5,Wickets_In_Last5,innings,battingTeam,bowlingTeam,city]]).astype(np.float64)
  pred=cricket_model.predict(inp)
  print(pred)
  st.success(pred)
  
def main():
      #title of web 
      st.title('cricket_score_prediction_web')
      #getting inputdata
      AverageScore=st.text_input('AverageScore')
      delivery_left=st.text_input('delivery_left')
      score=st.text_input('score')
      CurrentRunRate=st.text_input('CurrentRunRate')
      wicketsLeft=st.text_input('wicketsLeft')
      Run_In_Last5=st.text_input('Run_In_Last5')
      Wickets_In_Last5=st.text_input('Wickets_In_Last5')
      innings=st.text_input('innings')
      battingTeam=st.text_input('battingTeam')
      bowlingTeam=st.text_input('bowlingTeam')
      city=st.text_input('city')


      cricket=""
 #creating a button
      if st.button("predict the score "):
        cricke=(cricket_prediction(AverageScore,delivery_left,score,CurrentRunRate,wicketsLeft,Run_In_Last5,Wickets_In_Last5,innings,battingTeam,bowlingTeam,city))
        cricket=(cricke)
        print(cricket)
        
if __name__=='__main__':
 main()
    