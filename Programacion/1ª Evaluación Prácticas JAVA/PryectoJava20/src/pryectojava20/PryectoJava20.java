
package pryectojava20;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

public class PryectoJava20 {


    public static void main(String[] args) throws IOException {
        int altura = 400;
        int anchura = 800;
        
        BufferedImage Adobecs = new BufferedImage(anchura,altura,BufferedImage.TYPE_INT_RGB); //creacion imagen
        Graphics2D graficos = imagencacheada.createGraphics();
        //para pintar//
        graficos.setColor(Color.PINK);
        graficos.fillRect(0, 0, anchura, altura);
        
        graficos.setColor(Color.red);
        graficos.fillRect(20, 20, 300, 300);
        
        graficos.setColor(Color.green);
        graficos.drawString("Programa de Jose Vicente", 300, 150);
        
        BufferedImage imagen = null; //recurso vacio 
        imagen = ImageIO.read(new File("logos/logo_java.png"));
        graficos.drawImage(imagen, 0,0,400,400, null);
        
        //para pintar//
        
        graficos.dispose();
        for(int i =0;i<10;i++){
            File archivo = new File ("guardado/primeraprueba"+i+".png"); //apunto un nuevo archivo 
            
            ImageIO.write(imagencacheada, "png", archivo);
        }        
                
    }
    
}
