import pandas as pd
import numpy as np
import streamlit as st
from src.pipeline.predict_pipeline import PredictPipeline,CustomData
from sklearn.preprocessing import StandardScaler


df=pd.read_csv('data/final_data.csv')
title='Agriculture yields Prediction'


def main():
    st.set_page_config(layout='centered',page_title=title)
    st.title(title)
    form=st.form("Input Data")
    province_name=form.selectbox("province name",
                                [i for i in df.province_name.unique().tolist()]                                         
                                    )
    nama_komoditas=form.selectbox("commodity  name",
                                [i for i in df.nama_komoditas.unique().tolist()]
                                    )
    Tn=form.number_input("Minimum Themperature",min_value=0.0,max_value=100.0, step=1., format="%.2f")
    Tx=form.number_input("Maximum Themperature",min_value=0.0,max_value=100.0, step=1., format="%.2f")
    Tavg=form.number_input("Average Themperature",min_value=0.0,max_value=100.0, step=1., format="%.2f")
    RH_avg=form.number_input("Average Humidity (%)",min_value=0.0,max_value=100.0, step=1., format="%.2f")
    RR=form.number_input("Rainfall",min_value=0.0,max_value=100.0,step=1., format="%.2f")
    ss=form.number_input("Sunshine Duration",min_value=0.0,max_value=24.0,step=1., format="%.2f")
    ff_x=form.number_input("Max Wind Speed",min_value=0.0,max_value=25.0,step=1., format="%.2f")
    ddd_x=form.number_input("Wind Direction at Max Speed",min_value=0.0,max_value=360.0,step=1., format="%.2f")
    ff_avg=form.number_input("Min Wind Speed",min_value=0.0,max_value=25.0,step=1., format="%.2f")
    luar_wilayah_hektar=form.number_input("Agricultural Area", step=1., format="%.2f")
    tahun=form.number_input("Year")
    submit=form.form_submit_button("predict the commodity yields")

    if submit:
        data=CustomData(
                province_name=province_name,
                nama_komoditas=nama_komoditas,
                Tn=Tn,
                Tx=Tx,
                Tavg=Tavg,
                RH_avg=RH_avg,
                RR=RR,
                ss=ss,
                ff_x=ff_x,
                ddd_x=ddd_x,
                ff_avg=ff_avg,
                luar_wilayah_hektar=luar_wilayah_hektar,
                tahun=tahun
        )
        predict_df=data.get_data_as_data_frame()
        print(predict_df)

        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(predict_df)

        st.success("The yield of commodity is : " + str(results[0]))

if __name__=="__main__":
    main()
    

#        data = {
#            "province_name":province_name,
#            "nama_komoditas":nama_komoditas,
#            "Tn":Tn,
#            "Tx":Tx,
#            "Tavg":Tavg,
#            "RH_avg":RH_avg,
#            "RR":RR,
#            "ff_x":ff_x,
#            "ddd_x":ddd_x,
#            "ff_avg":ff_avg,
#            "luar_wilayah_hektar":luar_wilayah_hektar,
#            "tahun":tahun,
#            }