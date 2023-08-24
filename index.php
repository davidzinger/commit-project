<!DOCTYPE html>
<html>
    <head>
        <title>Welcome to commit!</title>
            <style>
                body {
                    width: 35em;
                    margin: 0 auto;
                    font-family: Tahoma, Verdana, Arial, sans-serif;
                }
            </style>
    </head>
    


    <body>
    <h1>Welcome to COMMIT!!</h1>
    
    
    
        <h2>My sql query!:</h2>
        <?php
        $connect = mysqli_connect('database-1.cwam3ksbsrrp.us-east-1.rds.amazonaws.com', 'user', 'password', 'commitdb');
        $query = 'SELECT * FROM movies';
        $result = mysqli_query($connect, $query);

        while($record = mysqli_fetch_assoc($result)){

            print_r($record);

        }
        

        ?>
        <img src="logo.jpg" width="500" height="200">
    </body>
</html>
