$a = 'something'
$b = 'everything'
$c = 123
$d = @(1, 2, 3)
$e = '8.8.8.8'
Write-Output $a
Write-Output $a$b
Write-Output $c
Write-Output -join($d)
Test-Connection  $e
[Reflection.Emit.OpCodes]