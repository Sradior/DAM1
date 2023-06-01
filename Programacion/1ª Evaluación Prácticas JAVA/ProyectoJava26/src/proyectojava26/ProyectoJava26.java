
package proyectojava26;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ProyectoJava26 {

    public static void main(String[] args) {
        String correo = "^[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,}$"; //expresion regular para validar
        Pattern patron = Pattern.compile(correo,Pattern.CASE_INSENSITIVE);
        Matcher frase = patron.matcher("El zumo tiene coco y piña");
    
        boolean encontrado = frase.find();
        
        if(encontrado){
            System.out.println("Si que se ha encontrado");
        }else{
            System.out.println("No que se ha encontrado");
        }
    
    }
    
}
