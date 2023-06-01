
package sqlite;
import java.sql.*;
public class SQLite {

    
    public static void main(String[] args) {
        Connection conexion = null;
        try{
            String ruta = "jdbc:sqlite:C:/Users/Frank Crespo/Desktop/registros.db";
            conexion = DriverManager.getConnection(ruta);
            //declaramos variables en las que guardar la informacion
            int windows = 0;
            int mac = 0;
            int ubuntu = 0;
            int android = 0;
            String nwindows = "";
            String nmac = "";
            String nubuntu = "";
            String nandroid = "";
            
            Statement peticion = conexion.createStatement();
            //Pedimos cosas a la base de datos
            //Windows
            String consulta = "SELECT * FROM windows";
            ResultSet resultados = peticion.executeQuery(consulta);
            while(resultados.next()){windows = resultados.getInt("windows");}
            //Mac
            consulta = "SELECT * FROM Mac";
            resultados = peticion.executeQuery(consulta);
            while(resultados.next()){mac = resultados.getInt("windows");}
            //ubuntu
            consulta = "SELECT * FROM ubuntu";
            resultados = peticion.executeQuery(consulta);
            while(resultados.next()){ubuntu = resultados.getInt("windows");}
            //android
            consulta = "SELECT * FROM Android";
            resultados = peticion.executeQuery(consulta);
            while(resultados.next()){android = resultados.getInt("windows");}
            for(int i = 0;i<windows;i+=500){nwindows += "#";}
            for(int i = 0;i<mac;i+=500){nmac += "#";}
            for(int i = 0;i<ubuntu;i+=500){nubuntu += "#";}
            for(int i = 0;i<android;i+=500){nandroid += "#";}
            
            System.out.println("Windows:\t "+Integer.toString(windows)+" "+nwindows);
            System.out.println("Mac:\t\t "+Integer.toString(mac)+" "+nmac);
            System.out.println("ubuntu:\t\t "+Integer.toString(ubuntu)+" "+nubuntu);
            System.out.println("Android:\t "+Integer.toString(android)+" "+nandroid);
        }catch(SQLException e){
        System.out.println(e.getMessage());}
    }
    
}
