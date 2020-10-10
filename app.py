import flask
import requests
from flask import Flask,render_template,request
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    r=requests.get('http://www.omdbapi.com/?t=The Shawshank Redemption&apikey=25851263')
    a=r.json()
    movie_1_plot=a['Plot']
    movie_1_year=a['Title']
    movie_1_poster=a['Poster']
    r=requests.get('http://www.omdbapi.com/?t=Fight Club&apikey=25851263')
    a=r.json()
    movie_2_plot=a['Plot']
    movie_2_year=a['Title']
    movie_2_poster=a['Poster']
    r=requests.get('http://www.omdbapi.com/?t=The Godfather&apikey=25851263')
    a=r.json()
    movie_3_plot=a['Plot']
    movie_3_year=a['Title']
    movie_3_poster=a['Poster']
    r=requests.get('http://www.omdbapi.com/?t=Pulp Fiction&apikey=25851263')
    a=r.json()
    movie_4_plot=a['Plot']
    movie_4_year=a['Title']
    movie_4_poster=a['Poster']
    r=requests.get('http://www.omdbapi.com/?t=Dark Knight&apikey=25851263')
    a=r.json()
    movie_5_plot=a['Plot']
    movie_5_year=a['Title']
    movie_5_poster=a['Poster']
    r=requests.get('http://www.omdbapi.com/?t=Forrest Gump&apikey=25851263')
    a=r.json()
    movie_6_plot=a['Plot']
    movie_6_year=a['Title']
    movie_6_poster=a['Poster']
    r=requests.get('http://www.omdbapi.com/?t=Inception&apikey=25851263')
    a=r.json()
    movie_7_plot=a['Plot']
    movie_7_year=a['Title']
    movie_7_poster=a['Poster']
    r=requests.get('http://www.omdbapi.com/?t=Interstellar&apikey=25851263')
    a=r.json()
    movie_8_plot=a['Plot']
    movie_8_year=a['Title']
    movie_8_poster=a['Poster']
    r=requests.get('http://www.omdbapi.com/?t=The Empire Strikes back&apikey=25851263')
    a=r.json()
    movie_9_plot=a['Plot']
    movie_9_year=a['Title']
    movie_9_poster=a['Poster']
    r=requests.get('http://www.omdbapi.com/?t=Whiplash&apikey=25851263')
    a=r.json()
    movie_10_plot=a['Plot']
    movie_10_year=a['Title']
    movie_10_poster=a['Poster']
    r=requests.get('http://www.omdbapi.com/?t=Star Wars&apikey=25851263')
    a=r.json()
    movie_11_plot=a['Plot']
    movie_11_year=a['Title']
    movie_11_poster=a['Poster']
    r=requests.get('http://www.omdbapi.com/?t=Inside Out&apikey=25851263')
    a=r.json()
    movie_12_plot=a['Plot']
    movie_12_year=a['Title']
    movie_12_poster=a['Poster']
    r=requests.get('http://www.omdbapi.com/?t=The Green Mile&apikey=25851263')
    a=r.json()
    movie_13_plot=a['Plot']
    movie_13_year=a['Title']
    movie_13_poster=a['Poster']
    r=requests.get('http://www.omdbapi.com/?t=Spirited Away&apikey=25851263')
    a=r.json()
    movie_14_plot=a['Plot']
    movie_14_year=a['Title']
    movie_14_poster=a['Poster']
    r=requests.get('http://www.omdbapi.com/?t=Se7en&apikey=25851263')
    a=r.json()
    movie_15_plot=a['Plot']
    movie_15_year=a['Title']
    movie_15_poster=a['Poster']
    r=requests.get('http://www.omdbapi.com/?t=The Lord of the Rings: The Fellowship of the Ring&apikey=25851263')
    a=r.json()
    movie_16_plot=a['Plot']
    movie_16_year=a['Title']
    movie_16_poster=a['Poster']
    r=requests.get('http://www.omdbapi.com/?t=The Lord of the Rings: The Two Towers&apikey=25851263')
    a=r.json()
    movie_17_plot=a['Plot']
    movie_17_year=a['Title']
    movie_17_poster=a['Poster']
    r=requests.get('http://www.omdbapi.com/?t=The Godfather: Part II&apikey=25851263')
    a=r.json()
    movie_18_plot=a['Plot']
    movie_18_year=a['Title']
    movie_18_poster=a['Poster']



    return render_template('index.html',p_b=movie_1_plot,p_a=movie_1_year,m2t=movie_2_year,
    	m3t=movie_3_year,m4t=movie_4_year,m5t=movie_5_year,m6t=movie_6_year,m7t=movie_7_year,
    	m8t=movie_8_year, m9t=movie_9_year,m10t=movie_10_year,m11t=movie_11_year,m2p=movie_2_plot,
    	m3p=movie_3_plot,m4p=movie_4_plot,m5p=movie_5_plot,m6p=movie_6_plot,m7p=movie_7_plot,m8p=movie_8_plot,
    	m9p=movie_9_plot,m10p=movie_10_plot,m11p=movie_11_plot,m12t=movie_12_year,m13t=movie_13_year,
    	m14t=movie_14_year,m15t=movie_15_year,m16t=movie_16_year,m12p=movie_12_plot,m13p=movie_13_plot,
    	m14p=movie_14_plot,m15p=movie_15_plot,m16p=movie_16_plot,px=movie_1_poster,p2=movie_2_poster,
    	p3=movie_3_poster,p4=movie_4_poster,p5=movie_5_poster,p6=movie_6_poster,p7=movie_7_poster,
    	p8=movie_8_poster,p9=movie_9_poster,p10=movie_10_poster,p11=movie_11_poster,p12=movie_12_poster,
    	p13=movie_13_poster,p14=movie_14_poster,p15=movie_15_poster,p16=movie_16_poster)


@app.route('/getdata',methods=['GET','POST'])
def recon():
	return render_template('recom.html')
@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['tt']
    u=0
    data1=pd.read_csv('tmdb_5000_movies.csv')
    data1=data1.iloc[:,[3,6,7]]
    from sklearn.feature_extraction.text import TfidfVectorizer
    tfidfv=TfidfVectorizer(min_df=3,ngram_range=(1,3),max_features=None,stop_words='english',strip_accents='unicode', analyzer='word',token_pattern=r'\w{1,}',use_idf=1,smooth_idf=1,sublinear_tf=1)
    data1['overview']=data1['overview'].fillna('')
    tfidf_t=tfidfv.fit_transform(data1['overview'])
    from sklearn.metrics.pairwise import cosine_similarity,linear_kernel
    recommended=[]
    for i in range(0,len(data1)):
    	if(data1['original_title'][i]==text):
    		u=i
    		print(u)

    for i in range(0,len(data1)):
    	c=cosine_similarity(tfidf_t[u],tfidf_t[i])
    	##print(c)
    	x={'name':data1['original_title'][i],'similarity':c}
    	recommended.append(x)
    recommended=sorted(recommended, key = lambda i: i['similarity'],reverse=True)
    r_names=[]
    for i in range(0,10):
    	r_names.append(recommended[i]['name'])
    ##print(r_names)
    r=requests.get('http://www.omdbapi.com/?t='+r_names[0]+'&apikey=25851263')
    a=r.json()
    print(a)
    movie_1_plot=a['Plot']
    movie_1_year=a['Title']
    movie_1_poster=a['Poster']
    r=requests.get('http://www.omdbapi.com/?t='+r_names[1]+'&apikey=25851263')
    a=r.json()
    movie_2_plot=a['Plot']
    movie_2_year=a['Title']
    movie_2_poster=a['Poster']
    r=requests.get('http://www.omdbapi.com/?t='+r_names[3]+'&apikey=25851263')
    a=r.json()
    movie_3_plot=a['Plot']
    movie_3_year=a['Title']
    movie_3_poster=a['Poster']
    r=requests.get('http://www.omdbapi.com/?t='+r_names[4]+'&apikey=25851263')
    a=r.json()
    movie_4_plot=a['Plot']
    movie_4_year=a['Title']
    movie_4_poster=a['Poster']
    r=requests.get('http://www.omdbapi.com/?t='+r_names[5]+'&apikey=25851263')
    a=r.json()
    movie_5_plot=a['Plot']
    movie_5_year=a['Title']
    movie_5_poster=a['Poster']
    r=requests.get('http://www.omdbapi.com/?t='+r_names[6]+'&apikey=25851263')
    a=r.json()
    movie_6_plot=a['Plot']
    movie_6_year=a['Title']
    movie_6_poster=a['Poster']
    r=requests.get('http://www.omdbapi.com/?t='+r_names[7]+'&apikey=25851263')
    a=r.json()
    movie_7_plot=a['Plot']
    movie_7_year=a['Title']
    movie_7_poster=a['Poster']
    r=requests.get('http://www.omdbapi.com/?t='+r_names[8]+'&apikey=25851263')
    a=r.json()
    movie_8_plot=a['Plot']
    movie_8_year=a['Title']
    movie_8_poster=a['Poster']
   

    return render_template('final.html',p_b=movie_1_plot,p_a=movie_1_year,px=movie_1_poster,m2t=movie_2_year,m2p=movie_2_plot,p2=movie_2_poster,
    	m3t=movie_3_year,m3p=movie_3_plot,p3=movie_3_poster,m4t=movie_4_year,m4p=movie_4_plot,p4=movie_4_poster,
    	m5t=movie_5_year,m5p=movie_5_plot,p5=movie_5_poster,m6t=movie_6_year,m6p=movie_6_plot,p6=movie_6_poster,
    	m7t=movie_7_year,m7p=movie_7_plot,p7=movie_7_poster,m8t=movie_8_year,m8p=movie_8_plot,p8=movie_8_poster)


app.run()
