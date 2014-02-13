<?php
$row = 1;
$result = array();
if (($handle = fopen("test1.csv", "r")) != FALSE) {
	// Ignore the header of the csv file
	fgets($handle);
	// Read data and store it in a 2-d array
	while (($data = fgetcsv($handle, 100, ","))!== FALSE ){
		$num = count($data);
		$result[$row -1] = $data;
		$row++;	
	}

	// Foreach and array_multisort used to sort data based on "route_id"
	foreach ($result as $key => $row){
		$runId[$key] = $row[2];
	}
	array_multisort($runId, SORT_ASC, $result); 
	fclose($handle);

	// Output the result in a human-friendly format
	echo "Train Line\tRoute\t\tRun Number\tOperator ID\n";
	for($i = 0; $i < sizeof($result); $i ++){
		echo $result[$i][0]."\t\t".$result[$i][1]."\t".$result[$i][2]."\t\t".$result[$i][3]."\n" ;
	}	
}
?>
