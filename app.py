{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "cca160c1-fa9c-48c8-a13d-ae4db2eaeb25",
   "metadata": {},
   "outputs": [
    {
     "ename": "EOFError",
     "evalue": "Ran out of input",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mEOFError\u001b[0m                                  Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[6], line 9\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[38;5;66;03m# Load the saved model\u001b[39;00m\n\u001b[0;32m      8\u001b[0m pickle_in \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mopen\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mregressor.pkl\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mrb\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m----> 9\u001b[0m regressor\u001b[38;5;241m=\u001b[39m pickle\u001b[38;5;241m.\u001b[39mload(pickle_in)\n\u001b[0;32m     11\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mwelcome\u001b[39m():\n\u001b[0;32m     12\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mWelcome All\u001b[39m\u001b[38;5;124m\"\u001b[39m\n",
      "\u001b[1;31mEOFError\u001b[0m: Ran out of input"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pickle\n",
    "import pandas as pd\n",
    "import streamlit as st\n",
    "from PIL import Image\n",
    "\n",
    "# Load the saved model\n",
    "pickle_in = open(\"regressor.pkl\", \"rb\")\n",
    "regressor= pickle.load(pickle_in)\n",
    "\n",
    "def welcome():\n",
    "    return \"Welcome All\"\n",
    "\n",
    "def predict_house_price(Location, Size, Total_Sqft, Bath, Balcony):\n",
    "    \"\"\"\n",
    "    Predict House Price\n",
    "    This is using docstrings for specifications.\n",
    "    ---\n",
    "    parameters:\n",
    "      - name: Location\n",
    "        in: query\n",
    "        type: string\n",
    "        required: true\n",
    "      - name: Size\n",
    "        in: query\n",
    "        type: number\n",
    "        required: true\n",
    "      - name: Total_Sqft\n",
    "        in: query\n",
    "        type: number\n",
    "        required: true\n",
    "      - name: Bath\n",
    "        in: query\n",
    "        type: number\n",
    "        required: true\n",
    "      - name: Balcony\n",
    "        in: query\n",
    "        type: number\n",
    "        required: true\n",
    "    responses:\n",
    "        200:\n",
    "            description: The output values\n",
    "    \"\"\"\n",
    "    prediction = regressor.predict([[Location, Size, Total_Sqft, Bath, Balcony]])\n",
    "    print(prediction)\n",
    "    return prediction\n",
    "\n",
    "def main():\n",
    "    st.title(\"Bangalore House Price Prediction\")\n",
    "    html_temp = \"\"\"\n",
    "    <div style=\"background-color:tomato;padding:10px\">\n",
    "    <h2 style=\"color:white;text-align:center;\">House Price Predictor ML App</h2>\n",
    "    </div>\n",
    "    \"\"\"\n",
    "    st.markdown(html_temp, unsafe_allow_html=True)\n",
    "    Location = st.text_input(\"Location\", \"Type Here\")\n",
    "    Size = st.text_input(\"Size (BHK)\", \"Type Here\")\n",
    "    Total_Sqft = st.text_input(\"Total Square Feet\", \"Type Here\")\n",
    "    Bath = st.text_input(\"Number of Bathrooms\", \"Type Here\")\n",
    "    Balcony = st.text_input(\"Number of Balconies\", \"Type Here\")\n",
    "    \n",
    "    result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ee75b24d-6ca1-4bfd-be7d-9963c3f97937",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
