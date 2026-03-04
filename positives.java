@RestController
public class TestController {

    @GetMapping("/test-cmd")
    public String testCmd(@RequestParam String cmd) throws Exception {
        Runtime.getRuntime().exec(cmd);
        return "done";
    }

    @GetMapping("/test-sql")
    public void testSql(@RequestParam String email) throws Exception {
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost/db");
        Statement stmt = conn.createStatement();
        stmt.executeQuery("SELECT * FROM users WHERE email = '" + email + "'");
    }

    @GetMapping("/test-path")
    public String testPath(@RequestParam String file) throws Exception {
        Files.readString(Paths.get("./uploads/" + file));
        return "done";
    }
}