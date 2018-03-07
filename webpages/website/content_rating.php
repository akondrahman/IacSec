<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>Security anti-patterns in configuration scripts</title>
<link rel="stylesheet" href="css/styles.css">

<?php
session_start();
if(isset($_SESSION['rating_cnt']))
{
   #echo "asi mama";
   $_SESSION['rating_cnt'] = $_SESSION['rating_cnt'] + 1;
}
else
{
   #echo "ekhaneo asi";
   $_SESSION['rating_cnt'] = 1;
   $_SESSION['tkn'] = $_POST['tokenTxt'];
   $_SESSION['st_time'] = time();
}
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
<?php

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error)
{
    die("Connection failed: " . $conn->connect_error);
}

/*
5 will be modiified to 100, depending on class size, per student repsoibility
if you want 5 put 6, as the 5th data must be entered , at the 6th iteration 

Laurie wants each students to review 15-20, as per BIBD rule we get 18 
Chnaging 6 to 19 
*/

if($_SESSION['rating_cnt'] >= 19) 
{
  #session_unset();
  #session_destroy(); 
  header("Location: http://13.59.115.46/website/complete.php"); 
  #exit();
}

$tknText=$_SESSION['tkn'];
$tknText=validateData($tknText);
/*get studentID from table*/
$std_stmt = $conn->prepare("SELECT `ID` FROM `token` WHERE `token`=?");
$std_stmt->bind_param('s', $tknText);
$std_stmt->execute();
$std_stmt->bind_result($studentID);
$std_stmt->fetch();
//echo"AFTER:".$studentID;
$std_stmt->close();

//check if studentID is valid, if nto redirect to start page and destroy all sessions
if($studentID==NULL)
{
           echo"Sorry. Your login credentials are invalid.  You will now be redirected to the start page in three seconds ...";
           session_unset();
           session_destroy(); 
           header("Refresh:3; url=http://13.59.115.46/website/start.php"); 
           exit();
}
echo"<h3>Look at the script and see if any of the anti-patterns mentioned on the right exist</h3>";
#echo "WELCOME! ".$studentID ;
echo "<br />";
/*get count from session*/
$countID=$_SESSION['rating_cnt'];
#echo "Count ID: <br />".$countID;
/*get script ID from studentID and count*/
$assi_stmt = $conn->prepare("SELECT `scriptID` FROM `assignment` WHERE `studentID`=? AND `countID`=?");
$assi_stmt->bind_param('ii', $studentID, $countID);
$assi_stmt->execute();
$assi_stmt->bind_result($scriptID);
$assi_stmt->fetch();
$assi_stmt->close();
$scriptID=(int)$scriptID;
#printf("For script:%s, count:%s, student:%s", $scriptID, $countID, $studentID);

$stmt = $conn->prepare("SELECT `content` FROM `script` WHERE `ID`=?") ;
$stmt->bind_param('i', $scriptID) ;  /* i means int, s means string , d means double */
$stmt->execute() ;
$stmt->bind_result($content) ;
$stmt->fetch();
#$content=nl2br($content);
#printf("For ID:%s, content is:%s", $id, $content);
$stmt->close();

echo"<table>";
echo"<tr>";
echo"<td>";
echo"<textarea name ='content_txt' cols=80  rows=50 readonly>";
echo $content ;
echo"</textarea>";
echo"</td>";

echo"<td>";
echo"<form action='content_rating.php' method='POST' name='fo_cr'>";
echo"Select the applicable anti-pattern:<br />";
$ap_stmt = $conn->prepare("SELECT * FROM `antipattern`") ;
$ap_stmt->execute();
$ap_stmt->bind_result($ap_ID, $ap_name, $ap_example); 
while ($ap_stmt->fetch())
{
  /*  echo"<input type='radio' name='radio_ap' value='$ap_ID'>$ap_name</input><br />"; */
  if($ap_ID==1)
  {
     echo"<input type='checkbox' name='ap_check_list[]' value=$ap_ID checked>$ap_name</input><br />";
  }
  else
  {
     echo"<input type='checkbox' name='ap_check_list[]' value=$ap_ID>$ap_name</input><br />";
  }
}
echo"<br />";
echo"Selected 'Other'? Please describe below: <br />";
echo"<textarea name='extra_smell' cols=25 rows=10>N/A</textarea><br />";
echo"<p><p>";
echo"<input type='submit' name='submitBtn' value ='Submit!'>";
echo"</form>";
echo"</td>";
echo"</tr>";
echo"</table>";
$ap_stmt->close();
?>
<?php
/*Block for form handling*/
if (isset($_POST['submitBtn'])) 
{
      //$apID=$_POST['radio_ap'];
      if((!empty($_POST['ap_check_list'])) && ($scriptID!=NULL) && ($studentID!=NULL))
      {
         foreach($_POST['ap_check_list'] as $apID)
         {
           $extraSmell=$_POST['extra_smell'];
           $extraSmell=validateData($extraSmell);
           $fullTxt="Antipattern:".$apID."Script:".$scriptID."Student:".$studentID."Extra:".$extraSmell; /*for debugging*/
           //echo"<b>$fullTxt</b>";  /*for debugging*/
           $ins_stmt = $conn->prepare("INSERT INTO `submission` (`studentID`, `scriptID`, `antipatternID`, `countID`, `extra`) VALUES (?, ?, ?, ?, ?)");
           $ins_stmt->bind_param('iiiis', $studentID, $scriptID, $apID, $countID, $extraSmell);  // 'iiiis' 4 i means the first four parameters are itnegers, the alst aprameter is string  
           $ins_stmt->execute();
           $ins_stmt->close();
         }
      }
}

function validateData($data){
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}
?>

<?php
$conn->close() ;
?>
              </div>
            </div>
           </div>
        <nav id="rightmenu">
	   <div class="innertube">
		<h3>Help materials</h3>
		  <ul>
		     <li><a href="materials/instruction.pdf">Instructions</a></li>
		     <li><a href="materials/puppet.pdf">Handbook on Puppet</a></li>
                     <li><a href="materials/chef.pdf">Handbook on Chef</a></li>
		  </ul>
           </div>
         </nav>
         <footer id="footer">
	    <div class="innertube">
		<p>Copyright: Realsearch group</p>
	    </div>
	</footer>
</body>
</html>
