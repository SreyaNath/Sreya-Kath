users_Afghan = df[df['year-month-day'].isin(["21-08-15", "21-08-16", "21-08-17", "21-08-18", "21-08-19", "21-08-20", "21-08-22", "21-08-23", "21-08-24", "21-08-25" , "21-08-28", "21-08-29", "21-08-30", "21-08-31", "20-09-06", "20-10-28", "20-10-29", "20-10-30", "20-10-31"])].groupby(['user_screen_name']).agg({'id':'count', # total number of tweets in the dataset
                                              'like_count': ['sum','mean','max'],
                                              'retweet_count': ['sum','mean','max'],
                                             'user_id':'first',
                                              'user_name':'first',
                                              'user_verified':'first',
                                             'user_description':'first',
                                             'user_image':'first',
                                             'user_tweets':'first',
                                             'user_followers':'first',
                                             'user_friends':'first',
                                             'user_likes':'first',
                                             'user_lists':'first',
                                             'user_created_at':'first',
                                             'links': str_cat, # list of all links
                                             'text': str_cat, # list of all links
                                              'url': str_cat # list of all tweets
                                             }).reset_index()
users_Afghan.sort_values('retweet_count_max', ascending= False)
