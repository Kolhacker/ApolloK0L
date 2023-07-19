const http = require('http')
var readline = require('readline'); 
var rl = readline.createInterface({ 
input: process.stdin, 
output: process.stdout 
});

console.log ("")
console.log ("                  <<<<< Coded By HamZsaja >>>>>")
console.log("┌─────────────────────────────────────────────┐")
console.log("│              Protect By HamZsaja:)          │")
console.log("├─────────────────────────────────────────────┤")
console.log("│                 Added New Feature:          │")
console.log("│          [+] Custom Http :)                 │")
console.log("│          [+] Anti Reader :)                 │")
console.log("│          [+] Limiter & Rate Limiter :)      │")
console.log("├─────────────────────────────────────────────┤")
console.log("│              Credit : HamZsaja              │")
console.log("└─────────────────────────────────────────────┘") 
console.log ("")

rl.question("Password : ", function(password) {
   if (password == "@hamzsaja") 
    {
        console.clear()
        var prompt = require('prompt-sync')();
        var ip = prompt("IP Addres: ");
        console.clear()
        var httpcode = prompt("HTTP Code (Default 999) : ");
        console.clear()


        const client = http.createServer(function (req, res) {
            let ipAddress = req.connection.remoteAddress;
            ipAddress = ipAddress.split(/::ffff:/g).filter(a => a).join('');
            if (req.url == "/growtopia/server_data.php") {
                if (req.url = "TRACE") {
                    res.write(`server|` + ip + `\nport|17091\ntype|1\n#maint|PROTECTED BY HamZ\n\nbeta_server|127.0.0.1\nbeta_port|17091\n\nbeta_type|1\nmeta|localhost\nRTENDMARKERBS1001`);
                    res.end();
                    console.log(`[!] Access Ip: ${ipAddress}\n[!] Req Method: ${req.method}\n[!] Access Logs: ${req.url}\n==========================`);
                }
            }

            else {
                res.writeHead(httpcode, "HamZ Http Protected");
                res.write(`<script>alert('HamZ Http Protected');</script><pre>Protect By HamZ HTTP Your IP ${ipAddress}`);
                res.end();
                res.destroy();
            }
        })
        client.listen(80)
        console.log("                    << <<<HamZ HTTP>>>>>")
        console.log("                          New Anti DDos") 
        console.log("                        Credit By : HamZsaja")
        console.log("                     Anti DDoS Lead BY HamZ")
        console.log('                       \u001B[36mIP Addres: ' + ip)
        console.log('                       \u001B[35mHTTP Code: ' + httpcode)
    }
        else
    {
        console.log("Wrong password")
        process.exit(0); //kode exit
    }
    rl.close();
});