<html>
    <head>
        <title>CoronaApp</title>
    </head>

    <body>
    <?php
    function is_in_array($search,$array){
        $bool = false;
        for($i = 0 ; $i < count($array);$i++){
            if(!empty($array[$i]) AND $array[$i] == $search){
                $bool = true;
            }
        }
        return $bool;
    }
    // Download File
    // shell_exec("python3 main.py");
    require_once('vendor/autoload.php'); // load the main class file (if you're not using autoloader)

    if ( $xlsx = SimpleXLSX::parse('Fallzahlen_Kum_Tab.xlsx') ) {
        // Sheet numeration started 0, we select second worksheet
        $sheets=$xlsx->sheetNames();

        $arr_datum  = Array();
        $arr_zahlen = Array();
        foreach($sheets as $index => $name){
            // echo "Reading sheet :".$name."<br>";
            if($name == "LK_7-Tage-Fallzahlen"){
                foreach ( $xlsx->rows($index) as $r => $row ) {

                    if(is_in_array("LKNR", $row)){
                        for($i =0; $i < count($row);$i++){
                            if(preg_match('~[0-9]+~', $row[$i])) {
                                $arr_datum[] = $row[$i];
                            }
                        }
                    }elseif(is_in_array("LK Leer", $row)){
                        for($i =1; $i < count($row);$i++){
                            if(preg_match('~[0-9]+~', $row[$i]) AND $row[$i] <> "3457" ) {
                                $arr_zahlen[] = $row[$i];
                            }
                        }
                    }
                }

            }
        }
    } else {
        echo SimpleXLSX::parseError();
    }

    ?>
    </body>
</html>