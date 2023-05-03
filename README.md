# django_task

api endpoints

"GET/api/works"            :- http://127.0.0.1:8000/api/works/
for getting all the works without any filter

"GET/api/works?work_type=" :- http://127.0.0.1:8000/api/works/?work_type=other  ,
                              http://127.0.0.1:8000/api/works/?work_type=youtube  ,
                              http://127.0.0.1:8000/api/works/?work_type=instagram 


"GET/api/work?artist=" :- http://127.0.0.1:8000/api/works/?artist=Smit  ,
                          http://127.0.0.1:8000/api/works/?artist=mike
                          

"GET/api/register" :- http://127.0.0.1:8000/api/register/  ,

data for adding the user (body) for register- 
{
    "username": "testuser1",
    "password": "123321"
}
{
    "username": "testuser2",
    "password": "123hello"
}

everytime a new user is registered a client object is created
