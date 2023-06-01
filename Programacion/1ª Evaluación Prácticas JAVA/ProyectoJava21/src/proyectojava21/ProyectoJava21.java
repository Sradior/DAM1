
package proyectojava21;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import javax.imageio.ImageIO;


public class ProyectoJava21 {


    public static void main(String[] args) {
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conexion = DriverManager.getConnection("jdbc:mysql://localhost:3306/cursojava","cursojava","cursojava");
            Statement peticion = conexion.createStatement();
            ResultSet resultado = peticion.executeQuery("SELECT * FROM cursos");
            while(resultado.next()){
            System.out.println(resultado.getString(3));
            }
            /////////////////////////////////////////////////////
            int altura = 400;
            int anchura = 800;
        
            BufferedImage Adobecs = new BufferedImage(anchura,altura,BufferedImage.TYPE_INT_RGB);
            Graphics2D graficos = Adobecs.createGraphics();
            //para pintar//
            graficos.setColor(Color.PINK);
            graficos.fillRect(0, 0, anchura, altura);

            graficos.setColor(Color.red);
            graficos.fillRect(20, 20, 300, 300);

            graficos.setColor(Color.green);
            graficos.drawString(resultado.getString(3), 300, 150);

            BufferedImage imagen = null; 
            imagen = ImageIO.read(new File(resultado.getString(7)));
            graficos.drawImage(imagen, 0,0,400,400, null);

            //para pintar//

            graficos.dispose();

                File archivo = new File ("guardado/"+resultado.getString(2)+".png");

                ImageIO.write(adobecs, "png", archivo);
                ////////////////////////////////////////////////////
            
            }catch(Exception e){
        e.printStackTrace();   
        }
    }    
}