<?php
    if(isset($_GET['name'])){
        echo "GET: 你的名字是:".$_GET['name'];
    }

    // 连接数据库
    $conn =mysqli_connect("localhost", "root", "root", "ajaxtest" );
    
    if(isset($_POST['name'])){
        echo "POST: 你的名字是:".$_POST['name'];
    
        //将数据转化,避免特殊字符被注入SQL
        $name = mysqli_real_escape_string($conn, $_POST['name']);
        //将数据构建数据库插入语句
        $query = "INSERT INTO user(name) VALUES('$name')";
        //执行并判断结果
        if(mysqli_query($conn, $query)){
            echo "<br>用户添加成功!";
        }
        else{
            echo "<br>用户添加失败".mysqli_error($conn);
        }
    }

?>
    