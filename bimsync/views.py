from django.shortcuts import render
from django.http import HttpResponse

from urllib.request import urlopen, HTTPError, Request
import urllib.error
from webbrowser import open_new
from urllib.parse import urlencode
import json
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime

API_BASE_URL = 'https://api.bimsync.com/1.0/'
API_BETA_URL = 'https://api.bimsync.com/beta/'
BASE_APP_URL = 'http://localhost:8000/bimsync'
REDIRECT_URL = 'http://localhost:8000/bimsync/code'

# Replace these variables with your app credentials and projectId
CLIENT_ID='JWt0MMGGIjNxr5A'                     # Put your client id here
CLIENT_SECRET= 'cs1ra9KmrqVlJ9f'                # Put your client secret here
PROJECT_ID='3f79feb6403f461a81d6c8766590b8ec'   # Put your projectId here

def index(request):
    html = "Bimsync API demo"
    if 'bs-access' in request.session:
        try: 
            viewerUrl = getViewer(request.session['bs-access'], PROJECT_ID)
            viewer2dUrl = getViewer2d(request.session['bs-access'], PROJECT_ID)
            t = get_template('viewer.html')
            html = t.render(Context({'viewerUrl' : viewerUrl, 'viewer2dUrl' : viewer2dUrl}))
        except urllib.error.HTTPError as e: 
            print(e.code)
            if e.code == 401:
                getAccess()
            else:
                return HttpResponse(str(e.code) + " " + e.reason)
    else:
        getAccess();
    return HttpResponse(html)

def code(request):
    code_ = request.GET.get('code')
    request.session['bs-access'] = getAccessToken(code_)
    open_new(BASE_APP_URL)
    return HttpResponse();

def getAccess():
    url = API_BASE_URL + 'oauth/authorize?client_id=' + CLIENT_ID + '&redirect_uri=' + REDIRECT_URL + "&response_type=code&state=1"
    request = Request(url)
    open_new(url)

def getAccessToken(code_):
    url = API_BASE_URL + 'oauth/access_token'
    post_fields = { "grant_type": "authorization_code",
                    "code": code_,
                    "client_id": CLIENT_ID,
                    "client_secret": CLIENT_SECRET}

    request = Request(url, urlencode(post_fields).encode('utf-8'), { "Content-Type": "application/x-www-form-urlencoded"})
    data = urlopen(request).read().decode('utf-8')
    return json.loads(data)['access_token']

def getProjects(access_token):
    url = API_BASE_URL + 'projects'
    request = Request(url, None, { "Authorization": "Bearer " + access_token})
    
    data = urlopen(request).read().decode('utf-8')
    projects = json.loads(data);

    for project in projects:
        print(project['name'].encode('utf-8'))
        
    return projects

def getFirstProjectId(access_token):
    for project in getProjects(access_token):
        print(project['name'].encode('utf-8'))
        return project['id']

def getViewer(access_token, projectId):
    url = API_BASE_URL + 'viewer/access?project_id=' + projectId
    request = Request(url, "".encode('utf-8'), { "Authorization": "Bearer " + access_token})
    data = urlopen(request).read().decode('utf-8')
    viewerToken = json.loads(data);
    return viewerToken['url'];

def getViewer2d(access_token, projectId):
    url = API_BETA_URL + 'viewer2d/access?project_ref=' + projectId
    request = Request(url, "".encode('utf-8'), { "Authorization": "Bearer " + access_token})
    data = urlopen(request).read().decode('utf-8')
    viewer2dToken = json.loads(data);
    return viewer2dToken['url'];
