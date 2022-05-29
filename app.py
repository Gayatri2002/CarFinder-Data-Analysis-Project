#Gayatri Kalyani Data Analysis Project (CarFinder)

#Importing all the necessary libraries
from ctypes import alignment


import json
import streamlit as st
import pickle
import pandas as pd

import numpy as np
import plost
import requests  
import streamlit as st  
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu 



#price prediction model intigrating using pickle, the python ml model is in Car_Price.ipynb
model = pickle.load(open('RF_price_predicting_model.pkl','rb'))


#Defining main function 
def main():
    string = "CarFinder"  #Website name
    st.set_page_config(page_title=string, page_icon="🚗",layout="wide") #Webpage configuration
    
    #Reducing the white space present at the starting of the webpage
    st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 1rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 0rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

    #Hiding default streamlit footer. with this command you can hide menu #MainMenu {visibility: hidden;} 
    hide_st_style = """
            <style>
            
            footer {visibility: hidden;}
            
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    #creating navigation bar with 5 tabs of website 
    selected = option_menu(menu_title=None, options=["Home", "Car Price Predictor", "Cars info", "Sales Dashboard", "Web info"],
                            icons=["house","calculator","clipboard-data","graph-up-arrow","bar-chart"], orientation="horizontal",
                            styles={"container": {"layout":"wide"}
                                    
                                    
            },)

    #First page of the website and Containt of Home Page
    if selected == "Home":
        
        #inserting animation from lottieFiles 
        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

        
        #inserting Welcome statement with css styling 
        st.markdown("<h1 style='text-align: center; font-weight: bold;'>Welcome to CarFinder</h1>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center;'>Get your car's genuine value and information all in one location</h5>", unsafe_allow_html=True)

        
        #Introduction of website with information about project idea
        col1,col2,col3,col4 = st.columns(4)
        with col1:
            lottie_first = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_kkwptb3f.json")
    
            st_lottie(lottie_first, height=350, width=350, key="first" )

        with col2:
            st.markdown("##### 🚗 Are you considering selling your old automobile or purchasing a new one??\n##### Then you've come to the right spot. ")
            st.markdown("##### With our clever car price predictor, you can get an accurate selling price for your automobile.")
            st.markdown("##### Get all the information you need on various car models, their pricing trends, and much more...")
            
        
 

        
        with col3:
            def load_lottieurl(url: str):
                r = requests.get(url)
                if r.status_code != 200:
                    return None
                return r.json()

            lottie_hello = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_asjtnqce.json")
    
            st_lottie(lottie_hello, height=300, width=300, key="hi")

         
        st.markdown("<h5 style='text-align: center;'>Our solution not only forecasts the price, but also delivers sales-related data</h5>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center;'>in the form of an intelligent dashboard that any sales or marketing teams may use.</h5>", unsafe_allow_html=True)
        
        with col4:
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            lottie_sec = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_80nu1g6c.json")
    
            st_lottie(lottie_sec, height=150, width=150, key="sec" )  

        
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')

        #footer of the website
        m1,m2,m3=st.columns(3)
        with m1:
            st.markdown("<h6 style='text-align: center;'>© 2022 CarFinder. All Rights Reserved</h6>", unsafe_allow_html=True)
    
        with m2:
            st.markdown("<h6 style='text-align: center;'>Made with ❤</h6>", unsafe_allow_html=True)

        with m3:
            st.markdown("<h6 style='text-align: center;'>Contact us: gayatrikalyani04@gmail.com</h6>", unsafe_allow_html=True)

    

    

    #Second page of the website, deployment of car price predictor model
    if selected == "Car Price Predictor":
        
        #car price prediction section

        col1,col2,col3 = st.columns(3)
        with col1:
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            def load_lottieurl(url: str):
                r = requests.get(url)
                if r.status_code != 200:
                    return None
                return r.json()
            
            lottie_car = load_lottieurl("https://assets9.lottiefiles.com/datafiles/HN7OcWNnoqje6iXIiZdWzKxvLIbfeCGTmvXmEm1h/data.json")
    
            st_lottie(lottie_car, height=350, width=350, key="car" )


            


        with col2:
            st.title("Car Price Predictor 🚗")

    

            st.markdown("##### Are you planning to sell your car !?\n##### So let's find the best price for your car.. 🤖 ")
            st.image(
                "https://upload.wikimedia.org/wikipedia/commons/1/1e/25_Years_of_Jaguar_R_Performance_Cars_%288837754720%29.jpg?20140424131340",
                width=400, # Manually Adjust the width of the image as per requirement
            )
            st.write('')
            st.write('')
            #Taking necessary inputs from the user
            Car_Name = st.text_input('Enter your car name', key='Car Name')
            Body_type = st.selectbox('Select Car type',('Hatchback','MPV','MUV','SUV','Sedan','Crossover','Coupe','Convertible','Sports-Hatchback',
                                                       'Sedan-Coupe','Sports','Crossover-SUV','SUV-Crossover','Sedan-Crossover','Sports-Convertible',
                                                       'Pick-up','Coupe-Convertible'))
            st.write("""<a style="color:inherit;" href = "https://www.acko.com/car-insurance/different-types-of-cars-in-india-car-body-types/">Click here to learn more about car types.</a>""",unsafe_allow_html=True)
            

            years = st.number_input('In which year car was purchased ?',1990, 2022, step=1, key ='year')
            Years_old = 2022-years

            Present_Price = st.number_input('What is the current ex-showroom price of the car ?  (In ₹lakhs)', 0.00, 50.00, step=0.5, key ='present_price')

            Kms_Driven = st.number_input('What is distance completed by the car in Kilometers ?', 0.00, 500000.00, step=500.00, key ='drived')

            Owner = st.radio("The number of owners the car had previously ?", (0, 1, 2, 3), key='owner')

            Fuel_Type_Petrol = st.selectbox('What is the fuel type of the car ?',('Petrol','Diesel', 'CNG'), key='fuel')
            if(Fuel_Type_Petrol=='Petrol'):
                Fuel_Type_Petrol=1
                Fuel_Type_Diesel=0
            elif(Fuel_Type_Petrol=='Diesel'):
                Fuel_Type_Petrol=0
                Fuel_Type_Diesel=1
            else:
                Fuel_Type_Petrol=0
                Fuel_Type_Diesel=0

            Seller_Type_Individual = st.selectbox('Are you a dealer or an individual ?', ('Dealer','Individual'), key='dealer')
            if(Seller_Type_Individual=='Individual'):
                Seller_Type_Individual=1
            else:
                Seller_Type_Individual=0	

            Transmission_Mannual = st.selectbox('What is the Transmission Type ?', ('Manual','Automatic'), key='manual')
            if(Transmission_Mannual=='Mannual'):
                Transmission_Mannual=1
            else:
                Transmission_Mannual=0

            

            st.write('')
            st.write('')
            if st.button("Estimate Price", key='predict'):
                #exception handling
                try:
                    Model = model  #get_model()
                    prediction = Model.predict([[Present_Price, Kms_Driven, Owner, Years_old, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual]])
                    output = round(prediction[0],2)
                    
                    if output<0:
                        st.warning("You will be not able to sell this car !!")
                    else:
                        st.success("You can sell the car for {} lakhs 🙌".format(output))  
                except:
                    st.warning("Opps!! Something went wrong\nTry again")

            
        with col3:
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            
            
            lottie_car2 = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_9tOMhs.json")
    
            st_lottie(lottie_car2, height=350, width=350, key="car2" )

    
    #Third page of website showing info about cars with city and fuel type filter
    if selected == "Cars info":
        
        # Displaying cars information sheet

        st.title(":car: Information about all the car models")
        st.write('')
        st.markdown("##### Find out everything you need to know about automobile models, including pricing, model year, and more. \n#####  You can also use the sidebar's cities filter.")
        st.write('')
    
        df = pd.read_excel(io='Pre-Owned Car Resale in India-2021.xlsx', engine='openpyxl', usecols='A:H', header=0)
    
        #sidebar filter code
        st.sidebar.header("Please Filter Here:")
        #command for city filter
        City = st.sidebar.multiselect("Select the city:", options=df["city"].unique(), default=df["city"].unique()
        )

        #command for fuel type filter
        fuel_type = st.sidebar.multiselect("Select the fuel type:", options=df["fueltype"].unique(), default=df["fueltype"].unique()
        )

        #defining and assigning the correct column from dataset
        df_selection = df.query(
            "city == @City & fueltype == @fuel_type"
        )
        # Displaying sheet
        st.dataframe(df_selection)

        st.write('')
        
        #Creating pie chart from the dataset using plotly
        #pie_chart = px.pie(df, title= 'sales by different companies', values= 'model_year', names='maker')

        #st.plotly_chart(pie_chart) #Displaying pie chart

        

    #Fourth page of website having Power BI sales dashboard
    if selected == "Sales Dashboard":

        
        ## -----Charts(Data Analysis and Visualization)-----
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.markdown("<h1 style='text-align: center;'>📈Know interesting trends in automotive industry</h1>", unsafe_allow_html=True)
        
        st.write('') 
        st.write('')
        nn1,nn2=st.columns([0.10,3])
        with nn2:
            st.markdown("<h4 style='text-align: center;'>Get all the information you need about selling trends in the automotive sector, such as the best-selling model and the most popular automobile model in your city, by using the dashboard below.</h4>", unsafe_allow_html=True)
            

        nn1,nn2=st.columns([0.05,3])
        with nn2:
            
            st.markdown("<h4 style='text-align: center;'>This dashboard is especially beneficial to car sales teams. They have access to all information on automobile businesses' car sales.</h4>", unsafe_allow_html=True)

       
        st.write('')   
        st.write('')
        st.write('')
        st.write('')

        #Embeding Power BI dashboard on website with the link 
        # Sales Dashboard
        n11,n22=st.columns([0.5,3])
        with n22:
            st.markdown("""
                <iframe title="Sales" width="1024" height="804" src="https://app.powerbi.com/view?r=eyJrIjoiYmNhYjUyYjktNjgxMS00MTIwLTkzMzYtYTEyZjA5ZmFkYjY4IiwidCI6Ijk5NTE1M2Q1LWQxN2YtNGMwOS04OWI0LTM3ZDFlMTUyODhkZiJ9&pageName=ReportSection" frameborder="0" allowFullScreen="true"></iframe>
                """, unsafe_allow_html=True) 
        

    #Fifth page of website with Power BI dashboard 
    if selected == "Web info":
        st.markdown("<h1 style='text-align: center;'>📝Find out how well our website is performing.</h1>", unsafe_allow_html=True)
     
        st.write('')
        nn1,nn2=st.columns([0.85,3])
        with nn2:
            st.markdown("#### Looking at the dashboard below will give you an idea of our website's reach", unsafe_allow_html=True)
            

        nn1,nn2=st.columns([0.89,3])
        with nn2:
            
            st.markdown("<h4>\tThis dashboard aids digital marketing teams in analysing users' interest.</h4>", unsafe_allow_html=True)
        
  
        st.write('')
        st.write('')
    
        #Embeding Power BI dashboard on website with the link 
        # Website Performance Dashboard 
         
        n11,n22=st.columns([0.5,3])
        with n22:
            st.markdown("""
                <iframe title="Website performance - Page 1" width="1024" height="612" src="https://app.powerbi.com/view?r=eyJrIjoiOTVkMThlNDUtNmNkYS00NzA0LWE3MzMtYWFiMGEwMzQ0MGJhIiwidCI6Ijk5NTE1M2Q1LWQxN2YtNGMwOS04OWI0LTM3ZDFlMTUyODhkZiJ9" frameborder="0" allowFullScreen="true"></iframe>
                """, unsafe_allow_html=True)
            
        
    
  
    st.write('')
    st.write('')
    st.write('')
    st.write('')


    
#Executing main function  
if __name__ == '__main__':
    main()
