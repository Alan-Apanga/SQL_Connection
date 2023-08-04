# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 12:02:47 2023

@author: alann
"""

"""
                Connection setup
Streamlit comes installed with generic connections for SQL and Snowflake 
Snowpark. These may need additional packages installed to work properly

In most cases, you'll need to:
    1. Install any necessary packages in your environment 
    2. Set up credentials and connection information
    3. Import and initialize the connection in your app

Connection configuration and credentials can be provided in three ways:
    a) In .streamlit/secrets.toml
    b) In any native config file or ENV for the particular data source
    c) Passed directly as arguments to st.experimental_connection


This example uses a local SQLite database that sits alongside the app. 
The only extra dependency installed is SQLAlchemy.


 """
# All SQLConnections in Streamlit use SQLAlchemy. For most other SQL dialects,
# you also need to install the driver. But the SQLite driver ships with python3, 
# so it isn't necessary.

# Installing packages
# pip install SQLAlchemy==1.4

import streamlit as st



# =============================================================================
#               Set up credentials
# =============================================================================
# If you are using secrets.toml, you'll want to create a section called 
# [connections.<connection name>] and add parameters there. You can name the 
# connection whatever you'd like.

# When developing your app locally, add a file called secrets.toml in a folder 
# called .streamlit at the root of your app repo, and copy/paste your secrets 
# into that file.

# .streamlit/secrets.toml
# [connections.pets_db]
# url = "sqlite:///pets.db"

# Now you can initialize the connection in one line of code
# This handles secrets retrieval, setup, query caching and retries.
conn = st.experimental_connection('mysql', type='sql')

# Perform query.
# By default, query() results are cached without expiring. In this case, we set 
# ttl=600 to ensure the query result is cached for no longer than 10 minutes. 
# You can also set ttl=0 to disable caching
df = conn.query('SELECT * from pets;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")

