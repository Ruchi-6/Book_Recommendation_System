# Book_Recommendation_System
## This is a colaborative Based Filtering

# *********************************************************

## Import necessary libraries
![import](https://user-images.githubusercontent.com/92905284/218269236-31ec3897-792e-4a75-ba36-5116a4ea0097.png)
## Read csv files - 'books.csv' , 'users.csv' and 'ratings.csv' and storing them in 'books' , 'users' and 'ratings' variables respectively
![read](https://user-images.githubusercontent.com/92905284/218269240-f80a9a32-7cc1-461f-9213-48920fe74620.png)

## Fetch top 5 records of books dataframe
![book](https://user-images.githubusercontent.com/92905284/218269246-ec8530b7-784d-497f-a6d2-2b3cc0346be4.png)

## Fetch top 5 records of users dataframe
![user](https://user-images.githubusercontent.com/92905284/218269247-f5ec5478-032d-437f-9698-26807fc8e38e.png)

## Fetch top 5 records of ratings dataframe
![rating](https://user-images.githubusercontent.com/92905284/218269248-2dc9473e-820e-452b-9abc-56aaf556eb52.png)

## Create function to fetch the details of the dataframe like - shape of the dataframe , checking missing values and duplicate records in the dataframe.
![data_info](https://user-images.githubusercontent.com/92905284/218269249-67970a81-dc2f-49ca-b126-ea3f64f47a0c.png)

## Use above function to get the details of the books dataframe
![data_book](https://user-images.githubusercontent.com/92905284/218269253-9ab22225-d996-4f58-8291-54db9605143e.png)

## Use above function to get the details of the users dataframe
![data_user](https://user-images.githubusercontent.com/92905284/218269258-5e310068-a234-4c40-bbc6-a649a3f689c1.png)

## Use above function to get the details of the ratings dataframe
![data_rating](https://user-images.githubusercontent.com/92905284/218269262-44ce08bf-4d31-4944-ab5e-3da59d871e2a.png)

## Drop the 'Age' column from the users dataframe as it has more than 40% missing values and drop the missing data from books dataframe
![dropping](https://user-images.githubusercontent.com/92905284/218269264-defdbd8c-cb56-4094-bccf-dd6fbbaf68b2.png)

## Now merge the books and ratings dataframe on the basis of 'ISBN' and store it in 'book_ratings' variable
![mergingbookrating](https://user-images.githubusercontent.com/92905284/218269269-08112b1f-0c17-40ae-88bb-c68e9d3b957c.png)

## Create new dataframe named as 'num_rating' by grouping the book_ratings dataframe on the basis of 'Book-Title' and count the Book-Ratings . later on rename Book-ratings column as 'No._of_Ratings'
![groupby_1](https://user-images.githubusercontent.com/92905284/218269272-7ee2b82e-0a13-4cd2-b430-019dba80411b.png)

## Create new dataframe named as 'avg_rating' by grouping the book_ratings dataframe on the basis of 'Book-Title' and apply mean() function to get the average number of book ratings . Afterwards rename Book-ratings column as 'Average_Ratings'
![groupby2](https://user-images.githubusercontent.com/92905284/218269274-ca02352a-9638-4885-a7d0-b86de6464285.png)

## Now , again merge avg_rating dataframe and num_rating on the basis of 'Book-Title' and then store in 'book_rating_df'
![merging_1](https://user-images.githubusercontent.com/92905284/218269279-a9e0e6ef-9584-4d5b-82ba-b78b5850641f.png)

## Rounding the 'Average_Ratings' column values to one decimal place
![round](https://user-images.githubusercontent.com/92905284/218271741-01926e96-33e9-47c5-8d02-744355e0c56c.png)

## Keep only those records which has more than 250 number of ratings . After that fetch top 50 records and store in the 'popular_books' dataframe.
![250](https://user-images.githubusercontent.com/92905284/218271747-f0ef2950-9307-4b01-b62a-3adfb2e39b5f.png)

## Merge 'popular_books' dataframe with 'books' dataframe on the basis of 'Book-Title' and store in 'popular_books' itself.
![popular](https://user-images.githubusercontent.com/92905284/218271754-666fda12-2ba5-4025-bf66-b47411cfd6f4.png)

## Filter records which has number of Book-rating greater than equal to 200.
![filtering](https://user-images.githubusercontent.com/92905284/218271773-7cb42758-ba43-4f99-b841-5ed00fd6f67e.png)

## Group the data on the basis of 'Book-Title' where number of Book-Rating is greater than equal to 50.
![y](https://user-images.githubusercontent.com/92905284/218271776-5ceb5858-b96a-462e-8899-c909f42387cf.png)

## Create a pivot table where index of the table is 'Book-Title' , columns are 'User-ID' and values has 'Book-Rating' store it in 'final_pt' variable. After that, fill all the NaN values as 0.
![final_pt](https://user-images.githubusercontent.com/92905284/218271782-9656b2f5-1e89-4e40-bd4f-cc6a20b38d11.png)

## Find the cosine_similarity by passing final_pt dataframe
![similarity](https://user-images.githubusercontent.com/92905284/218271786-9b40b96c-ac7f-4dc1-815d-6d4cbbdfaeb9.png)

## Create a function named as recommend_books and pass one parameter book_name.
Use of this function is to pass the book_name it will find the index of the given book_name , then it will show top 6 similar books alongwith author names , image URLs.
![recommend](https://user-images.githubusercontent.com/92905284/218271795-433da9c9-c5dd-42fd-b9e6-0c8a71e3f717.png)

##  Call the above function and pass the book_name .
![testing](https://user-images.githubusercontent.com/92905284/218271799-bd9dc1fb-8346-4bbb-bfbc-6afe4e80fd92.png)

## Now , save the required files for deployment .
![dump](https://user-images.githubusercontent.com/92905284/218271804-fbfd8872-5e4d-4ee6-9f46-f9ff2768bc1c.png)


# ************************************************************

# DEPLOYMENT USING FLASK

### Create 1 python file app.py and two html file index.html and recommend.html.

## Codes in app.py file 
![1](https://user-images.githubusercontent.com/92905284/218273246-02719330-cc6c-48cf-a7d1-1f486e604492.png)
![2](https://user-images.githubusercontent.com/92905284/218273248-c7ab0492-2b6b-49ae-98e1-b910e2ff859d.png)

## Codes in index.html
![3](https://user-images.githubusercontent.com/92905284/218273251-73a2008b-6fe6-4699-b959-adc145b4bd2c.png)
![4](https://user-images.githubusercontent.com/92905284/218273252-dfd4624c-1ea9-4027-bdf3-353fbde0a0ed.png)

## Codes in recommend.html
![5](https://user-images.githubusercontent.com/92905284/218273257-afd6d5e3-8ff0-4bae-84bd-0cb81500782a.png)
![6](https://user-images.githubusercontent.com/92905284/218273264-93304f02-ef15-44b6-8277-615ffc74cffa.png)

## Now , run the app.py file 
![runi](https://user-images.githubusercontent.com/92905284/218273431-db867e35-0e80-4723-b23c-b858f5591812.png)

## click on the http link in the terminal 
![runi2](https://user-images.githubusercontent.com/92905284/218273490-b74d06e7-b2ce-4836-8dd2-7907b7aaf168.png)

## It will redirect to the browser which will show top 50 Books 
![d](https://user-images.githubusercontent.com/92905284/218273836-769d3e2d-4bbc-41fa-a090-b9c7b8c076d7.png)

## now, click on the recommend button 
![d2](https://user-images.githubusercontent.com/92905284/218273898-7eb1aabb-bfaa-4dad-87f2-6deb32a4045b.png)

## and then test the recommendation system by writing book name and it will recoomend 6 similar books
![d3](https://user-images.githubusercontent.com/92905284/218273950-af926cd5-889b-4dd5-b9cb-acd8adf58143.png)

# *************************** THE END ******************************











