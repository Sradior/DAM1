package proyectojava16;
import java.sql.Connetion;
import java.sql.DriverManager;                                                            
import java.sql.Statement;                                                     


public class ProyectoJava16 {

    public static void main(String[] args) {
        

try { 
    Class.forname("com.mysql.jdbc.Driver")
}//ahora establezco conexion
Connection conexion= DriverManager.getConnection("jdbc:mysql://localhost:3306/cursojava", "cursojava", "cursojava"};
//preparo una petición a la base de datos
Statement peticion = conexion. createStatement();
peticion.excecute("INSERT INTO agenda VALUES (NULL, 'Juan','1234', 'juan@gmail.com')");
   }catch(Exception e) {
e.printStrackTrace()
}