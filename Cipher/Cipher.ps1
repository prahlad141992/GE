$str = Get-content $PSScriptRoot\input.txt
$rm = $str.Replace(" ", "")

$Set = @()
foreach($Name in $rm.ToCharArray() ){
    [char]$letter = $Name
    $letter = [byte]$letter + 3
    $Set += $letter

}

$Set -join ""
