package proyectojava18;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;
import java.sql.ResultSet;
public class ProyectoJava18 {

    public static void main(String[] args) {
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conexion = DriverManager.getConnection("jdbc:mysql://localhost:3306/cursojava","cursojava","cursojava");
            Statement peticion = conexion.createStatement();
            ResultSet resultado = peticion.executeQuery("SELECT * FROM agenda");
            while(resultado.next()){
                System.out.println(resultado.getString(1) + "-" + resultado.getString(2) + "-" + resultado.getString(3)+ "-" + resultado.getString(4));
            }
        }catch(Exception e){
            e.printStackTrace();
            
        }

    }
    
}
