<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>Security anti-patterns in configuration scripts</title>
<link rel="stylesheet" href="css/styles.css">
<?php
/*Start session*/
session_start();
$tknText=$_SESSION['tkn'];

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error)
{
    die("Connection failed: " . $conn->connect_error);
}
/*get studentID from table*/
$std_stmt = $conn->prepare("SELECT `ID` FROM `token` WHERE `token`=?");
$std_stmt->bind_param('s', $tknText);
$std_stmt->execute();
$std_stmt->bind_result($studentID);
$std_stmt->fetch();
$std_stmt->close();
?>

</head>

<body>
                        <header id="header">
                                <div class="innertube">
                                        <h1><img src="img/realsearch.jpg" alt="Security Anti-patterns in Configuration Scripts"></h1>
                                </div>
                        </header>
                <div id="mainwrapper">
                        <div id="contentwrapper">
                                <div id="content" align="center">
                                   <div class="innertube">
                                      <h3>Thanks for your participation. Please tell a little about yourself.</h3>
<table>
<?php
echo"<form action='complete.php' method='POST' name='complete'>";
echo"<tr>";
echo"<td>";
echo"For how many years have you worked in the software industry?";
echo"</td>";
echo"<td>";
echo"<input type='text' name='txtSWE' id='txtSWE'></input>";
echo"</td>";
echo "</tr>";
echo"<tr>";
echo"<td>";
echo"For how many years have you worked with Chef/Puppet/Ansible scripts?";
echo"</td>";
echo"<td>";
echo"<input type='text' name='txtIaC' id='txtIaC'></input>";
echo"</td>";
echo"</tr>";
echo"<tr>";
echo"<td>";
echo"</td>";
echo"<td>";
echo"<input type='submit' name='btn' value ='Submit!'>";
echo"</td>";
echo"</tr>";
echo"</form>";
?>
</table>


<?php
/*Block for form handling*/
//echo"ASI".$studentID;
if (isset($_POST['btn'])) 
{
      //echo"LOL:".$studentID; 
      $exp_swe   =$_POST['txtSWE'];
      $exp_iac   =$_POST['txtIaC'];
      $start_time=$_SESSION['st_time']; 
      $timediff  =time() - $start_time;
      if(($exp_swe != NULL) && ($exp_iac != NULL)  && ($studentID!=NULL) && ($timediff != NULL))
      {
           $ins_stmt = $conn->prepare("INSERT INTO `profile` (`studentID`, `expSWE`, `expIAC`, `timeDIFF`) VALUES (?, ?, ?, ?)");
           $ins_stmt->bind_param('issi', $studentID, $exp_swe, $exp_iac, $timediff);
           $ins_stmt->execute();
           $ins_stmt->close();

           /*Now destroy all sessions and redirect to a different webpage*/
           echo"Thanks! You will now be redirected to the NCSU CSC Webpage in three seconds ...";
           session_unset();
           session_destroy(); 
           header("Refresh:3; url=https://www.csc.ncsu.edu/"); 
           exit();
      }
      else
      {
           session_unset();
           session_destroy(); 
           /*Now destroy all sessions and redirect to a different webpage*/
           echo"Sorry. Your data was not collected. Redirecting you to the start page in three seconds ...";
           header("Refresh:3; url=http://13.59.115.46/website/start.php"); 
           exit();
      }
}
?>
<?php
$conn->close() ;
?>
                           </div>
                          </div>
                         </div>
</body>
</html>
