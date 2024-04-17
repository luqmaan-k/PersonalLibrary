import time
from typing import Dict
import streamlit as st
from hydralit import HydraHeadApp


class UserApp(HydraHeadApp):

    def __init__(self, title = '', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title


    def run(self) -> None:
        """
        Application entry point.
        """

        st.write("Welcome to your Personal Library 📚")